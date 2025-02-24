import streamlit as st
from openai import OpenAI
from os import environ
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Initialize OpenAI client
client = OpenAI(api_key=environ['OPENAI_API_KEY'])

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hello! You can upload documents and ask me questions about them."}]
    if "document_store" not in st.session_state:
        st.session_state["document_store"] = None
    if "uploaded_files" not in st.session_state:
        st.session_state["uploaded_files"] = []

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def process_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    else:  # txt files
        return uploaded_file.getvalue().decode("utf-8")

def create_document_store(documents):
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    # Process all documents and their metadata
    texts = []
    metadatas = []
    for doc, file_name in documents:
        chunks = text_splitter.split_text(doc)
        texts.extend(chunks)
        metadatas.extend([{"source": file_name}] * len(chunks))
    
    # Create vector store
    embeddings = OpenAIEmbeddings(model="openai.text-embedding-3-small")
    vector_store = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
    return vector_store

def get_relevant_context(query, vector_store, k=3):
    results = vector_store.similarity_search(query, k=k)
    contexts = []
    for doc in results:
        source = doc.metadata.get("source", "Unknown")
        contexts.append(f"From {source}:\n{doc.page_content}")
    print(contexts)
    return "\n\n".join(contexts)

def main():
    st.title("📚 Advanced Document Q&A")
    init_session_state()
    
    # File uploader section
    uploaded_files = st.file_uploader(
        "Upload documents (PDF or TXT)",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )
    
    # Process newly uploaded files
    if uploaded_files and uploaded_files != st.session_state.uploaded_files:
        with st.spinner("Processing documents..."):
            documents = []
            for file in uploaded_files:
                text = process_file(file)
                documents.append((text, file.name))
            
            st.session_state.document_store = create_document_store(documents)
            st.session_state.uploaded_files = uploaded_files
            st.success(f"Successfully processed {len(uploaded_files)} documents!")
    
    # Display chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Chat input
    if question := st.chat_input(
        "Ask a question about the documents",
        disabled=not st.session_state.document_store
    ):
        # Add user question to chat history
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)
        
        # Get relevant context from the document store
        context = get_relevant_context(question, st.session_state.document_store)
        
        # Generate response using OpenAI
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="openai.gpt-4o",
                messages=[
                    {"role": "system", "content": f"""You are a helpful assistant answering questions about documents. 
                    Use the following context from the documents to answer the user's question. If you're not sure 
                    about something, say so. Here's the relevant context:\n\n{context}"""},
                    {"role": "user", "content": question}
                ],
                stream=True
            )
            response = st.write_stream(stream)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
