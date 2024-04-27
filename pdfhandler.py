from langchain_community.document_loaders import PyPDFLoader


def loadPdf(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load()
    return pages

# loadPdf("./somatosensory.pdf")