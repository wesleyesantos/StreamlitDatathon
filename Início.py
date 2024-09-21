import streamlit as st

st.set_page_config(page_title="Datathon Passos Mágicos",  page_icon="💎",layout = "wide")
st.sidebar.title("Página Inicial")

st.markdown("""<style>[data-testid="stSidebar"] {background: linear-gradient(180deg, #00c6ff, #0072ff);padding: 20px;}.icon-container {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<font face= Helvetica><b><u>Desenvolvedor</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Wesley E. dos Santos  
                - Fiap Postech - 3DTAT''')
    linkedin_url = "https://www.linkedin.com/in/wesleyesantos/"
    youtube_url = "https://www.youtube.com/@Wesley_santos-Excel_PowerBI"
    github_url = "https://github.com/wesleyesantos/StreamlitDatathon"
    st.sidebar.markdown(f"""<div class="icon-container"><a href="{linkedin_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/linkedin.png?raw=true" width="30"/></a><a href="{youtube_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/youtube.png?raw=true" width="30"/></a></div>""", unsafe_allow_html=True)
    st.sidebar.markdown(
    f"""
    <div style="display: flex; justify-content: flex-start;">
        <a href="{linkedin_url}" target="_blank" style="margin-right: 10px;">
            <img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/linkedin.png?raw=true" width="30"/>
        </a>
        <a href="{youtube_url}" target="_blank" style="margin-right: 10px;">
            <img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/youtube.png?raw=true" width="30"/>
        </a>
        <a href="{github_url}" target="_blank">
            <img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/github.png?raw=true" width="30"/>
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)
    st.sidebar.image('https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/eu.jpg?raw=true', use_column_width=True)


st.title(":blue[Evolução dos Alunos na PASSOS MÁGICOS [2020-2022]]")
st.subheader(':blue[Visão geral do Projeto]',divider='blue')

st.markdown("<big><big><big><big><big><i><b> Seja Bem vindo ao meu Datathon! 👋", unsafe_allow_html=True)

st.markdown('''Desenvolvedor: Wesley Estevão dos Santos | RM352704<br> 
            Postech FIAP  <br>
            Curso: Data Analytics | 3DTAT
            ''', unsafe_allow_html=True)

st.subheader(':blue[Resumo]',divider='blue')
st.markdown('''Esse é um projeto realizado para fins de estudo de caso, em uma parceria da <b><font color='blue'>Postech FIAP</font></b> com a instituição <b><font color='blue'>PASSOS MÁGICOS</b></font>, a instiruição traz aqui alguns desafios reais para os alunos da Postech, deixando em pauta os desafios abaixo que considerei nesse projeto.''', unsafe_allow_html=True)

st.markdown('''
- Deparar os principais indicadores,
- Analisar e demonstrar o comportamento da evolução de cada indicador,
- Realizar comparação da evolução dos alunos por ano,
- Realizar comparação da evolução dos alunos por fase,
- Analisar o perfil individualmente de cada aluno,
- Analisar como se comportam as Pedras,
- Analisar e explicar evolução do ponto de virada,
- Demonstrar graficamente em quais momentos mais ocorre o ponto de virada,
- Analisar como o INDE se comporta. 
''')

st.subheader(':blue[Sobre a PASSOS MÁGICOS ]',divider='blue')

col, col1 = st.columns([4,1])
with col:
    st.markdown('''A <b><font color='blue'>Associação Passos Mágicos</b></font> é uma organização sem fins lucrativos que atua há 31 anos, focada na transformação da vida de crianças e jovens de baixa renda, oferecendo-lhes melhores oportunidades de vida. Fundada por Michelle Flues e Dimetri Ivanoff em 1992, a instituição começou suas atividades em orfanatos no município de Embu-Guaçu, São Paulo.''', unsafe_allow_html=True)

with col1:
    st.image('https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/Passos-magicos-icon-cor.png?raw=true', use_column_width=True )

tab1, tab2, tab3 = st.tabs(
    tabs=["Missão e Visão", "Programas e Atividades", "Impacto e Resultados"]
)

with tab1:
    st.markdown('''A missão da Passos Mágicos é transformar a vida de jovens e crianças, fornecendo ferramentas que os levem a melhores oportunidades de vida. A visão da organização é viver em um Brasil onde todas as crianças e jovens tenham iguais oportunidades para realizar seus sonhos e se tornem agentes transformadores de suas próprias vidas.''')

with tab2:
    st.markdown('''A Passos Mágicos oferece uma variedade de programas educacionais e de apoio, incluindo.''')
    st.markdown('''- <b>Educação de qualidade:</b> Acesso a ensino de alta qualidade para crianças e jovens.''', unsafe_allow_html=True)
    st.markdown('''- <b>Assistência psicológica e psicopedagógica:</b> Suporte emocional e educacional para ajudar no desenvolvimento integral dos alunos.''', unsafe_allow_html=True)
    st.markdown('''- <b>Ampliação da visão de mundo: </b>Projetos de intercâmbio e apadrinhamento que visam integrar os alunos a diferentes culturas e ambientes.''', unsafe_allow_html=True)
    st.markdown('''- <b>Campanhas de arrecadação:</b> Anualmente, são promovidas campanhas para arrecadar fundos e presentes para as crianças e adolescentes atendidos pela instituição.''', unsafe_allow_html=True)

with tab3:
    st.markdown('''Desde sua fundação, a Passos Mágicos tem expandido significativamente seu alcance e impacto. Em 2016, a organização formalizou-se como um projeto social e educacional, ampliando suas atividades para beneficiar mais jovens. Atualmente, a instituição atende centenas de crianças e adolescentes, oferecendo bolsas de estudo, suporte psicológico e oportunidades de intercâmbio.''')
