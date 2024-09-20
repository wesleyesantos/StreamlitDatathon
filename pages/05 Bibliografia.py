import streamlit as st

st.set_page_config(layout = "wide")
st.markdown("""<style>[data-testid="stSidebar"] {background: linear-gradient(180deg, #00c6ff, #0072ff);padding: 20px;}.icon-container {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<font face= Helvetica><b><u>Desenvolvedor</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Wesley E. dos Santos  
                - Fiap Postech - 3DTAT''')
    linkedin_url = "https://www.linkedin.com/in/wesleyesantos/"
    youtube_url = "https://www.youtube.com/@Wesley_santos-Excel_PowerBI"
    st.sidebar.markdown(f"""<div class="icon-container"><a href="{linkedin_url}" target="_blank"><img src="https://github.com/wesleyesantos/Datathon/blob/main/Images/linkedin.png?raw=true" width="30"/></a><a href="{youtube_url}" target="_blank"><img src="https://github.com/wesleyesantos/Datathon/blob/main/Images/youtube.png?raw=true" width="30"/></a></div>""", unsafe_allow_html=True)
    st.sidebar.image('https://github.com/wesleyesantos/Datathon/blob/main/Images/eu.jpg?raw=true', use_column_width=True)

st.subheader(':blue[Bibliografia]', divider='blue')

st.markdown(
        """
        1. Documentação pandas: https://pandas.pydata.org/docs/index.html,
        2. Documentação Matplotlib: https://matplotlib.org/stable/users/index.html,
        3. Documentação Streamlit: https://docs.streamlit.io,
        4. Documentação Plotly: https://plotly.com/python/getting-started/,
        5. Passos Mágicos: https://passosmagicos.org.br,
        6. Google colab: https://colab.research.google.com,
        7. Github: https://docs.github.com/pt
        8. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2020. Associação Passos Mágicos. 
        9. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2021. Associação Passos Mágicos. 
        10. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2022. Associação Passos Mágicos.
    """, unsafe_allow_html=True
    )