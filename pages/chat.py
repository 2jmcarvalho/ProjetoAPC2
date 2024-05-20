import streamlit as st
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Conversation

def main():
    st.title("ChatGPT with Streamlit")
    st.write("Talk to me!")

    # Carregar o modelo e o tokenizador do GPT-Neo
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    model = GPT2LMHeadModel.from_pretrained("EleutherAI/gpt-neo-125M")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input.strip() != "":
            with st.spinner("Thinking..."):
                # Iniciar conversa com GPT-Neo
                conversation = Conversation(tokenizer, model)
                response = conversation.reply(user_input)
            st.text_area("GPT-Neo:", value=response, height=150, max_chars=None, key=None)

if __name__ == "__main__":
    main()
