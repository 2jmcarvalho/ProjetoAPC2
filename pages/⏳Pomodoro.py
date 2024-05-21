import streamlit as st
import time

# Definir tempos para os intervalos de trabalho e descanso em segundos
pomodoro_duration = 25 * 60  # 25 minutos
short_break_duration = 5 * 60  # 5 minutos
long_break_duration = 15 * 60  # 15 minutos

# Função de contagem regressiva
def countdown_timer(total_seconds):
    progress_bar = st.progress(0)
    timer_text = st.empty()
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_text.markdown(f"<h1 style='text-align: center;'>{timeformat}</h1>", unsafe_allow_html=True)
        progress_bar.progress((total_seconds - remaining) / total_seconds)
        time.sleep(1)
    st.success("Tempo Acabou!")

# Função para carregar o estilo customizado
def load_custom_css():
    st.markdown(
        """
        <style>
        .main {
            background: url('') no-repeat center center fixed;
            background-size: cover;
            color: ;
        }
        h1 {
            color: ;
            font-size: 48px;
            margin: 0;
        }
        .stButton>button {
            color: white;
            background-color: #ff6347;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stSelectbox div {
            font-size: 18px;
        }
        .stProgress div {
            height: 25px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Carregar o estilo customizado
load_custom_css()

# Título da aplicação
st.title("Cronômetro Pomodoro")

# Seleção de intervalo
selected_interval = st.radio(
    "Escolha o intervalo:",
    ("25min", "Pausa Curta", "Pausa Longa")
)

# Iniciar o cronômetro quando o botão for clicado
if st.button('Iniciar'):
    
    
    if selected_interval == "25min":
        st.toast('Bom estudo!!!')
        time.sleep(.5)
        st.toast('NERD')
        time.sleep(.5)
        st.toast('🤓🤓🤓')
        time.sleep(.5)
        st.write("Iniciando Pomodoro de 25 minutos...")
        countdown_timer(pomodoro_duration)
        st.balloons()
        
    elif selected_interval == "Pausa Longa":
        st.toast('Pode cochilar😴')
        time.sleep(.5)
        st.write("Iniciando Pausa Longa de 15 minutos...")
        countdown_timer(long_break_duration)

        
    elif selected_interval == "Pausa Curta":
        st.toast('Só não desiste')
        time.sleep(.5)
        st.write("Iniciando Pausa Curta de 5 minutos...")
        countdown_timer(short_break_duration)
        
