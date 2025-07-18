import tempfile
from fpdf import FPDF
import os

class PDFWithFooter(FPDF):
    def footer(self):
        # Set position of the footer at 15 units from bottom
        self.set_y(-20)
        # Add Philips logo (assumed to be in the same directory as this script)
        logo_path = os.path.join(os.path.dirname(__file__), 'philips_logo.png')
        if os.path.exists(logo_path):
            # Center the logo horizontally
            page_width = self.w - 2 * self.l_margin
            logo_width = 30
            x_center = (self.w - logo_width) / 2
            self.image(logo_path, x=x_center, y=self.get_y(), w=logo_width, h=10)

def draw_table_row(pdf, col_widths, row_data, alignments, font_style=None, wrap_col_idx=None):
    # Robust fix: never split a row across pages
    line_height = 8
    y_start = pdf.get_y()
    x_start = pdf.get_x()
    n_cols = len(col_widths)

    if wrap_col_idx is not None:
        # Calculate the number of lines for the wrapped cell
        wrap_width = col_widths[wrap_col_idx]
        wrap_lines = pdf.multi_cell(wrap_width, line_height, row_data[wrap_col_idx], border=0, align=alignments[wrap_col_idx], split_only=True)
        n_lines = len(wrap_lines)
        max_height = n_lines * line_height
    else:
        max_height = line_height

    # Robust: If the row won't fit, add a new page before drawing
    if pdf.get_y() + max_height > pdf.page_break_trigger:
        pdf.add_page()
        y_start = pdf.get_y()
        x_start = pdf.get_x()

    # Draw each cell
    x = x_start
    for i in range(n_cols):
        pdf.set_xy(x, y_start)
        if wrap_col_idx is not None and i == wrap_col_idx:
            # Draw border rectangle for the wrapped cell
            pdf.rect(x, y_start, col_widths[i], max_height)
            pdf.multi_cell(col_widths[i], line_height, row_data[i], border=0, align=alignments[i])
            x += col_widths[i]
            pdf.set_xy(x, y_start)
        else:
            pdf.cell(col_widths[i], max_height, row_data[i], border=1, align=alignments[i])
            x += col_widths[i]
    pdf.set_y(y_start + max_height)

async def export_to_pdf(frs_data):
    """
    Export the FRS data to a professional, readable PDF with tables and Philips logo at the bottom of each page.
    Returns the path to the generated PDF file.
    """
    pdf = PDFWithFooter()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 10, txt="Functional Requirements Specification", ln=True, align='C')
    pdf.ln(10)

    for section in frs_data.get("sections", []):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, txt=section["title"], ln=True)
        pdf.set_font("Arial", 'B', 11)
        col_widths = [45, 100, 45]
        alignments = ['C', 'L', 'C']
        draw_table_row(pdf, col_widths, ["FRS Identifier", "Requirement Description", "URS Identifier"], alignments, wrap_col_idx=1)
        pdf.set_font("Arial", size=11)
        for item in section.get("items", []):
            draw_table_row(pdf, col_widths, [item['id'], item['description'], item['source']], alignments, wrap_col_idx=1)
        pdf.ln(5)

    # Revision History Table (example static data)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, txt="Revision History", ln=True)
    pdf.set_font("Arial", 'B', 11)
    rev_col_widths = [25, 45, 80, 40]  # sum = 190
    alignments = ['C', 'C', 'C', 'C']
    draw_table_row(pdf, rev_col_widths, ["Rev.", "Author", "Description of Change", "Reason for Change"], alignments, wrap_col_idx=None)
    pdf.set_font("Arial", size=11)
    draw_table_row(pdf, rev_col_widths, ["1.0", "Alex Lee", "Initial draft", "Project start"], alignments, wrap_col_idx=None)
    draw_table_row(pdf, rev_col_widths, ["1.1", "Priya Patel", "Added regulatory and reporting requirements", "Compliance update"], alignments, wrap_col_idx=None)

    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_pdf.name)
    return temp_pdf.name
