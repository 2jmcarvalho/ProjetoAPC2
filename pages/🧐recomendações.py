import streamlit as st

class Node:
    def __init__(self, video_url):
        self.video_url = video_url
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, video_url):
        new_node = Node(video_url)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def get_videos(self):
        videos = []
        if self.head:
            current = self.head
            while True:
                videos.append(current.video_url)
                current = current.next
                if current == self.head:
                    break
        return videos

    def clear(self):
        self.head = None

def save_videos_to_file(videos, filename):
    with open(filename, "w") as f:
        for video in videos:
            f.write(f"{video}\n")

def load_videos_from_file(filename):
    videos = []
    try:
        with open(filename, "r") as f:
            videos = [line.strip() for line in f]
    except FileNotFoundError:
        pass
    return videos

# Criação da lista encadeada circular
cll = CircularLinkedList()

# Nome do arquivo para salvar os vídeos
video_file = "videos1.txt"

# Carregar vídeos do arquivo
loaded_videos = load_videos_from_file(video_file)
for video in loaded_videos:
    cll.append(video)

def main():
    # Formulário para adicionar um novo vídeo
    
    st.write('<span style="color:yellow">Mande recomendações de videos, iremos analizar e adicionar ao site</span>', unsafe_allow_html=True)
    with st.form("Adicionar vídeo"):
        new_video_url = st.text_input("URL do vídeo")
        submit_button = st.form_submit_button("Adicionar")

        if submit_button and new_video_url:
            cll.append(new_video_url)
            videos = cll.get_videos()
            save_videos_to_file(videos, video_file)
            st.success("Vídeo adicionado com sucesso!")

    s1,s2,s3 = st.columns([1,3,1])
       

    with s2:
        # Configuração inicial do Streamlit
        st.title("Recomendações:")

        # Criar uma sessão para o estado do índice
        if "video_index" not in st.session_state:
            st.session_state.video_index = 0

        videos = cll.get_videos()

        # Mostrar o vídeo atual
        if videos:
            st.video(videos[st.session_state.video_index])
        else:
            st.write("Nenhum vídeo disponível.")

        # Botões para navegar na lista encadeada circular
        if st.button("Próximo"):
            st.session_state.video_index = (st.session_state.video_index + 1) % len(videos)

        if st.button("Anterior"):
            st.session_state.video_index = (st.session_state.video_index - 1) % len(videos)



if __name__ == "__main__":
    main()
