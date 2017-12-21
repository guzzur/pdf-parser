import tabula


class PdfParser:
    def __init__(self):
        self._pdf_path = ""
        self._csv_path = ""

    def _read_file(self, path):
        self._pdf_path = path
        print "Reading PDF: " + self._pdf_path

        tabula_pdf = tabula.read_pdf(self._pdf_path)
        tabula.convert_into(self._pdf_path, self._csv_path, "csv")

        print "Done reading"

    def dump_pdf_to_csv(self, pdf_path, csv_path):
        self._csv_path = csv_path
        self._read_file(pdf_path)
        print "Dumping into CSV: " + self._csv_path

        # Add here all dumping stuff

        print "Done dumping"


pdf = r"C:\Temp\Family_File3.pdf"
csv = r"C:\Temp\Family_File3.csv"

parser = PdfParser()
parser.dump_pdf_to_csv(pdf, csv)
