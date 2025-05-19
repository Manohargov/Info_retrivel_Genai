import streamlit as st
import time
from src.helper import get_pdf_text,Get_text_chunks,get_vector_store,get_conversational_chain



def user_input(user_question):
    response = st.session_state.conversation({"question": user_question,})
    st.session_state.chatHistory = response['chat_history']
    for in ,message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("User", message.content))
        else:
            st.write("Assistant", message.content,)


def main():
    st.set_page_config(page_title="Information Retrieval")
    st.header("📄 Info_retrivel_Genai")

    user_question = st.text_input("Ask a question about your PDF documents")
    if "coversation" not in st.session_state:
        st.session_state.coversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu")
        pdf_docs =st.file_uploader("Upload your PDF files and Click on the submit & process button",accept_multiple_files=True)
        if st.botton("submit & process"):
            with st.spinner("processing..."):
                raw_text =get_pdf_text(pdf_docs)
                text_chunks = Get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.coversation= get_conversational_chain(vector_store)



                time.sleep(2)

                st.success("Done")
      

if __name__ == "__main__":
    main()
