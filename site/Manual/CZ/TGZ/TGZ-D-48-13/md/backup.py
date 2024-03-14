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
    for row_idx, row in enumerate(sheet[range_start:range_end], start=1):
        row_data = []
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
        if row_data:  # Append non-empty rows
            rows.append(row_data)

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

# Example usage
file_path = "parameters.xlsx"
sheet_name = "TGZ-D-48-13_26"
range_start = "A1"
range_end = "B9"
markdown_table = excel_to_markdown_table(file_path, sheet_name, range_start, range_end)

# Specify output file path
output_file = "parameters.md"

# Save Markdown table to file
save_markdown_table(markdown_table, output_file)