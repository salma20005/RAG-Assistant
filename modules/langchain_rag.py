from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import tempfile
import uuid
# embedding
from langchain_huggingface import HuggingFaceEmbeddings
from modules.embedding import load_model
embedding_model = load_model()
# build retriever
def build_retriever(file):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp:
        temp.write(file.read())
        temp.flush()
        # loading pdf file
        loader = PyPDFLoader(temp.name)
        docs = loader.load()
        # Chunking
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)
        print(f"Chunk count: {len(splits)}")
        for chunk in splits:
            print(chunk.page_content)
        # embedding
        embedding_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
        )
        # vector database
        db = Chroma.from_documents(documents=splits, embedding=embedding_model,
                                   collection_name=str(uuid.uuid4()))
        data = db.get()
        print(data["documents"][0])
        # retriever
        # search engine
        # get top k documents
        retriever = db.as_retriever(search_kwargs={"k": 5})

        return  retriever

