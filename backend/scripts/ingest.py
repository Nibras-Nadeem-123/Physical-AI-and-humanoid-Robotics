import os
import re
from glob import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAI
from qdrant_client import QdrantClient, models

# Initialize OpenAI client
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Qdrant client
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
client_qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

COLLECTION_NAME = "book_chunks"
EMBEDDING_SIZE = 1536 # For "text-embedding-ada-002"

def clean_text(text):
    """
    Cleans the text by removing markdown formatting and other non-textual elements.
    """
    # Remove markdown headers
    text = re.sub(r'#+\s', '', text)
    # Remove images
    text = re.sub(r'!\[.*\]\(.*\)', '', text)
    # Remove links
    text = re.sub(r'\[.*\]\(.*\)', '', text)
    # Remove code blocks
    text = re.sub(r'```.*```', '', text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r'`.*`', '', text)
    # Remove other markdown elements
    text = re.sub(r'[\*_~]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_book_content(docs_path="frontend/docs"):
    """
    Extracts the content from all .mdx files in the docs directory.
    """
    all_text = ""
    for filepath in glob(os.path.join(docs_path, "**/*.mdx"), recursive=True):
        with open(filepath, "r", encoding="utf-8") as f:
            all_text += f.read()
    return all_text

def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Chunks the text into smaller pieces using RecursiveCharacterTextSplitter.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def generate_embeddings(text_chunks):
    """
    Generates embeddings for a list of text chunks using OpenAI API.
    """
    response = client_openai.embeddings.create(
        input=text_chunks,
        model="text-embedding-ada-002"
    )
    embeddings = [embedding.embedding for embedding in response.data]
    return embeddings

def upload_vectors_to_qdrant(collection_name, chunks, embeddings):
    """
    Uploads vectors and their payloads to the Qdrant collection.
    """
    points = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            models.PointStruct(
                id=i,
                vector=embedding,
                payload={"text": chunk}
            )
        )
    client_qdrant.upsert(
        collection_name=collection_name,
        points=points
    )
    print(f"Uploaded {len(points)} vectors to Qdrant collection '{collection_name}'.")

def main():
    """
    This script extracts book content, cleans it, chunks it,
    generates embeddings, and uploads them to Qdrant.
    """
    print("Ingesting data...")
    create_qdrant_collection(COLLECTION_NAME)
    content = extract_book_content()
    cleaned_content = clean_text(content)
    chunks = chunk_text(cleaned_content)
    print(f"Created {len(chunks)} chunks.")
    embeddings = generate_embeddings(chunks)
    print(f"Generated {len(embeddings)} embeddings.")
    upload_vectors_to_qdrant(COLLECTION_NAME, chunks, embeddings)
    print("Data ingestion complete.")


if __name__ == "__main__":
    main()
