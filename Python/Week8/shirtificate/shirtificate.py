from fpdf import FPDF


name = input("Enter your name: ")
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()


pdf.set_font("Helvetica", "B", size=40)
pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


pdf.image("shirtificate.png", x="C", y=60, w=160)


pdf.set_font("Helvetica", "B", size=28)
pdf.set_text_color(255, 255, 255)   
pdf.set_y(120)
pdf.cell(0, 10, f"{name} took CS50", align="C")


pdf.output("shirtificate.pdf")
