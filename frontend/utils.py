"""
Utils function for streamlit app
"""

import streamlit as st


def display_chat_messages():
    with st.container(border=True):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
