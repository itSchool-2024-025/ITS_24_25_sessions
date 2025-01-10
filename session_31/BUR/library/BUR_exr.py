from docx import Document
from docx.shared import Pt

class CertificateBuilder:
    def __init__(self, word_input_filepath):
        self.word_input_filepath = word_input_filepath
        self.doc_object = None
        self.list_of_paragraphs = []

    def open_docx(self):
        """
        Open the document template
        :return:
        True - doc template returned OK
        False - something went wrong
        """
        try:
            self.doc_object = Document(self.word_input_filepath)
            self.list_of_paragraphs = self.doc_object.paragraphs
            if self.doc_object:
                print("Docx Template opened OK")
                return True
            else:
                print("Docx Template not opened!")
                return False
        except Exception as e:
            print("func call - WordBuilder::open_docx()")
            print(f"An error occurred: {e}")

    def modify_doc_paragraphs(self):
        for parag in self.list_of_paragraphs:
            print(parag.text)

    def save_as_new_certificate(self, new_cert_filepath):
        pass

if __name__ == "__main__":
    certificate = CertificateBuilder("C:/Users/Danny/Documents/IT School/2024_2025/PythonProjects/BUR/cert_template/certif_template.docx")
    certificate.open_docx()
    certificate.modify_doc_paragraphs()