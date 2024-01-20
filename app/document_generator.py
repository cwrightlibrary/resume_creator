from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH

class Resume:
    def __init__(self):
        # Create blank document
        self.document = Document()
        
        # Adjust the Styles
        _style_h1_name = self.document.styles["Title"]
        _style_h1_name.font.name = "Lexend Tera Thin"
        
