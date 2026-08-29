SEPARATOR_LEN = 80
print('LangChain Example') 
print(f'\n{'-' * SEPARATOR_LEN}\n')


# STEP 1 - LOAD DATA --------------------------------------------------------------------------------------
import wikipedia
wikipedia.set_user_agent("langchain-wiki-example/1.0 (example@mail.com)")
from langchain_core.documents import Document


page        = wikipedia.page(title="Mars", auto_suggest=False)
document    = Document(page_content=page.content, metadata={"title": page.title, "url": page.url})
# ----------------------------------------------------------------------------------------------------------



# STEP 2 - CHUNKING ----------------------------------------------------------------------------------------
from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter    = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks      = splitter.split_documents([document])
# ----------------------------------------------------------------------------------------------------------



# STEP 3 - EMBEDDING MODEL ---------------------------------------------------------------------------------
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


embeddings_model = OpenAIEmbeddings() # HuggingFace Trans
# ----------------------------------------------------------------------------------------------------------



# STEP 4 - EMBEDDING + In Memory Store ----------------------------------------------------------------------
from langchain_core.vectorstores import InMemoryVectorStore


vector_store = InMemoryVectorStore.from_documents(
    documents= chunks,
    embedding= embeddings_model
)
# ----------------------------------------------------------------------------------------------------------



# STEP 5 - QUERY DATA --------------------------------------------------------------------------------------
query = "What is the atmosphere of Mars made of?"

result = vector_store.similarity_search(query, k= 5)

query_related_chunks = "\n\n---\n\n".join([doc.page_content for doc in result])

print(f'Query: {query}')
print(f'\n{'-' * SEPARATOR_LEN}\n')
print(f'Result: \n{query_related_chunks}')
# ----------------------------------------------------------------------------------------------------------