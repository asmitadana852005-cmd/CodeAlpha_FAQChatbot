import streamlit as st

from chatbot import FAQChatbot


# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------
# Title
# --------------------------------

st.title("🤖 AI FAQ Chatbot")

st.write(
    "Ask a question and the chatbot will find "
    "the most relevant answer from the FAQ database."
)


# --------------------------------
# Load Chatbot
# --------------------------------

chatbot = FAQChatbot("faq.csv")


# --------------------------------
# Chat History
# --------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------
# Display Previous Messages
# --------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# --------------------------------
# User Input
# --------------------------------

user_question = st.chat_input(
    "Ask your question..."
)


# --------------------------------
# Process Question
# --------------------------------

if user_question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.write(user_question)


    # Get chatbot answer
    answer = chatbot.get_answer(
        user_question
    )


    # Store chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    # Display chatbot response
    with st.chat_message("assistant"):

        st.write(answer)