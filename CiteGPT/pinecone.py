import pinecone

# connect to pinecone environment
pinecone.init(
    api_key="YOUR_API_KEY",
    environment="YOUR_ENV"  # find next to API key in console
)

index_name = "abstractive-question-answering"

# check if the abstractive-question-answering index exists
if index_name not in pinecone.list_indexes():
    # create the index if it does not exist
    pinecone.create_index(
        index_name,
        dimension=768,
        metric="cosine"
    )

# connect to abstractive-question-answering index we created
index = pinecone.Index(index_name)