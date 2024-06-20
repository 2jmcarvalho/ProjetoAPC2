import os
import streamlit as st
from meus_canais import canais
from meus_videos import videos


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
            st.markdown(f'<div style="text-align: center;"><a href="{canal["link"]}"><img src="{canal["imagem"]}" width="200"></a></div>', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'>{canal['titulo']}</p>", unsafe_allow_html=True)

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

def main():
    #st.title(f"Bem-vindo, {username}!")
    termo_busca = st.text_input("Pesquisa")
    tab1, tab2 = st.tabs(["Vídeos", "Canais"])
    
    with tab1:  
        c1,c2,c3 = st.columns([1,3,1])
        with c2:
            exibir_videos_youtube(videos, termo_busca)
        

    with tab2:
        exibir_canais_youtube(canais, termo_busca)



if __name__ == "__main__":
    main()
