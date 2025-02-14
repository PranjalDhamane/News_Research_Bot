import os
import streamlit as st
import pickle
import time
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API Key is missing. Please add it to your .env file.")
    st.stop()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

# Define FAISS file path (must match API script)
file_path = r"C:\Github\News_Research_Bot\Data\faiss.pkl"

st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
main_placeholder = st.empty()

# Load or Process FAISS
if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        vectorstore = pickle.load(f)
else:
    vectorstore = None

if process_url_clicked:
    if not urls:
        st.warning("Please enter at least one URL before processing.")
    else:
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("🔄 Loading data from URLs...")
        
        try:
            data = loader.load()
        except Exception as e:
            st.error(f"Error loading URLs: {e}")
            st.stop()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        docs = text_splitter.split_documents(data)

        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        vectorstore = FAISS.from_documents(docs, embeddings)
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore, f)

        st.success("✅ Data processed and stored successfully!")

query = main_placeholder.text_input("🔍 Ask a question about the articles:")

if query:
    if not vectorstore:
        st.error("No FAISS index found. Please process URLs first.")
    else:
        retriever = vectorstore.as_retriever()
        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=llm, retriever=retriever, chain_type="stuff"
        )

        with st.spinner("🔎 Searching for answers..."):
            result = chain({"question": query}, return_only_outputs=True)

        st.header("📜 Answer")
        st.write(result.get("answer", "No answer found."))

        sources = result.get("sources", "")
        if sources:
            st.subheader("📌 Sources:")
            for source in sources.split("\n"):
                st.write(source)
