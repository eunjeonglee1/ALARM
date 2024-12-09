from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st

@st.cache_data
def create_vectorstore(_data):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000,
        chunk_overlap=0,
        encoding_name='cl100k_base'
    )
    documents = text_splitter.split_documents(_data)

    embeddings_model = HuggingFaceEmbeddings(
        # model_name='jhgan/ko-sroberta-multitask',
        # model_name='jhgan/ko-sbert-nli',
        model_name='BM-K/KoSimCSE-RoBERTa-multitask',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
    )


    # load db
    vectorstore = FAISS.load_local('db', embeddings_model,
                                   allow_dangerous_deserialization=True)

    # 웹베이스 로더 추가 멀티체인
    # Retrieval
    # 요리명 일련번호 관련 벡터에서 찾기
    retriever = vectorstore.as_retriever(
        search_type='mmr',
        search_kwargs={'k': 500, 'fetch_k': 600, 'lambda_mult': 0.9}
    )

    return retriever