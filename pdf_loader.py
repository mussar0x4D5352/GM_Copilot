from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader

def load_all_pdfs(path):
    loader = PyPDFDirectoryLoader(path)
    return loader.load()

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()

def split_pdf(loader):
    return loader.load_and_split()
