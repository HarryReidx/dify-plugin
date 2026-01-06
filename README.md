# HSE 安全检查表生成插件

**Author:** ty-huangxin  
**Version:** 0.0.1  
**Type:** Dify Tool Plugin

## 📋 简介

HSE 安全检查表生成插件是一个 Dify 工具插件，用于将结构化的 JSON 数据转换为格式美观的 Excel 检查表文件。支持单元格合并、自定义样式、自动换行等高级功能，特别适用于生成 HSE（健康、安全、环境）安全检查表或任何结构化的检查清单。

## ✨ 主要特性

- 📊 **格式化 Excel 生成**：自动生成带样式的 Excel 文件
- 🎨 **丰富的样式支持**：表头、字段名、分组标题、数据行均有独特样式
- 🔗 **单元格合并**：自动合并表头和分组标题
- 📝 **自动换行**：长文本自动换行显示
- 🎯 **自定义列宽**：针对不同内容类型优化列宽
- 🛡️ **错误处理**：完善的 JSON 解析和验证机制
- 💾 **内存生成**：使用内存缓冲区，无需磁盘 I/O
- 📥 **直接下载**：在 Dify 界面直接下载生成的文件

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 本地测试

```bash
python test_tool.py
```

查看生成的 `施工现场安全检查表_测试.xlsx` 文件验证功能。

### 3. 部署到 Dify

```bash
# 开发模式
dify plugin dev

# 或打包发布
dify plugin package
dify plugin publish
```

### 4. 在 Dify 中使用

1. 在 Dify 平台启用"HSE安全检查表生成器"插件
2. 在工作流中添加该工具节点
3. 输入 JSON 数据到 `checklist_json` 参数
4. 运行工作流并下载生成的 Excel 文件

## 📖 文档

> 📑 **[完整文档索引](INDEX.md)** - 查看所有文档和快速导航

### 核心文档
- **[快速开始](QUICK_START.md)** - 一分钟上手指南
- **[使用说明](USAGE_CN.md)** - 详细的使用文档和示例
- **[部署指南](DEPLOYMENT.md)** - 部署步骤和故障排查

### 技术文档
- **[架构说明](ARCHITECTURE.md)** - 技术架构和设计文档
- **[格式预览](EXCEL_FORMAT_PREVIEW.md)** - Excel 输出格式说明
- **[实现总结](IMPLEMENTATION_SUMMARY.md)** - 英文实现总结
- **[实现清单](IMPLEMENTATION_CHECKLIST.md)** - 完整的功能清单

## 📝 输入格式

```json
{
  "tableName": "施工现场安全检查表",
  "columns": ["序号", "检查内容", "检查方式", "检查参考依据", "检查情况", "存在问题和建议", "得分"],
  "sections": [
    {
      "title": "一、安全管理",
      "items": [
        {
          "id": "1.1",
          "content": "施工单位应建立健全安全生产责任制度",
          "method": "查阅安全管理制度文件",
          "reference": "《建设工程安全生产管理条例》第21条",
          "situation": "",
          "suggestion": "",
          "score": "10"
        }
      ]
    }
  ]
}
```

完整示例请参考 [example_checklist.json](example_checklist.json)

## 📊 输出示例

生成的 Excel 文件包含：
- ✅ 合并的大标题行（16pt 宋体加粗）
- ✅ 格式化的表头行（10.5pt 宋体加粗，浅灰背景 #EAEAEA）
- ✅ 分组标题行（淡绿背景 #EBF1DE，加粗居中）
- ✅ 带边框的数据行（内边框细线，外边框中粗线）
- ✅ 自动换行的长文本
- ✅ 精确的列宽和行高设置
- ✅ 智能对齐（序号/检查情况/建议/得分居中，其他左对齐+缩进）

## 🛠️ 技术栈

- **Python 3.8+**
- **Dify Plugin SDK** (>=0.4.0)
- **openpyxl** (>=3.1.0) - Excel 文件处理

## 📦 项目结构

```
hse_safe_checklist/
├── tools/
│   ├── hse_safe_checklist.py      # 核心工具实现
│   └── hse_safe_checklist.yaml    # 工具配置
├── main.py                         # 插件入口
├── requirements.txt                # 依赖列表
├── example_checklist.json          # 示例数据
├── test_tool.py                    # 测试脚本
└── docs/                           # 文档目录
    ├── USAGE_CN.md
    ├── DEPLOYMENT.md
    ├── QUICK_START.md
    └── ARCHITECTURE.md
```

## 🧪 测试

运行测试脚本验证功能：

```bash
python test_tool.py
```

测试结果：
- ✅ JSON 解析正常
- ✅ Excel 生成成功
- ✅ 样式应用正确
- ✅ 单元格合并正常
- ✅ 边框显示正确

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

请参考 LICENSE 文件。

## 📧 联系方式

**Author:** ty-huangxin

---

**注意**：本插件需要 Dify 平台支持（版本 >= 0.4.0）



