# HSE 安全检查表生成插件使用说明

## 功能概述

本插件用于将结构化的 JSON 数据转换为格式美观的 Excel 检查表文件，支持：
- 表头合并与样式设置
- 分组标题（Section）
- 自动换行
- 单元格边框
- 自定义列宽
- 文件下载

## 输入参数

### checklist_json (必填)

JSON 字符串，包含以下字段：

```json
{
  "tableName": "表格名称",
  "columns": ["列名1", "列名2", "列名3", ...],
  "sections": [
    {
      "title": "分组标题",
      "items": [
        {
          "id": "序号",
          "content": "检查内容",
          "method": "检查方式",
          "reference": "检查参考依据",
          "situation": "检查情况",
          "suggestion": "存在问题和建议",
          "score": "得分"
        }
      ]
    }
  ]
}
```

### 字段说明

- **tableName**: 检查表的总标题，会显示在第一行并合并所有列
- **columns**: 表头字段名数组，通常包含 ["序号", "检查内容", "检查方式", "检查参考依据", "检查情况", "存在问题和建议", "得分"]
- **sections**: 分组数组，每个分组包含：
  - **title**: 分组标题（如"一、安全管理"）
  - **items**: 该分组下的检查项数组，每项包含：
    - **id**: 序号（如 "1.1"）
    - **content**: 检查内容描述
    - **method**: 检查方式
    - **reference**: 检查参考依据
    - **situation**: 检查情况（可为空）
    - **suggestion**: 存在问题和建议（可为空）
    - **score**: 得分

## Excel 格式说明

生成的 Excel 文件具有以下格式特点：

### 1. 表头行（第1行）
- 显示 `tableName`
- 合并所有列
- 样式：居中对齐、加粗、灰色背景 (#D9D9D9)

### 2. 字段名行（第2行）
- 显示 `columns` 数组内容
- 样式：加粗、浅灰背景 (#F2F2F2)、居中对齐、细边框

### 3. Section 标题行
- 显示每个 section 的 `title`
- 合并所有列
- 样式：加粗、淡绿背景 (#EBF1DE)、左对齐、细边框

### 4. 数据行
- 填充 items 数据
- 所有单元格自动换行
- 所有单元格添加细边框
- 左对齐、垂直居中

### 5. 列宽设置
- 第1列（序号）：10
- 第2列（检查内容）：45
- 其他列：20

## 使用示例

### 在 Dify 工作流中使用

1. 添加"HSE安全检查表生成器"工具节点
2. 在 `checklist_json` 参数中输入 JSON 数据（可以从上游节点获取）
3. 运行工作流
4. 下载生成的 Excel 文件

### JSON 示例

参考项目根目录的 `example_checklist.json` 文件，包含完整的示例数据。

### 最小示例

```json
{
  "tableName": "简单检查表",
  "columns": ["序号", "内容"],
  "sections": [
    {
      "title": "第一部分",
      "items": [
        {
          "id": "1",
          "content": "检查项1"
        }
      ]
    }
  ]
}
```

## 错误处理

插件会处理以下错误情况：

1. **未提供参数**：返回错误提示"未提供 checklist_json 参数"
2. **JSON 解析失败**：返回具体的 JSON 解析错误信息
3. **columns 为空**：返回错误提示"columns 字段为空"
4. **其他异常**：返回详细的错误信息

## 输出

成功执行后，插件会返回一个 Excel 文件（.xlsx 格式），文件名格式为：`{tableName}_检查表.xlsx`

用户可以直接在 Dify 界面中下载该文件。

## 技术栈

- **openpyxl**: Excel 文件生成与样式设置
- **dify_plugin**: Dify 插件 SDK
- **Python 3.x**: 核心开发语言

## 安装依赖

```bash
pip install -r requirements.txt
```

## 开发与调试

1. 确保已安装 Dify CLI
2. 修改代码后，使用 Dify CLI 重新加载插件
3. 在 Dify 工作流中测试功能

## 注意事项

1. JSON 字符串必须是有效的 JSON 格式
2. `columns` 数组不能为空
3. `items` 中的字段会按照 `columns` 的顺序填充到 Excel 中
4. 如果 `items` 的字段少于 `columns` 的数量，剩余列会填充空字符串
5. 所有文本内容支持换行符 `\n`，会在 Excel 中正确显示

## 许可证

请参考项目根目录的 LICENSE 文件。
