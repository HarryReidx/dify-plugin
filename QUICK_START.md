# 快速开始指南 - HSE 安全检查表生成插件

## 一分钟上手

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 测试功能
```bash
python test_tool.py
```
查看生成的 `施工现场安全检查表_测试.xlsx` 文件

### 3. 部署到 Dify
```bash
dify plugin dev
```

## 最小可用示例

### 输入 JSON
```json
{
  "tableName": "我的检查表",
  "columns": ["序号", "内容"],
  "sections": [
    {
      "title": "第一部分",
      "items": [
        {"id": "1", "content": "检查项1"}
      ]
    }
  ]
}
```

### 输出
生成文件：`我的检查表_检查表.xlsx`

## 完整示例

参考 `example_checklist.json` 文件，包含：
- 表名
- 5个列（序号、检查内容、检查方法、参考依据、分值）
- 3个分组
- 5个检查项

## 在 Dify 中使用

1. **添加工具节点**: "HSE安全检查表生成器"
2. **输入参数**: 将 JSON 字符串传入 `checklist_json`
3. **运行**: 执行工作流
4. **下载**: 获取生成的 Excel 文件

## 常见问题

**Q: JSON 格式错误怎么办？**
A: 使用在线 JSON 验证工具检查格式，确保使用双引号。

**Q: 如何自定义列？**
A: 修改 `columns` 数组，`items` 中的字段会按顺序填充。

**Q: 支持多少检查项？**
A: 建议不超过 1000 项，以保证性能。

**Q: 如何修改样式？**
A: 编辑 `tools/hse_safe_checklist.py` 中的样式定义。

## 文件说明

| 文件 | 说明 |
|------|------|
| `tools/hse_safe_checklist.py` | 核心实现代码 |
| `tools/hse_safe_checklist.yaml` | 工具配置 |
| `example_checklist.json` | 示例数据 |
| `test_tool.py` | 本地测试脚本 |
| `USAGE_CN.md` | 详细使用文档 |
| `DEPLOYMENT.md` | 部署指南 |

## 技术支持

遇到问题？检查：
1. Python 版本 >= 3.8
2. openpyxl 已安装
3. JSON 格式正确
4. Dify 版本 >= 0.4.0

详细文档请查看 `USAGE_CN.md` 和 `DEPLOYMENT.md`。
