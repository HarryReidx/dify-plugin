# 部署和迁移指南

## 部署步骤

### 1. 环境要求

- Python 3.8+
- Dify CLI 已安装
- Dify 平台版本 >= 0.4.0

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 本地测试

```bash
python test_tool.py
```

验证 Excel 生成功能正常。

### 4. 部署到 Dify

#### 开发模式（推荐用于调试）

```bash
dify plugin dev
```

#### 生产部署

```bash
dify plugin package
dify plugin publish
```

### 5. 在 Dify 中启用

1. 登录 Dify 平台
2. 进入"插件管理"页面
3. 找到"TY检查表生成器"插件
4. 点击"启用"

## 从旧版本迁移

如果您之前使用了 `hse_safe_checklist` 插件，按以下步骤迁移：

### 迁移步骤

1. **部署新插件**
   ```bash
    dify plugin package ./yourapp
   ```


### 兼容性说明

- ✅ JSON 格式完全兼容
- ✅ Excel 输出格式完全一致
- ✅ 所有样式参数保持不变
- ✅ 无需修改任何输入数据

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
3. 运行 `python test_tool.py` 本地验证

## 性能优化

### 大数据量处理

如果检查项超过 1000 条，建议分批生成：

```python
# 分批处理示例
batch_size = 500
for i in range(0, len(items), batch_size):
    batch_items = items[i:i+batch_size]
    # 生成 Excel
```

### 内存管理

- openpyxl 会将整个工作簿加载到内存
- 注意控制数据量，避免内存溢出
- 对于超大数据集，考虑使用流式处理

### 并发控制

在 `main.py` 中可以调整超时时间：

```python
plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=120))
```

## 更新和维护

### 更新插件

修改代码后：

```bash
# 重新打包
dify plugin package

# 更新到 Dify
dify plugin publish --update
```

或在开发模式下，Dify 会自动检测文件变化并重新加载。

### 版本管理

- 使用语义化版本号（MAJOR.MINOR.PATCH）
- 在 `manifest.yaml` 中更新版本号
- 保持更新日志

## 安全注意事项

1. **输入验证**: 插件已包含 JSON 解析异常处理
2. **文件大小限制**: 建议在工作流中限制输入数据大小
3. **权限控制**: 确保只有授权用户可以使用该插件
4. **数据隐私**: 生成的 Excel 文件不会被保存到服务器

## 技术支持

遇到问题时，请提供：
1. Dify 版本号
2. 插件版本号
3. 完整的错误日志
4. 输入的 JSON 示例（脱敏后）

## 回滚方案

如果遇到问题需要回滚：

1. 保留旧版本的代码备份
2. 在 Dify 中重新启用旧插件
3. 恢复工作流中的旧工具节点

## 许可证

请参考项目根目录的 LICENSE 文件。
