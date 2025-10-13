from pdf_handler import PDF_Handler
from vector_db import VectorDatabase

file_path = "./hydrogenprice-introduction.pdf"

pdf_handler = PDF_Handler(file_path) #instantiating

vector_db = VectorDatabase()  # instantiating

vector_db.loader(pdf_handler.load_docs(), fresh_load=True)  # loading documents into vector db
# now take a document and will pass to pdf_handler


print(vector_db.search("What is hydrogen fuel?"))  # searching in vector db



