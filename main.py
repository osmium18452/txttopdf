from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, headertxt=""):
        super().__init__()
        self.headertxt = headertxt

    def header(self):
        self.set_font("courier", "", 8)
        self.cell(0, 3, txt=self.headertxt, border="B", align="C")
        self.ln()

    def footer(self):
        self.set_y(-15)
        self.set_font('courier', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def print_file_bin(self, file):
        self.set_font('courier', '', 12)
        txt = file.decode("utf8")
        self.multi_cell(0, 7, txt=txt)


txt = 'Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World!'
pdf = PDF("header test")
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('courier', '', 12)
with open("main.py", "rb") as f:
    pdf.print_file_bin(f.read())
pdf.output("tuto2.pdf")


