import chromedb
from modules.embedding import load_model
embedding_model = load_model()
def build_vector__db(chunks):
    client = chromedb.Client()
    collection = client.get_or_create_collection("Course")
    embeddings = embedding_model.encode(chunks)
    ids = [str(i) for i in range(len(chunks))]
    try:
        collection.delete(ids=ids)
    except:
        pass
    collection.add(ids=ids, documents=chunks, embeddings=embeddings)
    return collection
def retrieve_context(question, collection):
    query_embedding = embedding_model.encode(question)
    results = collection.query(query_texts=[query_embedding], n_results=3)
    context = results["documents"][0]
    return "\n\n".join(context)