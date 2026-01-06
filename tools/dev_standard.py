from collections.abc import Generator
from typing import Any
import json
import io

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
except ImportError:
    raise ImportError("openpyxl is required. Please install it via: pip install openpyxl")


class HseSafeChecklistTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        生成 HSE 安全检查表 Excel 文件
        """
        try:
            # 调试信息：显示接收到的所有参数
            # yield self.create_text_message(f"调试信息 - 接收到的参数: {list(tool_parameters.keys())}")

            # 获取输入参数
            checklist_json_str = tool_parameters.get("checklist_json", "")

            # 更详细的错误信息
            if not checklist_json_str:
                available_keys = list(tool_parameters.keys())
                yield self.create_text_message(
                    f"错误：未提供 checklist_json 参数\n"
                    f"接收到的参数键: {available_keys}\n"
                    f"参数值: {tool_parameters}\n\n"
                    f"请确保在 Dify 工作流中正确连接了 checklist_json 参数。"
                )
                return

            # 解析 JSON
            try:
                checklist_data = json.loads(checklist_json_str)
            except json.JSONDecodeError as e:
                yield self.create_text_message(f"JSON 解析错误：{str(e)}")
                return

            # 提取数据
            table_name = checklist_data.get("tableName", "检查表")
            columns = checklist_data.get("columns", [])
            sections = checklist_data.get("sections", [])

            if not columns:
                yield self.create_text_message("错误：columns 字段为空")
                return

            # 创建 Excel 工作簿
            wb = Workbook()
            ws = wb.active
            ws.title = "检查表"

            # 定义字体（全文使用宋体，大标题使用黑体）
            title_font = Font(name="黑体", bold=True, size=16)
            header_font = Font(name="宋体", bold=True, size=10.5)
            section_font = Font(name="宋体", bold=True, size=10.5)
            data_font = Font(name="宋体", size=10.5)

            # 定义填充色
            header_fill = PatternFill(start_color="EAEAEA", end_color="EAEAEA", fill_type="solid")
            section_fill = PatternFill(start_color="EBF1DE", end_color="EBF1DE", fill_type="solid")

            # 定义对齐方式
            title_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            section_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

            # 数据行对齐（序号、检查情况、备注列居中，其他左对齐）
            center_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            left_indent_alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

            # 定义边框
            thin_border = Border(
                left=Side(style='thin', color='000000'),
                right=Side(style='thin', color='000000'),
                top=Side(style='thin', color='000000'),
                bottom=Side(style='thin', color='000000')
            )

            medium_border = Border(
                left=Side(style='medium', color='000000'),
                right=Side(style='medium', color='000000'),
                top=Side(style='medium', color='000000'),
                bottom=Side(style='medium', color='000000')
            )

            # 设置列宽（按照新要求）
            ws.column_dimensions['A'].width = 7      # 序号
            ws.column_dimensions['B'].width = 50     # 检查内容
            ws.column_dimensions['C'].width = 50     # 检查方式
            ws.column_dimensions['D'].width = 30     # 检查参考依据
            ws.column_dimensions['E'].width = 26     # 检查情况
            ws.column_dimensions['F'].width = 26     # 存在问题和建议
            ws.column_dimensions['G'].width = 5    # 得分

            current_row = 1

            # 1. 写入大标题（表名）- 第1行
            # 合并 A1:G1（假设最多7列，如果columns更多需要动态调整）
            max_col = max(7, len(columns))  # 至少7列或columns的长度
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=max_col)
            cell = ws.cell(row=current_row, column=1, value=table_name)
            cell.font = title_font
            cell.alignment = title_alignment
            cell.border = thin_border
            ws.row_dimensions[current_row].height = 24  # 设置行高为24
            current_row += 1

            # 2. 写入表头（字段名）- 第2行
            for col_idx, col_name in enumerate(columns, start=1):
                cell = ws.cell(row=current_row, column=col_idx, value=col_name)
                cell.font = header_font
                cell.fill = header_fill
                cell.alignment = header_alignment
                cell.border = thin_border
            ws.row_dimensions[current_row].height = 30  # 设置行高为30
            current_row += 1

            # 3. 写入 sections 和 items
            for section in sections:
                section_title = section.get("title", "")
                items = section.get("items", [])

                # 写入 section 标题行（title行）
                if section_title:
                    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=max_col)
                    cell = ws.cell(row=current_row, column=1, value=section_title)
                    cell.font = section_font
                    cell.fill = section_fill
                    cell.alignment = section_alignment  # 加粗、水平及垂直居中
                    cell.border = thin_border
                    ws.row_dimensions[current_row].height = 23  # 设置行高为23
                    current_row += 1

                # 写入 items 数据行
                for item in items:
                    item_id = item.get("id", "")
                    content = item.get("content", "")
                    method = item.get("method", "")
                    reference = item.get("reference", "")
                    situation = item.get("situation", "")
                    suggestion = item.get("suggestion", "")
                    score = item.get("score", "")

                    # 根据 columns 的数量动态填充
                    # 假设标准列顺序：序号、检查内容、检查方式、检查参考依据、检查情况、存在问题和建议、得分
                    row_data = []
                    if len(columns) >= 1:
                        row_data.append(item_id)
                    if len(columns) >= 2:
                        row_data.append(content)
                    if len(columns) >= 3:
                        row_data.append(method)
                    if len(columns) >= 4:
                        row_data.append(reference)
                    if len(columns) >= 5:
                        row_data.append(situation)
                    if len(columns) >= 6:
                        row_data.append(suggestion)
                    if len(columns) >= 7:
                        row_data.append(score)

                    # 填充剩余列（如果有）
                    while len(row_data) < len(columns):
                        row_data.append("")

                    # 填充单元格并设置样式
                    for col_idx, value in enumerate(row_data, start=1):
                        cell = ws.cell(row=current_row, column=col_idx, value=value)
                        cell.font = data_font
                        cell.border = thin_border

                        # 根据列位置设置对齐方式
                        # A列(序号)、E列(检查情况)、F列(备注)、G列(得分) 居中
                        # B列(检查内容)、C列(检查方式)、D列(依据) 左对齐+缩进
                        if col_idx in [1, 5, 6, 7]:  # A, E, F, G列
                            cell.alignment = center_alignment
                        else:  # B, C, D列
                            cell.alignment = left_indent_alignment

                    # 数据行不设置固定高度，让Excel自动根据内容调整
                    # 移除固定行高设置，实现自适应

                    current_row += 1

            # 4. 为整个表格区域添加中粗外边框
            # 确定表格范围：从A1到最后一行的最后一列
            last_row = current_row - 1
            last_col = max_col

            # 设置外边框（顶部、底部、左侧、右侧）
            for row in range(1, last_row + 1):
                for col in range(1, last_col + 1):
                    cell = ws.cell(row=row, column=col)

                    # 保留原有的细边框，只修改外边框为中粗
                    left_style = 'medium' if col == 1 else 'thin'
                    right_style = 'medium' if col == last_col else 'thin'
                    top_style = 'medium' if row == 1 else 'thin'
                    bottom_style = 'medium' if row == last_row else 'thin'

                    cell.border = Border(
                        left=Side(style=left_style, color='000000'),
                        right=Side(style=right_style, color='000000'),
                        top=Side(style=top_style, color='000000'),
                        bottom=Side(style=bottom_style, color='000000')
                    )

            # 保存到内存
            excel_buffer = io.BytesIO()
            wb.save(excel_buffer)
            excel_buffer.seek(0)

            # 生成文件名
            filename = f"{table_name}_检查表.xlsx"

            # 返回文件
            yield self.create_blob_message(
                blob=excel_buffer.read(),
                meta={
                    "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "filename": filename
                }
            )

        except Exception as e:
            yield self.create_text_message(f"生成 Excel 时发生错误：{str(e)}")
