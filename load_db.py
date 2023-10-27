import lib
# def func(file, kwargs={})
def load_db(file, chain_type, k):
# Load Documents
    loader = lib.PyPDFLoader(file)
    documents = loader.load() # Original documents
    # Define Text Splitter
    text_splitter = lib.RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=150)
    # Split documents
    docs = text_splitter.split_documents(documents) # New Split Documents

    # Create embeddings before creating vector store
    embeddings = lib.OpenAIEmbeddings()
    # Create Vector Store with embeddings for Semantic Search
    db = lib.DocArrayInMemorySearch.from_documents(docs = docs,embeddings=embeddings)

    # Create retriever
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":k})
   
