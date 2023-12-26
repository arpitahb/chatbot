import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(files):
    text = ""
    for pdf in files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:  # Corrected attribute name to 'pages'
            text += page.extract_text()
    return text
def get_text_chunks(raw_text):
    text_splitter= CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function= len
    )
    chunks= text_splitter.split_text(raw_text)



    return chunks

def main():
    load_dotenv()
    st.set_page_config(page_title="InterviewBot")
    st.header('AI Interview Bot', divider='grey')
    
    
    user_input = st.text_input("How may I assist You?")

    with st.sidebar:
        st.subheader("Your documents")
        uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Check if files are uploaded
                if uploaded_files:
                    # Get text from PDF files
                    raw_text = get_pdf_text(uploaded_files)
                    

                    # Get Chunks of text
                    text_chunks= get_text_chunks(raw_text)
                    st.write(text_chunks)
                    # ...

if __name__ == '__main__':
    main()
