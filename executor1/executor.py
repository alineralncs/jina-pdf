from jina import Executor, requests, Document, DocumentArray
from docarray import DocList
import PyPDF2
import spacy
# from ..models import PDFDocument
# from models import PDFDocument
nlp = spacy.load("pt_core_news_sm")



class PDFTextPreprocessor(Executor):
    @requests
    def process(self, docs: DocumentArray, **kwargs) -> DocList[Document]:
        for doc in docs:
            doc = self._get_text_from_pdf(doc.uri)
            # fazer processamento de texto
            doc = self.preprocess(doc)
            return doc

    def _get_text_from_pdf(self, pdf_path: str) -> str:
        text = []
        read_pdf = PyPDF2.PdfReader(pdf_path)
        number_of_pages = len(read_pdf.pages)
        for page_num in range(number_of_pages):
            page = read_pdf.pages[page_num]
            content = page.extract_text()
            doc = nlp(content)
            text.append(doc)
            
        return text
    def preprocess(self, text: str) -> str:
        for token in text:
            print(token)
            # if token.is_stop == False and token.is_punct == False and token.is_space == False:
            #     text.append(token)
        return text