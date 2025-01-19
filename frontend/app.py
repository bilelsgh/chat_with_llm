import sys

sys.path.append("..")

import streamlit as st
from utils import display_chat_messages

from clients.mistral import MistralClient
from config.config import key, model_name

client = MistralClient(model_name=model_name, key=key)

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Comment puis-je t'aider ?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.ask(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

display_chat_messages()
