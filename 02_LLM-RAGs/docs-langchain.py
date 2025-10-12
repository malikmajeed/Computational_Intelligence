from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50, #characters per chunk use 5k or more to fit pdf data
    chunk_overlap=20, #overlap between chunks
    length_function=len,
    is_separator_regex=False)


Document = PyPDFLoader("/document.pdf")
pages = Document.load()


print(f"Total Pages in PDF: {len(pages)} and type of pages is {type(pages)}")