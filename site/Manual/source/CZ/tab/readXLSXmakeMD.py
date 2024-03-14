from openpyxl import load_workbook
from markdown import markdown

def excel_to_markdown_table(file_path, sheet_name, range_start, range_end):
    # Load the Excel workbook
    wb = load_workbook(filename=file_path, data_only=True)

    # Select the specified sheet
    sheet = wb[sheet_name]

    # Initialize list to store table rows
    rows = []

    # Flag to track if bold formatting is needed
    make_bold = True

    # Iterate over the specified range of cells and extract data
    consecutive_blank_rows = 0  # Counter for consecutive blank rows
    for row_idx, row in enumerate(sheet[range_start:range_end], start=1):
        row_data = []
        row_is_blank = True  # Flag to track if current row is blank
        for cell_idx, cell in enumerate(row, start=1):
            # Skip empty cells
            if cell.value in (None, "None"):
                if cell_idx == 1:
                    make_bold = True
            else:
                row_data.append(cell.value)
                if make_bold:
                    row_data[0] = "**" + row_data[0] + "**"
                    make_bold = False  # Reset bold flag after making first cell bold
                row_is_blank = False  # Set row_is_blank to False if non-empty cell found
        if not row_is_blank:  # Append non-empty rows
            rows.append(row_data)
            consecutive_blank_rows = 0  # Reset consecutive_blank_rows counter
        else:
            consecutive_blank_rows += 1  # Increment consecutive_blank_rows counter
            if consecutive_blank_rows >= 2:  # Skip printing rows with two or more consecutive blank rows
                break

    # Convert data to Markdown table format
    markdown_table = ""
    for idx, row_data in enumerate(rows):
        if idx == 0:
            markdown_table += "| " + " | ".join(cell for cell in row_data) + " |\n"
            markdown_table += "| " + " | ".join(":---:" for _ in row_data) + " |\n"
        else:
            markdown_table += "| " + " | ".join(str(cell) for cell in row_data) + " |\n"

    return markdown_table
  
def save_markdown_table(markdown_table, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_table)

# TGZ-D-48-13_26
file_path = "parameters.xlsx"
sheet_name = "TGZ-D-48-13_26"
range_start = "A1"
range_end = "B100"
markdown_table = excel_to_markdown_table(file_path, sheet_name, range_start, range_end)
output_file = "../../../CZ/TGZ/TGZ-D-48-13/md/parameters.md"
save_markdown_table(markdown_table, output_file)

# TGZ-S-48-50_100
file_path = "parameters.xlsx"
sheet_name = "TGZ-S-48-50_100"
range_start = "A1"
range_end = "B100"
markdown_table = excel_to_markdown_table(file_path, sheet_name, range_start, range_end)
output_file = "../../../CZ/TGZ/TGZ-S-48-50_100/md/parameters.md"
save_markdown_table(markdown_table, output_file)

# TGZ-D-48-50_100
file_path = "parameters.xlsx"
sheet_name = "TGZ-D-48-50_100"
range_start = "A1"
range_end = "B100"
markdown_table = excel_to_markdown_table(file_path, sheet_name, range_start, range_end)
output_file = "../../../CZ/TGZ/TGZ-D-48-50_100/md/parameters.md"
save_markdown_table(markdown_table, output_file)