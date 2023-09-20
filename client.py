from jina import Client, Document
from docarray import DocList
from docarray.documents import TextDoc
from models import PDFDocument

if __name__ == '__main__':
    c = Client(port=54321)
    pdf_path = 'documentos/2023/92-2023 - Alteração da Resolução Consuni nº 07-2019 - Prevenção e Segurança Laboratórios da UFT - Consuni-UFT.pdf'
    # pdf_document = Document(uri=pdf_path, mime_type='application/pdf')
    # pdf_document.uri = pdf_path
    pdf_document = PDFDocument(uri=pdf_path, mime_type='application/pdf')
    print(pdf_document)
    # passar o documento para o executor
    c.post(on='/', inputs=pdf_document, return_results=True)

    #pdf_document.mime_type = 'application/pdf'  # Defina o mime_type conforme necessário

    #pdf_document.uri = pdf_path

#     pri    c.post(on='/', inputs=pdf_document, return_results=True)
# nt(da.text)