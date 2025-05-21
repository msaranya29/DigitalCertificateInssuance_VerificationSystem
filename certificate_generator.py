from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os
from datetime import datetime

def generate_certificate(cert_data):
    """
    Generate a PDF certificate using provided certificate data
    
    Args:
        cert_data: Tuple containing certificate data (cert_id, name, course, issue_date)
    
    Returns:
        String: Path to the generated certificate file
    """
    # Extract certificate data
    cert_id, name, course, issue_date = cert_data
    
    # Create directory for certificates if it doesn't exist
    cert_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'certificates')
    os.makedirs(cert_directory, exist_ok=True)
    
    # Set the filename
    filename = f"certificate_{cert_id}.pdf"
    filepath = os.path.join(cert_directory, filename)
    
    # Create PDF
    c = canvas.Canvas(filepath, pagesize=landscape(letter))
    width, height = landscape(letter)
    
    # Add decorative border
    c.setStrokeColor(HexColor('#4682B4'))  # Steel Blue
    c.setLineWidth(3)
    c.rect(0.5*inch, 0.5*inch, width-inch, height-inch)
    
    # Add fancy inner border
    c.setStrokeColor(HexColor('#1E3F66'))  # Darker Blue
    c.setLineWidth(1)
    c.rect(0.75*inch, 0.75*inch, width-1.5*inch, height-1.5*inch)
    
    # Add certificate title
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(HexColor('#1E3F66'))
    c.drawCentredString(width/2, height-2*inch, "CERTIFICATE OF COMPLETION")
    
    # Add the organization name
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(HexColor('#4682B4'))
    c.drawCentredString(width/2, height-2.7*inch, "Your Organization Name")
    
    # Add certificate text
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor('#333333'))
    c.drawCentredString(width/2, height-3.5*inch, "This is to certify that")
    
    # Add recipient name
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(HexColor('#000000'))
    c.drawCentredString(width/2, height-4.2*inch, name)
    
    # Add course information
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor('#333333'))
    c.drawCentredString(width/2, height-4.9*inch, f"has successfully completed the course")
    
    # Add course name
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor('#1E3F66'))
    c.drawCentredString(width/2, height-5.5*inch, course)
    
    # Add date
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor('#333333'))
    c.drawString(1.2*inch, 1.2*inch, f"Date: {issue_date}")
    
    # Add certificate ID
    c.setFont("Helvetica", 10)
    c.drawString(width-3*inch, 1.2*inch, f"Certificate ID: {cert_id}")
    
    # Save the PDF
    c.save()
    
    return filename