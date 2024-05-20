import streamlit as st

# Define o tema personalizado
def main():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #f5f5f5;
        }
        .sidebar .sidebar-content {
            background: #3498db;
            color: #ffffff;
        }
        .Widget>label {
            color: #ffffff;
        }
        .stButton>button {
            background-color: #3498db;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Seu código Streamlit continua abaixo
    st.title('Meu Site Azul')
    st.write('Bem-vindo ao meu site com tema azul!')

if __name__ == '__main__':
    main()

