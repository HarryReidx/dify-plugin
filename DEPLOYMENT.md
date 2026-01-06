# HSE 安全检查表插件 - 部署指南

## 前置要求

1. **Python 环境**: Python 3.8 或更高版本
2. **Dify CLI**: 已安装 Dify 命令行工具
3. **Dify 平台**: 可访问的 Dify 实例

## 安装步骤

### 1. 安装依赖

在插件根目录执行：

```bash
pip install -r requirements.txt
```

这将安装：
- `dify_plugin` (Dify 插件 SDK)
- `openpyxl` (Excel 文件处理库)

### 2. 验证插件结构

确保以下文件存在且配置正确：

```
hse_safe_checklist/
├── main.py                          # 插件入口
├── manifest.yaml                    # 插件清单
├── requirements.txt                 # Python 依赖
├── tools/
│   ├── hse_safe_checklist.py       # 工具实现
│   └── hse_safe_checklist.yaml     # 工具配置
├── example_checklist.json          # 示例数据
├── USAGE_CN.md                     # 使用说明
└── DEPLOYMENT.md                   # 本文件
```

### 3. 本地测试（可选）

运行测试脚本验证 Excel 生成逻辑：

```bash
python test_tool.py
```

成功后会生成 `施工现场安全检查表_测试.xlsx` 文件。

### 4. 使用 Dify CLI 部署

#### 方式一：开发模式（推荐用于调试）

```bash
# 在插件目录下
dify plugin dev
```

这会启动本地开发服务器，Dify 可以连接到本地插件进行测试。

#### 方式二：打包发布

```bash
# 打包插件
dify plugin package

# 上传到 Dify 平台
dify plugin publish
```

### 5. 在 Dify 中启用插件

1. 登录 Dify 平台
2. 进入"插件管理"页面
3. 找到"HSE安全检查表生成器"插件
4. 点击"启用"

## 在工作流中使用

### 创建工作流

1. 新建工作流
2. 添加"HSE安全检查表生成器"工具节点
3. 配置输入参数 `checklist_json`

### 参数配置示例

#### 方式一：直接输入 JSON

在 `checklist_json` 参数中粘贴 JSON 字符串：

```json
{
  "tableName": "施工现场安全检查表",
  "columns": ["序号", "检查内容", "检查方法", "参考依据", "分值"],
  "sections": [
    {
      "title": "一、安全管理",
      "items": [
        {
          "id": "1.1",
          "content": "施工单位应建立健全安全生产责任制度",
          "method": "查阅安全管理制度文件",
          "reference": "《建设工程安全生产管理条例》第21条",
          "score": "10"
        }
      ]
    }
  ]
}
```

#### 方式二：从上游节点获取

如果使用 LLM 生成 JSON：

1. 添加 LLM 节点
2. 提示词示例：
```
请根据以下要求生成安全检查表的 JSON 数据：
- 表名：{{table_name}}
- 检查项：{{check_items}}

输出格式：
{
  "tableName": "...",
  "columns": ["序号", "检查内容", "检查方法", "参考依据", "分值"],
  "sections": [...]
}
```
3. 将 LLM 输出连接到工具的 `checklist_json` 参数

### 获取生成的文件

工具执行成功后，会返回一个 Excel 文件。用户可以：
- 在工作流执行结果中直接下载
- 通过 Dify API 获取文件 blob

## 故障排查

### 问题 1: ModuleNotFoundError: No module named 'openpyxl'

**解决方案**:
```bash
pip install openpyxl>=3.1.0
```

### 问题 2: JSON 解析错误

**原因**: 输入的 JSON 格式不正确

**解决方案**:
1. 使用 JSON 验证工具检查格式
2. 确保所有字符串使用双引号
3. 检查是否有多余的逗号或缺少括号

### 问题 3: 生成的 Excel 文件无法下载

**可能原因**:
- Dify 版本不支持 blob 类型返回
- 文件大小超过限制

**解决方案**:
1. 检查 Dify 版本（需要 >= 0.4.0）
2. 减少检查项数量
3. 查看 Dify 日志获取详细错误信息

### 问题 4: Excel 格式不正确

**检查项**:
1. 确认 `columns` 数组不为空
2. 确认 `items` 中的字段与 `columns` 对应
3. 运行 `test_tool.py` 本地验证

## 性能优化建议

1. **大数据量处理**: 如果检查项超过 1000 条，建议分批生成
2. **并发控制**: 在 `main.py` 中可以调整 `MAX_REQUEST_TIMEOUT` 参数
3. **内存管理**: openpyxl 会将整个工作簿加载到内存，注意控制数据量

## 更新插件

修改代码后：

```bash
# 重新打包
dify plugin package

# 更新到 Dify
dify plugin publish --update
```

或在开发模式下，Dify 会自动检测文件变化并重新加载。

## 安全注意事项

1. **输入验证**: 插件已包含 JSON 解析异常处理
2. **文件大小限制**: 建议在工作流中限制输入数据大小
3. **权限控制**: 确保只有授权用户可以使用该插件

## 技术支持

如遇到问题，请提供：
1. Dify 版本号
2. 插件版本号
3. 完整的错误日志
4. 输入的 JSON 示例（脱敏后）

## 版本历史

- **v1.0.0** (2026-01-06)
  - 初始版本
  - 支持基本的 Excel 生成功能
  - 支持单元格合并和样式设置
  - 支持自动换行和边框

## 许可证

请参考项目根目录的 LICENSE 文件。
