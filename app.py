import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import PyMuPDFLoader
from langchain.vectorstores import FAISS
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()

user_api_key = os.getenv("OPENAI_API_KEY")

# user_api_key = st.sidebar.text_input(
#     label="#### Your OpenAI API key 👇",
#     placeholder="Paste your openAI API key, sk-",
#     type="password")

# Query suggestions
query_suggestions = ["Query 1", "Query 2", "Query 3", "Query 4", "Query 5"]

st.sidebar.title("Query Suggestions")
st.sidebar.markdown(
    "<br>".join(
        f"<p style='padding: 1px; '>{query}</p>" for query in query_suggestions
    ),
    unsafe_allow_html=True
)
# selected_query = st.sidebar.selectbox("Select a query", query_suggestions)

# uploaded_file = st.sidebar.file_uploader("upload", type="csv")

data = None

# if uploaded_file:
#     #use tempfile because CSVLoader only accepts a file_path
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         tmp_file.write(uploaded_file.getvalue())
#         tmp_file_path = tmp_file.name

#     loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={
#                 'delimiter': ','})
#     data = loader.load()

persist_directory = "./storage"
pdf_path = "./Politics_in_Zimbabwe.pdf"

loader = PyMuPDFLoader(pdf_path)
data = loader.load()

vectorstore = None

if data:
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(data, embeddings)

# embeddings = OpenAIEmbeddings()
# vectorstore = FAISS.from_documents(data, embeddings)

if vectorstore:
    chain = ConversationalRetrievalChain.from_llm(
    llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo',max_tokens=20),
    retriever=vectorstore.as_retriever())

def conversational_chat(query):
    
    result = chain({"question": query, 
    "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    
    return result["answer"]

if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello ! Im TK how can i help you today"]
if 'past' not in st.session_state:
    st.session_state['past'] = [""]
    
#container for the chat history
response_container = st.container()
#container for the user's text input
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        st.markdown(
            """
            <style>
            ::placeholder {
                color: transparent;
            }

            :-ms-input-placeholder {
                color: transparent;
            }

            ::-ms-input-placeholder {
                color: transparent;
            }

            input:focus::placeholder {
                animation-name: blink-caret;
                animation-duration: 0.8s;
                animation-iteration-count: infinite;
                animation-timing-function: step-end;
            }

            input[type="text"] {
                border: none;
                outline: none;
            }

            @keyframes blink-caret {
                from, to { border-color: transparent; }
                50% { border-color: #000; }
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        user_input = st.text_input("", value="", key='input', help="Ask me about zim politics, Mugabe era")
        # user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
        submit_button = st.form_submit_button(label='Send')
        
    if submit_button and user_input:
        output = conversational_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

# if st.session_state['generated']:
#     with response_container:
#         for i in range(len(st.session_state['generated'])):
#             # message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="adventurer")
#             # message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
#             message(
#                 st.session_state["generated"][i],
#                 key=str(i),
#                 avatar_style="image",
#                 avatar_url="https://ivesexid.sirv.com/Portfolio/IMG_20230104_000907-removebg-preview.png"
#             )

if st.session_state.get('generated'):
    with response_container:
        for i in range(len(st.session_state['generated'])):
            st.markdown(
                f'<div><img src="https://ivesexid.sirv.com/Portfolio/IMG_20230104_000907-removebg-preview.png" style="border-radius: 50%; width: 30px; height: 30px; object-fit: cover; margin-right: 5px;" alt="Avatar"> {st.session_state["past"][i]}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div><img src="https://ivesexid.sirv.com/Portfolio/IMG_20230104_000907-removebg-preview.png" style="border-radius: 50%; width: 30px; height: 30px; object-fit: cover; margin-right: 5px;" alt="Avatar"> {st.session_state["generated"][i]}</div>',
                unsafe_allow_html=True
            )
