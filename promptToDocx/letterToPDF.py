from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os
# Function to create a PDF document
def createPdf(uuid,letter_text):
    # Create a PDF document
    doc = SimpleDocTemplate(os.getcwd()+"/letters/"+str(uuid)+".pdf", pagesize=letter)

    # Create styles
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    heading_style = ParagraphStyle(
        'Heading1', parent=styles['Heading1'], spaceAfter=12
    )

    # Create content
    content = []

    # Add entire letter text with explicit line breaks
    letter_text_with_line_breaks = letter_text.replace('\n', '<br/>')
    letter_paragraph = Paragraph(letter_text_with_line_breaks, normal_style)
    content.append(letter_paragraph)

    # Build the PDF document
    doc.build(content)

    return str(uuid)




