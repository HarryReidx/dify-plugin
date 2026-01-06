# HSE 安全检查表生成插件 - 文档索引

## 📚 文档导航

### 🚀 快速入门

1. **[README.md](README.md)** - 项目主页
   - 项目简介和特性
   - 快速开始步骤
   - 基本使用说明

2. **[QUICK_START.md](QUICK_START.md)** - 快速开始指南
   - 一分钟上手
   - 最小可用示例
   - 常见问题解答

### 📖 详细文档

3. **[USAGE_CN.md](USAGE_CN.md)** - 使用说明（中文）
   - 完整的功能说明
   - 详细的参数说明
   - 使用示例和最佳实践
   - 错误处理说明

4. **[DEPLOYMENT.md](DEPLOYMENT.md)** - 部署指南
   - 环境要求
   - 安装步骤
   - 部署方式（开发模式/生产模式）
   - 故障排查指南
   - 性能优化建议

### 🏗️ 技术文档

5. **[ARCHITECTURE.md](ARCHITECTURE.md)** - 架构说明
   - 数据流程图
   - 组件说明
   - 样式系统
   - 性能特性
   - 扩展点说明

6. **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - 实现总结（英文）
   - 实现概述
   - 技术栈
   - 代码质量
   - 测试结果

7. **[IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md)** - 实现清单
   - 功能完成情况
   - 需求对照表
   - 测试验证结果
   - 交付物清单

### 🎨 格式说明

8. **[EXCEL_FORMAT_PREVIEW.md](EXCEL_FORMAT_PREVIEW.md)** - Excel 格式预览
   - 视觉布局示例
   - 样式详细说明
   - 颜色方案
   - 边框和换行效果

9. **[STYLE_SPECIFICATION.md](STYLE_SPECIFICATION.md)** - 样式规范说明
   - 最新样式要求
   - 行高和列宽设定
   - 字体和对齐方式
   - JSON字段映射

10. **[UPDATE_NOTES.md](UPDATE_NOTES.md)** - 更新说明
    - 版本变更记录
    - 样式升级详情
    - 兼容性说明
    - 迁移指南

### 📝 示例文件

9. **[example_checklist.json](example_checklist.json)** - 示例数据
   - 完整的 JSON 输入示例
   - 包含 3 个分组
   - 包含 5 个检查项
   - 可直接用于测试

10. **[test_tool.py](test_tool.py)** - 测试脚本
    - 本地测试工具
    - 验证 Excel 生成逻辑
    - 无需 Dify 环境

11. **[DIFY_WORKFLOW_GUIDE.md](DIFY_WORKFLOW_GUIDE.md)** - Dify 工作流配置指南
    - 参数配置说明
    - 常见错误解决
    - 调试步骤
    - 工作流示例

### 🔧 核心代码

11. **[tools/hse_safe_checklist.py](tools/hse_safe_checklist.py)** - 工具实现
    - 核心业务逻辑
    - Excel 生成代码
    - 错误处理

12. **[tools/hse_safe_checklist.yaml](tools/hse_safe_checklist.yaml)** - 工具配置
    - 参数定义
    - 多语言标签
    - 工具描述

13. **[main.py](main.py)** - 插件入口
    - Dify 插件初始化
    - 插件运行入口

14. **[requirements.txt](requirements.txt)** - 依赖列表
    - Python 包依赖
    - 版本要求

## 📋 按用途分类

### 新手入门
1. [README.md](README.md) - 了解项目
2. [QUICK_START.md](QUICK_START.md) - 快速上手
3. [example_checklist.json](example_checklist.json) - 查看示例
4. [test_tool.py](test_tool.py) - 本地测试

### 使用指南
1. [USAGE_CN.md](USAGE_CN.md) - 详细使用说明
2. [EXCEL_FORMAT_PREVIEW.md](EXCEL_FORMAT_PREVIEW.md) - 了解输出格式
3. [example_checklist.json](example_checklist.json) - 参考示例

### 部署运维
1. [DEPLOYMENT.md](DEPLOYMENT.md) - 部署步骤
2. [requirements.txt](requirements.txt) - 安装依赖
3. [QUICK_START.md](QUICK_START.md) - 快速部署

### 开发维护
1. [ARCHITECTURE.md](ARCHITECTURE.md) - 理解架构
2. [tools/hse_safe_checklist.py](tools/hse_safe_checklist.py) - 修改代码
3. [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - 了解实现
4. [test_tool.py](test_tool.py) - 测试验证

### 项目管理
1. [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md) - 功能清单
2. [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - 项目总结
3. [README.md](README.md) - 项目概览

## 🎯 常见任务指引

### 任务 1: 第一次使用插件
```
1. 阅读 README.md 了解项目
2. 按照 QUICK_START.md 快速开始
3. 运行 test_tool.py 本地测试
4. 查看 USAGE_CN.md 学习详细用法
```

### 任务 2: 部署到 Dify
```
1. 查看 DEPLOYMENT.md 了解部署步骤
2. 安装 requirements.txt 中的依赖
3. 使用 Dify CLI 部署插件
4. 参考 USAGE_CN.md 在工作流中使用
```

### 任务 3: 自定义样式
```
1. 阅读 ARCHITECTURE.md 了解样式系统
2. 查看 EXCEL_FORMAT_PREVIEW.md 了解当前格式
3. 修改 tools/hse_safe_checklist.py 中的样式定义
4. 运行 test_tool.py 验证修改
```

### 任务 4: 排查问题
```
1. 查看 DEPLOYMENT.md 的故障排查部分
2. 检查 requirements.txt 依赖是否安装
3. 运行 test_tool.py 本地测试
4. 查看 USAGE_CN.md 的错误处理说明
```

### 任务 5: 理解实现
```
1. 阅读 IMPLEMENTATION_SUMMARY.md 了解概览
2. 查看 ARCHITECTURE.md 理解架构
3. 阅读 tools/hse_safe_checklist.py 源代码
4. 参考 IMPLEMENTATION_CHECKLIST.md 查看功能清单
```

## 📊 文档统计

| 类型 | 数量 | 文件 |
|------|------|------|
| 说明文档 | 8 | README, USAGE_CN, DEPLOYMENT, QUICK_START, ARCHITECTURE, IMPLEMENTATION_SUMMARY, IMPLEMENTATION_CHECKLIST, EXCEL_FORMAT_PREVIEW |
| 代码文件 | 4 | main.py, tools/hse_safe_checklist.py, tools/hse_safe_checklist.yaml, requirements.txt |
| 示例文件 | 2 | example_checklist.json, test_tool.py |
| 索引文件 | 1 | INDEX.md (本文件) |
| **总计** | **15** | |

## 🔍 文档搜索

### 按关键词查找

- **安装**: DEPLOYMENT.md, QUICK_START.md, requirements.txt
- **使用**: USAGE_CN.md, QUICK_START.md, README.md
- **样式**: EXCEL_FORMAT_PREVIEW.md, ARCHITECTURE.md
- **错误**: USAGE_CN.md, DEPLOYMENT.md
- **测试**: test_tool.py, IMPLEMENTATION_CHECKLIST.md
- **架构**: ARCHITECTURE.md, IMPLEMENTATION_SUMMARY.md
- **示例**: example_checklist.json, USAGE_CN.md
- **部署**: DEPLOYMENT.md, QUICK_START.md
- **配置**: tools/hse_safe_checklist.yaml, DEPLOYMENT.md
- **性能**: ARCHITECTURE.md, DEPLOYMENT.md

## 📱 快速链接

### 核心文档（必读）
- [README.md](README.md) - 项目主页
- [QUICK_START.md](QUICK_START.md) - 快速开始
- [USAGE_CN.md](USAGE_CN.md) - 使用说明

### 参考文档
- [DEPLOYMENT.md](DEPLOYMENT.md) - 部署指南
- [ARCHITECTURE.md](ARCHITECTURE.md) - 架构说明
- [EXCEL_FORMAT_PREVIEW.md](EXCEL_FORMAT_PREVIEW.md) - 格式预览

### 开发文档
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - 实现总结
- [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md) - 功能清单
- [tools/hse_safe_checklist.py](tools/hse_safe_checklist.py) - 源代码

## 🆘 获取帮助

1. **使用问题**: 查看 [USAGE_CN.md](USAGE_CN.md) 和 [QUICK_START.md](QUICK_START.md)
2. **部署问题**: 查看 [DEPLOYMENT.md](DEPLOYMENT.md) 的故障排查部分
3. **格式问题**: 查看 [EXCEL_FORMAT_PREVIEW.md](EXCEL_FORMAT_PREVIEW.md)
4. **技术问题**: 查看 [ARCHITECTURE.md](ARCHITECTURE.md) 和源代码

## 📝 文档维护

### 文档版本
- 创建日期: 2026-01-06
- 最后更新: 2026-01-06
- 版本: 1.0.0

### 更新记录
- 2026-01-06: 初始版本，创建完整文档体系

---

**提示**: 建议按照"新手入门"部分的顺序阅读文档，可以快速掌握插件的使用方法。
