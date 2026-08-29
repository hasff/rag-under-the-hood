SEPARATOR_LEN = 80
print('\nLlama Index Example') 
print(f'\n{'-' * SEPARATOR_LEN}\n')


# STEP 1 - LOAD DATA --------------------------------------------------------------------------------------
import wikipedia
wikipedia.set_user_agent("langchain-wiki-example/1.0 (example@mail.com)")
from llama_index.core import Document
 
 
page        = wikipedia.page(title="Mars", auto_suggest=False)
document    = Document(text=page.content, metadata={"title": page.title, "url": page.url})
# ----------------------------------------------------------------------------------------------------------



# STEP 2 - CHUNKING ----------------------------------------------------------------------------------------
from llama_index.core.node_parser import SentenceSplitter
 
 
splitter    = SentenceSplitter(chunk_size=800, chunk_overlap=100)
nodes       = splitter.get_nodes_from_documents([document])
# ----------------------------------------------------------------------------------------------------------



# STEP 3 - EMBEDDING MODEL ---------------------------------------------------------------------------------
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
 
 
load_dotenv()
 
 
embeddings_model = OpenAIEmbedding()
# ----------------------------------------------------------------------------------------------------------



# STEP 4 - EMBEDDING + In Memory Store ----------------------------------------------------------------------
from llama_index.core import VectorStoreIndex
 
 
index = VectorStoreIndex(
    nodes= nodes,
    embed_model= embeddings_model
)
# ----------------------------------------------------------------------------------------------------------



# STEP 5 - QUERY DATA --------------------------------------------------------------------------------------
query                   = "What is the atmosphere of Mars made of?"
 
retriever               = index.as_retriever(similarity_top_k=5)
result                  = retriever.retrieve(query)
 
query_related_chunks    = "\n\n---\n\n".join([node.get_content() for node in result])
 
print(f'Query: {query}')
print(f'\n{"-" * SEPARATOR_LEN}\n')
print(f'Result: \n{query_related_chunks}')
# ----------------------------------------------------------------------------------------------------------


