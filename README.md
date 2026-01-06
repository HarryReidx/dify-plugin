# TY 检查表生成插件

**Author:** ty-huangxin  
**Version:** 0.0.1  
**Type:** Dify Tool Plugin

## 📋 简介

TY 检查表生成插件是一个 Dify 工具插件集合，用于将结构化的 JSON 数据转换为格式美观的 Excel 检查表文件。支持单元格合并、自定义样式、自动换行等高级功能。

## 🛠️ 包含工具

### 1. 研发规范检查表生成器 (dev_standard)
生成研发规范检查表，适用于代码规范检查、开发流程审核、技术标准评估等。

### 2. HSE安全管理检查表生成器 (hse_safe)
生成HSE（健康、安全、环境）安全管理检查表，适用于施工现场安全检查、环保评估等。

## ✨ 主要特性

- 📊 **格式化 Excel 生成**：自动生成带样式的 Excel 文件
- 🎨 **专业样式**：黑体标题、宋体内容、精确行高和列宽
- 🔗 **单元格合并**：自动合并表头和分组标题
- 📝 **自动换行**：长文本自动换行显示
- 🎯 **智能对齐**：序号/情况/建议/得分居中，内容左对齐+缩进
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

### 3. 部署到 Dify
```bash
dify plugin dev
# 或
dify plugin publish
```

### 4. 在 Dify 中使用

1. 启用"TY检查表生成器"插件
2. 在工作流中添加工具节点：
   - **研发规范检查表生成器** (dev_standard)
   - **HSE安全管理检查表生成器** (hse_safe)
3. 输入 JSON 数据到 `checklist_json` 参数
4. 运行工作流并下载 Excel 文件

## 📝 输入格式

```json
{
  "tableName": "检查表名称",
  "columns": ["序号", "检查内容", "检查方式", "检查参考依据", "检查情况", "存在问题和建议", "得分"],
  "sections": [
    {
      "title": "分组标题",
      "items": [
        {
          "id": "1.1",
          "content": "检查内容",
          "method": "检查方式",
          "reference": "参考依据",
          "situation": "检查情况",
          "suggestion": "建议",
          "score": "10"
        }
      ]
    }
  ]
}
```

## 📊 Excel 格式

- **第1行**：大标题，黑体16pt，行高24，合并所有列
- **第2行**：表头，宋体10.5pt加粗，行高30，浅灰背景
- **Section行**：分组标题，宋体10.5pt加粗，淡绿背景，自适应高度
- **数据行**：宋体10.5pt，自适应高度，内边框细线，外边框中粗线
- **列宽**：A(6), B(15), C(50), D(26), E(26), F(26), G(4.5)

## 📦 项目结构

```
ty_checklist/
├── provider/
│   ├── ty_checklist.py              # Provider 实现
│   └── ty_checklist.yaml            # Provider 配置
├── tools/
│   ├── dev_standard.py              # 研发规范工具
│   ├── dev_standard.yaml            # 研发规范配置
│   ├── hse_safe.py                  # HSE安全工具
│   └── hse_safe.yaml                # HSE安全配置
├── main.py                           # 插件入口
├── manifest.yaml                     # 插件清单
├── requirements.txt                  # 依赖列表
├── example_checklist.json            # 示例数据
└── test_tool.py                      # 测试脚本
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

## 🛠️ 技术栈

- **Python 3.8+**
- **Dify Plugin SDK** (>=0.4.0)
- **openpyxl** (>=3.1.0) - Excel 文件处理

## 📄 许可证

请参考 LICENSE 文件。

## 📧 联系方式

**Author:** ty-huangxin

---

**注意**：本插件需要 Dify 平台支持（版本 >= 0.4.0）
