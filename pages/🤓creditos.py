import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3, col4, col5= st.columns(5)
with col1:
    st.header("A Crara")
    st.image("./img/clara.jpeg", width=200 )
    st.link_button("Github", "https://github.com/CraraMaria")
    
with col2:
    st.header("JohnK")
    st.image("./img/johnk.jpeg", width=200)
    st.link_button("Github", "https://github.com/2jmcarvalho")

with col3:
    st.header("Ana")
    st.image("./img/ana.jpeg", width=200)
    st.link_button("Github", "https://gist.github.com/AnaSouza-Dev")

with col4:
    st.header("kore")
    st.image("./img/kore.jpeg", width=200)
    st.link_button("Github", "https://github.com/AnaKanashiro")

with col5:
    st.header("Tutu")
    st.image("./img/tutu.png", width=200)
    st.link_button("Github", "https://github.com/TutsXD1")
        
st.write('<span style="color:blue">Muitos universitários chegam a faculdade e ficam perdidos sem saber onde procurar informações e ajuda, ao ter um ambiente de ajuda de universitário para universitário cria um ambiente de ajuda que entra em loop, sempre entram novos e os veteranos ficam para ajudar os próximos</span>', unsafe_allow_html=True)
