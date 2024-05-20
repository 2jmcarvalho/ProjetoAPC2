import streamlit as st
from transformers import pipeline

def main():
    st.title("ChatGPT with Streamlit")
    st.write("Talk to me!")

    # Carregar o modelo ChatGPT
    chatbot = pipeline("conversational")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input.strip() != "":
            with st.spinner("Thinking..."):
                response = chatbot(user_input)[0]['generated_text']
            st.text_area("ChatGPT:", value=response, height=150, max_chars=None, key=None)

if __name__ == "__main__":
    main()
