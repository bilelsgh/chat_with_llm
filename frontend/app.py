import sys

sys.path.append("..")

import streamlit as st
from utils import display_chat_messages

from clients.llmclient import available_models
from config.config import key
from helpers.utils import get_llm_client, get_model_type_from_input

# Model choice
client_choice = st.selectbox("Chose your model", list(available_models.keys()))
model_type = get_model_type_from_input(client_choice)

# Init the client
if "client" not in st.session_state or st.session_state.client_choice != client_choice:
    try:
        st.session_state.client = get_llm_client(model=model_type, key=key)
        st.session_state.client_choice = client_choice
        st.info(f"Model `{client_choice}` selected.")
    except Exception as e:
        st.error(f"Error while creating the client: {e}")

# Start the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Comment puis-je t'aider ?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = st.session_state.client.ask(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

display_chat_messages()
