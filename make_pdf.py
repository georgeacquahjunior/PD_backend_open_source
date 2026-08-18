from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

output = "python-beginners-guide.pdf"

content = []
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleStyle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=20, leading=24, spaceAfter=12, textColor=colors.HexColor('#1f4e79')))
styles.add(ParagraphStyle(name='HeadingStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, leading=18, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor('#2f5d7c')))
styles.add(ParagraphStyle(name='BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='CodeStyle', parent=styles['Code'], fontName='Courier', fontSize=10, leading=12, textColor=colors.HexColor('#1b1b1b'), backColor=colors.HexColor('#f5f5f5'), borderPadding=6, spaceAfter=6))

content.append(Paragraph("Python for Beginners", styles['TitleStyle']))
content.append(Paragraph("A simple guide to learning Python step by step.", styles['BodyStyle']))
content.append(Spacer(1, 12))

sections = [
    ("1. What is programming?", "Programming means giving instructions to a computer. A program is a set of steps the computer follows in order. Example: <font face='Courier'>print(\"Hello, world!\")</font>"),
    ("2. Variables", "Variables store information. You can think of them as labeled boxes that hold data. Example: <font face='Courier'>name = \"Ada\"</font>"),
    ("3. Input and output", "Use <font face='Courier'>print()</font> to show output and <font face='Courier'>input()</font> to ask the user for information."),
    ("4. Numbers and math", "Python can work with numbers using +, -, *, and /. Example: <font face='Courier'>subtotal = price * quantity</font>"),
    ("5. Decisions with if", "The <font face='Courier'>if</font> statement lets your program make decisions. It can choose one path or another."),
    ("6. Repeating with loops", "Loops let you repeat code. Example: <font face='Courier'>for i in range(3): print(\"Hello\")</font>"),
    ("7. Functions", "Functions let you organize code into reusable blocks. They help keep programs clear and simple."),
    ("8. Understanding your receipt generator", "Your receipt program uses input, variables, loops, and math to calculate totals and tax."),
    ("9. Small practice exercise", "Try this example: <font face='Courier'>name = input(\"What is your name? \")\nage = int(input(\"How old are you? \") )</font>"),
    ("10. Suggested learning order", "Start with variables, input and output, numbers, if statements, loops, and functions."),
]

for heading, body in sections:
    content.append(Paragraph(heading, styles['HeadingStyle']))
    content.append(Paragraph(body, styles['BodyStyle']))
    content.append(Spacer(1, 6))

content.append(Paragraph("Final advice", styles['HeadingStyle']))
content.append(Paragraph("The best way to learn Python is to write small programs, test them often, and fix errors one at a time.", styles['BodyStyle']))

pdf = SimpleDocTemplate(output, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
pdf.build(content)
print(f"Created {output}")
