# News Research Bot

## Overview

News Research Bot is a Streamlit-based web application that allows users to extract and analyze news articles using AI-powered retrieval techniques. The system leverages LangChain, FAISS, and Google's Gemini AI to process articles, store vector embeddings, and answer user queries based on indexed content.

## Features

- **Web Scraping:** Extracts text content from news article URLs.
- **Text Chunking:** Splits text into manageable chunks for efficient processing.
- **Vector Embedding:** Uses SentenceTransformer (all-MiniLM-L6-v2) for text representation.
- **FAISS-based Retrieval:** Stores and retrieves documents based on user queries.
- **Google Gemini AI:** Processes queries and generates responses.
- **Streamlit Web Interface:** User-friendly interface for submitting URLs and queries.

## Project Structure

```
News_Research_Bot/
│── Data/
│   ├── faiss.pkl  # FAISS index storage
│── app/
│   ├── main.py  # Streamlit web application
│── api/
│   ├── api.py  # Backend processing script
│── .env  # Environment variables (API keys)
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
```

## Installation

### Clone the repository:
```sh
git clone https://github.com/yourusername/News_Research_Bot.git
cd News_Research_Bot
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

### Set up environment variables:
Create a `.env` file in the root directory and add your Google API Key:
```sh
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Running the API Script

Navigate to the `api/` directory:
```sh
cd api
```
Run the FAISS indexing script:
```sh
python api.py
```
This script loads articles from predefined URLs, processes them, and stores embeddings in `faiss.pkl`.

### Running the Streamlit App

Navigate to the `app/` directory:
```sh
cd app
```
Launch the application:
```sh
streamlit run main.py
```
Enter article URLs and submit queries via the web interface.

## Technical Details

### FAISS Indexing
- The project utilizes FAISS for efficient similarity search.
- The FAISS index is created from document embeddings using SentenceTransformer.
- The stored index (`faiss.pkl`) allows quick retrieval without reprocessing.

### Query Processing
- User queries are processed through `RetrievalQAWithSourcesChain` from LangChain.
- The retriever fetches relevant text chunks from FAISS.
- Google's Gemini AI generates responses based on retrieved content.

## Compatibility & Considerations

- The Streamlit application (`main.py`) and API script (`api.py`) use the same FAISS index (`faiss.pkl`).
- Ensure that both scripts use the same embedding model (`all-MiniLM-L6-v2`).
- If the FAISS index does not exist, the Streamlit app prompts users to process URLs.

## Dependencies

- **Python 3.8+**
- **Streamlit**
- **LangChain**
- **FAISS**
- **SentenceTransformers**
- **Google Generative AI SDK**
- **Unstructured (for text extraction)**
- **Python-dotenv**

Install all dependencies using:
```sh
pip install -r requirements.txt
```

## Troubleshooting

- **Google API Key Not Found:** Ensure `.env` file contains `GOOGLE_API_KEY`.
- **FAISS Index Not Found:** Run `api.py` before using `main.py`.
- **Incorrect Query Results:** Confirm that the FAISS index and embedding model match.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **LangChain** for enabling seamless AI-powered retrieval.
- **FAISS** for efficient vector search.
- **Gemini AI** for language model support.
- **SentenceTransformers** for embeddings.

## Contact

For issues or contributions, reach out via GitHub or email at **pranjaldhamane37@gmail.com**.

