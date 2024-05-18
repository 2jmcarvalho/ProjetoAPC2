import os
import streamlit as st
import sqlite3

def exibir_videos_youtube(videos, termo_busca):
    st.write("Vídeos:")
    for video in videos:
        if termo_busca.lower() in video['titulo'].lower():
            #st.markdown(f"[{video['titulo']}]({video['link']})")
            st.video(video['link'])
            st.write(video['titulo'], text_align='center')





    
    

st.set_page_config(layout="wide", page_title="Guia do Universitario", page_icon="🤓")
st.title("Guia do Universitario")

def register(username, password):
    with open("user_credentials.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def login(username, password):
    with open("user_credentials.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

#def main():
    st.title("Login e Registro")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")


    if st.button("Registrar"):
        if len(username) == 0 or len(password) == 0:
            st.warning("Por favor, preencha todos os campos.")
        else:
            register(username, password)
            st.success("Registro realizado com sucesso. Você pode fazer login agora.")
    if st.button("Login"):
        if len(username) == 0 or len(password) == 0:
            st.warning("Por favor, preencha todos os campos.")
        else:
            if os.path.exists("user_credentials.txt"):
                if login(username, password):
                    st.success("Login bem-sucedido!")
                    st.empty()
                    next_page(username)  # Chamada para a próxima página após o login
                else:
                    st.error("Credenciais inválidas.")
            else:
                st.error("Nenhum usuário registrado. Por favor, registre-se primeiro.")


def main():
    #st.title(f"Bem-vindo, {username}!")
    tab1, tab2 = st.tabs(["Inicio", "Créditos"])

    with tab1:
        st.subheader("canais recomendados")
        st.markdown(f'<a href="{"https://www.youtube.com/@CanalUSP"}"><img src="{"https://yt3.googleusercontent.com/hwpjVSGYUvTWn6wtXJ_75BWdwG_Z_erSU-gM3XfsqzzHI51QPnKErtC5iJEshXc86T7nNTh5tq0=s160-c-k-c0x00ffffff-no-rj"}" width="200"></a>', unsafe_allow_html=True)
        st.subheader("videos recomendados")
        videos = [
        {"titulo": "INTRODUÇÃO ÀS FUNÇÕES COM DUAS VARIÁVEIS 1", "link": "https://www.youtube.com/watch?v=jjFYS51D4WE"},
        {"titulo": "Lady Gaga - Bad Romance (Official Music Video)", "link": "https://www.youtube.com/watch?v=qrO4YZeyl0I"},
        {"titulo": "Aula 01 Cálculo II - Funções de Várias Variáveis", "link": "https://www.youtube.com/watch?v=LmmPho49tDc&list=PLrOyM49ctTx9EGYGvXS6KVA9aoB3P4lJD"},
        #{"tirulo": "teste", "link": "https://www.youtube.com/watch?v=MB3VkzPdgLA"}
    ]
        termo_busca = st.text_input("Digite o título do vídeo:")
        #exibir_playlist_youtube(playlist, termo_busca)

        s1, s2, s3 = st.columns(3)
        with s1:
            exibir_videos_youtube(videos, termo_busca)
        with s2:
            st.header("canais(em breve)")


    


if __name__ == "__main__":
    main()
