
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


#creating a class so we can access it in other files
#when we use SELF we makes it accessiblel throughout the class and its = THIS
class PDF_Handler():

#_init_ is a constructor that will run when the class is instantiated
#we're document path, chunk size and chunk overlap as parameters
    def __init__(self,document_path:str, chunk_size:int = 500, chunk_overlap:int = 20):
        self.document_path = document_path

        #instantiating the text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,      
            chunk_overlap= chunk_overlap,  #chunkoverlap is the overlap between chunks     #overlap is 20 characters
            length_function=len,
            is_separator_regex=False    #regex is used for pattern matching (like email validation etc) we're not using it

        )

    def load_docs(self):
        loader = PyPDFLoader(self.document_path)
        pages = loader.load()
        chunks = []

        for i in pages:
            text = i.page_content
            peices = self.text_splitter.create_documents([text])
            chunks.extend(peices)

        return chunks
