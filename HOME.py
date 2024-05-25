import os
import streamlit as st
import sqlite3

def exibir_videos_youtube(videos, termo_busca):
    st.write("Vídeos:")
    
    for video in videos:
        if termo_busca.lower() in video['titulo'].lower():
            #st.markdown(f"[{video['titulo']}]({video['link']})")
            st.video(video['link'])
            st.markdown(f"<p style='text-align:center;'>{video['titulo']}</p>", unsafe_allow_html=True)

def exibir_canais_youtube(canais, termo_busca):
    st.write("Canais:")
    for canal in canais:
        if termo_busca.lower() in canal['titulo'].lower():
            #st.markdown(f"[{video['titulo']}]({video['link']})")
            st.markdown(f'<a href="{canal["link"]}"><img src="{canal["imagem"]}" width="200"></a>', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:;'>{canal['titulo']}</p>", unsafe_allow_html=True)




    
    

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
    tab1, tab2 = st.tabs(["Inicio", "Monitoria(em breve)"])

    with tab1:


        
        videos = [
        {"titulo": "INTRODUÇÃO ÀS FUNÇÕES COM DUAS VARIÁVEIS 1", "link": "https://www.youtube.com/watch?v=jjFYS51D4WE"},
        {"titulo": "Lady Gaga - Bad Romance (Official Music Video)", "link": "https://www.youtube.com/watch?v=qrO4YZeyl0I"},
        {"titulo": "Aula 01 Cálculo II - Funções de Várias Variáveis", "link": "https://www.youtube.com/watch?v=LmmPho49tDc&list=PLrOyM49ctTx9EGYGvXS6KVA9aoB3P4lJD"},
        {"titulo": "Billie Eilish - LUNCH (Official Music Video)", "link": "https://www.youtube.com/watch?v=MB3VkzPdgLA"},
    ]
        canais = [
        {"titulo": "Canal 1", "link": "https://www.youtube.com/@HelpEngenharia" , "imagem": "https://yt3.googleusercontent.com/68JRWeh5ZsvALQXATU2eeeYmIHRLpYnWChBcVc8AWlpi_Xsm_kaJfcRTlnE8-33cGUBj753cbLQ=s160-c-k-c0x00ffffff-no-rj"},
        
    ]
        termo_busca = st.text_input("Digite o título do vídeo:")
        #exibir_playlist_youtube(playlist, termo_busca)

        s1, s2 = st.columns([3,1])
        with s1:
            exibir_videos_youtube(videos, termo_busca)
        with s2:
            exibir_canais_youtube(canais, termo_busca)


    


if __name__ == "__main__":
    main()
