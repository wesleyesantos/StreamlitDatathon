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
    
st.subheader(':blue[Conclusão]',divider='blue')