from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 15, 50, 180)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=24)
        # Moving cursor to the right:
        # Setting text color to white:
        self.set_text_color(255)
        # self.cell(80)
        # Printing title:
        # self.cell(30, 180, "Harry Potter took CS50", align="C")
        # Performing a line break:
        self.ln(0)


# Instantiation of inherited class
name = input("Name: ")
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.header()
pdf.cell(80)
pdf.cell(30, 180, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")