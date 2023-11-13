import sys
import lib
import openai
import os
import datetime
from dotenv import load_dotenv, find_dotenv

llm_name=""
current_date = datetime.datetime.now().date()
if current_date < datetime.date(2023, 9, 2):
    llm_name = "gpt-3.5-turbo-0301"
else:
    llm_name = "gpt-3.5-turbo"


_=load_dotenv(find_dotenv())
openai.api_key=os.environ['OPENAI_API_KEY']

def load_db(file, chain_type, k):
    loaded_db = lib.PyPDFLoader(file)
    document = loaded_db.load()
    split_text = lib.RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = split_text.split_documents(document)
    embeddings = lib.OpenAIEmbeddings()
    db = lib.DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_type='similarity',kwargs={'k':k})
    qa = lib.ConversationalRetrievalChain(llm = lib.ChatOpenAI(model_name=llm_name, temperature=0),
                                          chain_type=chain_type,
                                          retriever=retriever,
                                          return_generated_question=True,
                                          return_source_documents=True,
                                          )
    return qa
    








