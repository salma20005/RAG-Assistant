try:
    import chromedb
except ImportError:
    # Some environments use the package name "chromadb"
    import chromadb as chromedb
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


def retrieve_context(question, collection, n_results=3, as_list=False):
    query_embedding = embedding_model.encode(question)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
    )
    context = results["documents"][0]

    cleaned_context = []
    for item in context:
        text = str(item).strip().replace("\n", " ")
        if not text:
            continue
        words = text.split()
        if len(words) <= 2:
            continue
        cleaned_context.append(" ".join(words))

    if not cleaned_context:
        return [] if as_list else ""

    if as_list:
        return cleaned_context

    return " ".join(cleaned_context)