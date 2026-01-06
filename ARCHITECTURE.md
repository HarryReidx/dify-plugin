# 架构说明 - HSE 安全检查表生成插件

## 数据流程图

```
┌─────────────────┐
│  Dify Workflow  │
│   (用户输入)     │
└────────┬────────┘
         │
         │ checklist_json (String)
         │
         ▼
┌─────────────────────────────────────┐
│  HseSafeChecklistTool               │
│  (_invoke method)                   │
│                                     │
│  1. 接收参数                         │
│  2. JSON 解析                        │
│  3. 数据验证                         │
└────────┬────────────────────────────┘
         │
         │ Parsed Data
         │
         ▼
┌─────────────────────────────────────┐
│  openpyxl Workbook                  │
│                                     │
│  1. 创建工作簿                       │
│  2. 设置样式                         │
│  3. 写入表头                         │
│  4. 写入字段名                       │
│  5. 遍历 sections                   │
│  6. 写入 section 标题               │
│  7. 写入 items 数据                 │
│  8. 应用边框和格式                   │
└────────┬────────────────────────────┘
         │
         │ Excel Workbook
         │
         ▼
┌─────────────────────────────────────┐
│  io.BytesIO                         │
│  (内存缓冲区)                        │
│                                     │
│  wb.save(excel_buffer)              │
└────────┬────────────────────────────┘
         │
         │ Binary Data
         │
         ▼
┌─────────────────────────────────────┐
│  ToolInvokeMessage                  │
│  (create_blob_message)              │
│                                     │
│  - blob: 二进制数据                  │
│  - mime_type: Excel 格式            │
│  - filename: 文件名                 │
└────────┬────────────────────────────┘
         │
         │ Blob Message
         │
         ▼
┌─────────────────┐
│  Dify Frontend  │
│   (文件下载)     │
└─────────────────┘
```

## 组件说明

### 1. Input Layer (输入层)

**组件**: Dify Workflow
**职责**: 
- 接收用户输入或 LLM 生成的 JSON
- 传递给工具节点

**数据格式**:
```json
{
  "tableName": "string",
  "columns": ["string"],
  "sections": [
    {
      "title": "string",
      "items": [{"id": "string", "content": "string", ...}]
    }
  ]
}
```

### 2. Processing Layer (处理层)

**组件**: HseSafeChecklistTool
**职责**:
- JSON 解析和验证
- 错误处理
- 调用 Excel 生成逻辑

**关键方法**:
```python
def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]
```

### 3. Generation Layer (生成层)

**组件**: openpyxl
**职责**:
- 创建 Excel 工作簿
- 应用样式和格式
- 单元格合并
- 边框和对齐

**关键操作**:
- `Workbook()`: 创建工作簿
- `ws.merge_cells()`: 合并单元格
- `cell.font/fill/alignment/border`: 设置样式
- `wb.save(buffer)`: 保存到内存

### 4. Serialization Layer (序列化层)

**组件**: io.BytesIO
**职责**:
- 在内存中缓存 Excel 文件
- 避免磁盘 I/O
- 提供二进制流

**优势**:
- 性能高（无磁盘操作）
- 安全（不留临时文件）
- 可扩展（支持大文件）

### 5. Output Layer (输出层)

**组件**: ToolInvokeMessage (Blob)
**职责**:
- 封装文件数据
- 提供元数据（MIME 类型、文件名）
- 返回给 Dify 前端

**消息结构**:
```python
{
  "blob": bytes,
  "meta": {
    "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "filename": "表名_检查表.xlsx"
  }
}
```

## 样式系统

### 样式定义

```python
# 表头样式
header_font = Font(bold=True, size=12)
header_fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# 字段名样式
column_font = Font(bold=True, size=11)
column_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
column_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Section 标题样式
section_font = Font(bold=True, size=11)
section_fill = PatternFill(start_color="EBF1DE", end_color="EBF1DE", fill_type="solid")
section_alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# 数据行样式
data_alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# 边框样式
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)
```

### 样式应用流程

```
1. 定义样式对象
   ↓
2. 创建单元格
   ↓
3. 应用样式属性
   ↓
4. 设置单元格值
   ↓
5. 添加边框
```

## 列宽策略

| 列 | 宽度 | 用途 |
|----|------|------|
| A (序号) | 10 | 短文本，如 "1.1" |
| B (内容) | 45 | 长文本，需要换行 |
| C-Z (其他) | 20 | 中等长度文本 |

## 错误处理流程

```
输入参数
   ↓
参数存在？ ──No──> 返回错误消息
   ↓ Yes
JSON 解析
   ↓
解析成功？ ──No──> 返回 JSON 错误
   ↓ Yes
验证 columns
   ↓
非空？ ──No──> 返回验证错误
   ↓ Yes
生成 Excel
   ↓
成功？ ──No──> 返回异常信息
   ↓ Yes
返回文件
```

## 性能特性

### 时间复杂度
- JSON 解析: O(n)
- Excel 生成: O(m × c)
  - m: 总行数（sections + items）
  - c: 列数

### 空间复杂度
- 内存占用: O(m × c)
- 文件大小: 约 6KB + (rows × 100 bytes)

### 性能基准
- 100 项: < 1 秒
- 500 项: < 3 秒
- 1000 项: < 5 秒

## 扩展点

### 1. 自定义样式
修改 `tools/hse_safe_checklist.py` 中的样式定义

### 2. 添加新列
在 JSON 的 `columns` 和 `items` 中添加新字段

### 3. 多语言支持
在 `tools/hse_safe_checklist.yaml` 中添加新语言

### 4. 自定义文件名
修改 `filename` 生成逻辑

### 5. 添加图表
使用 openpyxl 的 Chart 功能

## 依赖关系

```
HseSafeChecklistTool
    ├── dify_plugin (SDK)
    │   ├── Tool (基类)
    │   └── ToolInvokeMessage (消息类型)
    ├── openpyxl (Excel 库)
    │   ├── Workbook
    │   ├── styles (Font, Alignment, PatternFill, Border)
    │   └── utils
    ├── json (标准库)
    └── io (标准库)
```

## 安全考虑

1. **输入验证**: JSON 格式检查
2. **异常处理**: 捕获所有可能的错误
3. **内存管理**: 使用 BytesIO 避免文件泄露
4. **大小限制**: 建议限制输入数据大小
5. **注入防护**: 不执行用户提供的代码

## 测试策略

### 单元测试
- JSON 解析测试
- 样式应用测试
- 边界条件测试

### 集成测试
- 完整流程测试 (`test_tool.py`)
- Dify 工作流测试

### 性能测试
- 大数据量测试
- 内存使用监控
- 执行时间测量

## 维护建议

1. **定期更新依赖**: 保持 openpyxl 最新版本
2. **监控性能**: 记录执行时间和内存使用
3. **收集反馈**: 了解用户需求和问题
4. **版本控制**: 使用语义化版本号
5. **文档更新**: 保持文档与代码同步
