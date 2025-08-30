import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.set_page_config(page_title="Datathon Análise Exploratória",  page_icon="💎",layout = "wide")
st.markdown("""<style>[data-testid="stSidebar"] {background: linear-gradient(180deg, #00c6ff, #0072ff);padding: 20px;}.icon-container {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<font face= Helvetica><b><u>Desenvolvedor</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Wesley E. dos Santos  
                - Fiap Postech - 3DTAT''')
    linkedin_url = "https://www.linkedin.com/in/wesleyesantos/"
    youtube_url = "https://www.youtube.com/@Wesley_santos-Excel_PowerBI"
    github_url = "https://github.com/wesleyesantos/StreamlitDatathon"
    st.sidebar.markdown(f"""<div class="icon-container">
    <a href="{linkedin_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/linkedin.png?raw=true" width="30"/></a>
    <a href="{youtube_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/youtube.png?raw=true" width="30"/></a>
    <a href="{github_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/github.png?raw=true" width="30"/></a>
    </div>""", unsafe_allow_html=True)
    st.sidebar.image('https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/eu.jpg?raw=true')

url = "https://github.com/wesleyesantos/Postech-Datathon/raw/main/PEDE_PASSOS_DATASET_FIAP.csv"
url1 = "https://github.com/4ca63473-734d-4d8c-8181-9635c1837ddc"
response = requests.get(url)
csv_data = response.content
response1 = requests.get(url1)
file_data = response1.content


st.subheader(':blue[Análise Exploratória 📌]', divider='blue')

st.markdown('''A análise Exploratória do projeto foi realizada com a base <b><font color='blue'>PEDE (Pesquisa Extensiva do Desenvolvimento Educacional)</b></font> da Passos Mágicos e foi disponibilizada toda documentação explicando como foram criadas cada índice e métricas já existentes. A PASSOS MÁGICOS utiliza uma métrica chamada <b><font color='blue'>INDE (Índice Nacional de Desenvolvimento Educacional)</b></font> para avaliar os alunos essa métrica é composta por alguns indicadores que são separados em 3 dimensões principais onde avaliam vários critérios como adequação de nível, desempenho acadêmico, engajamento, autoavaliação, aspectos psicossociais e psicopedagógicos, essas dimensões estão divididas conforme abaixo e cada uma delas trazem os seguintes indicadores:''', unsafe_allow_html=True)
st.markdown('''- Dimensão acadêmica: Com os indicadores IEG, IDA e IAN''',  unsafe_allow_html=True)
st.markdown('''- Dimensão psicossocial: Com os indicadores IAA e IPS''',  unsafe_allow_html=True)
st.markdown('''- Dimensão psicopedagógica: Com os indicadores IPP e IPV''',  unsafe_allow_html=True)

st.markdown('''Quanto ao <b><font color='blue'>INDE </b></font> geral tem uma média de 7,07, obtendo uma variação bem grande entre o mínimo de 2,46 e máximo de 9,71; ao realizar a análise por ano podemos observar que tem um aumento na quantidade de alunos e os níveis do INDE caem, nos trazendo o desafio de começar a segregar essa informação para buscar o gap.''', unsafe_allow_html=True) 

st.markdown('''O indicador <b><font color='blue'>IDA</b></font> se sobresai como o mais baixo de todos os anos que é um indicador de participação dos projetos e atividades pedagógicas, e devido a esse defasamento o maior indicador que temos é o <b><font color='blue'>IAA</b></font> que é o indice de atenção psicológica e psicopedagógica aos alunos.''', unsafe_allow_html=True)

st.subheader(':blue[Indicadores 📈]', divider='blue')

tab0,tab,tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tabs=['INDE','Pedras','IEG', 'IDA', 'IAN', 'IAA', 'IPS', 'IPP', 'IPV', 'Ponto de Virada'])

with tab0:
    st.markdown('''O <b><font color='blue'>Índice de Desenvolvimento Educacional (INDE)</b></font> da Associação Passos Mágicos é uma métrica utilizada para avaliar o progresso educacional dos alunos atendidos pela instituição. Esse índice é calculado com base em diversos fatores, incluindo:''', unsafe_allow_html=True)    
    st.markdown('''- <b><font color='blue'>Desempenho Acadêmico:</b></font> Avaliação das notas dos alunos em disciplinas como Português, Matemática e Inglês.''', unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Apoio Psicológico e Psicopedagógico:</b></font> Impacto das intervenções psicológicas e psicopedagógicas no desenvolvimento dos alunos.''', unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Participação em Atividades Extracurriculares:</b></font> Envolvimento dos alunos em atividades que ampliam sua visão de mundo, como intercâmbios e projetos culturais.''', unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Evolução ao Longo do Ano:</b></font> Comparação das notas e do desenvolvimento dos alunos entre o início e o final do ano letivo.''', unsafe_allow_html=True)
    st.markdown('''O INDE é uma ferramenta crucial para a Passos Mágicos, pois permite monitorar e ajustar suas estratégias educacionais, garantindo que cada aluno receba o suporte necessário para alcançar seu pleno potencial.''')

with tab:
    st.markdown('''As <b><font color='blue'>Pedras</b></font> podem ser definidas como o quanto os alunos estão pontuando, então ele entra num esquema de classificação, o que traz mais clareza na análise e atenção para o desenvolvimento de cada aluno e também dá uma visão mais competitiva aos alunos, porém eles irão almejar as melhores classificações. Até o último relatório PEDE tinhamos 4 pedras que são:''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Quartzo:</b></font> Alunos com INDE entre <b><font color='blue'>2,405 a 5,506</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Ágata:</b></font> Alunos com INDE entre <b><font color='blue'>5,506 a 6,868</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Ametista:</b></font> Alunos com INDE entre <b><font color='blue'>6,868 a 8,230</b></font>.''',unsafe_allow_html=True)
    st.markdown('''- <b><font color='blue'>Topázio:</b></font> Alunos com INDE entre <b><font color='blue'>8,230 a 9,294</b></font>.''',unsafe_allow_html=True)
with tab1:
    st.markdown('''###### <font color='blue'>IEG (Índice de Engajamento Global)''',unsafe_allow_html=True )
    st.markdown('''Avalia o nível de envolvimento dos alunos em atividades extracurriculares e programas de intercâmbio. Este índice é importante para entender como as experiências fora da sala de aula contribuem para o desenvolvimento pessoal e acadêmico dos alunos.''')

with tab2:
    st.markdown('''###### <font color='blue'>IDA (Índice de Desenvolvimento Acadêmico)''',unsafe_allow_html=True)
    st.markdown('''Mede o progresso acadêmico dos alunos, considerando notas, frequência escolar e participação em atividades educacionais. Este índice ajuda a identificar áreas que necessitam de melhorias e a eficácia das intervenções pedagógicas.''')

with tab3:
    st.markdown('''######  <font color='blue'>IAN (Índice de Aproveitamento Nutricional)''',unsafe_allow_html=True)
    st.markdown('''Avalia a qualidade da alimentação fornecida às crianças e jovens, medindo o impacto da nutrição no desempenho escolar e no bem-estar geral dos alunos.''')

with tab4:
    st.markdown('''######  <font color='blue'>IAA (Índice de Atendimento e Acompanhamento)''',unsafe_allow_html=True)
    st.markdown('''Mede a qualidade e a frequência do atendimento psicológico e psicopedagógico oferecido aos alunos. Este índice é crucial para garantir que os alunos recebam o suporte necessário para superar desafios emocionais e acadêmicos.''')

with tab5:
    st.markdown('''######  <font color='blue'>IPS (Índice de Participação Social)''',unsafe_allow_html=True)
    st.markdown('''Avalia o envolvimento dos alunos em atividades comunitárias e projetos sociais. Este índice ajuda a medir o impacto dos programas da Passos Mágicos na formação de cidadãos conscientes e ativos na sociedade.''')

with tab6:
    st.markdown('''###### <font color='blue'>IPP (Índice de Progresso Pessoal)''',unsafe_allow_html=True)
    st.markdown('''Mede o desenvolvimento pessoal dos alunos, considerando aspectos como autoestima, habilidades sociais e resiliência. Este índice é importante para avaliar o impacto das intervenções da Passos Mágicos no crescimento pessoal dos alunos.''')

with tab7:
    st.markdown('''###### <font color='blue'>IPV (Índice de Permanência e Valorização)''',unsafe_allow_html=True)
    st.markdown('''Avalia a taxa de retenção dos alunos nos programas da Passos Mágicos e a valorização dos mesmos pelos beneficiários e suas famílias. Este índice é fundamental para entender a satisfação e o comprometimento dos alunos com os programas oferecidos.''')

st.subheader(':blue[PEDE (Pesquisa Extensiva do Desenvolvimento Educacional) 🗃️]', divider='blue')

tab9, tab10 = st.tabs(tabs=['Base (Conceito e download)', 'Estrutura e Dicionário'])
with tab9:
    st.markdown('''A base <b><font color='blue'>PEDE</font></b> foi disponibilizada a base completa referenciando as colunas por anos, sendo que os anos disponibilizados para esse trabalho foram os anos 2020, 2021 e 2022, como tiveram alguns alunos que iniciaram no decorrer desse período a base exigiu uma atenção na realização de análise e algumas limpezas que foram cruciais para seguir com a análise exploratória.''', unsafe_allow_html=True)
    st.download_button(label="Baixar Base PEDE (csv)",data=csv_data,file_name="PEDE_PASSOS_DATASET_FIAP.csv",mime="text/csv")
with tab10:
    st.markdown('''###### <font color='blue'>Estrutura da Base''',unsafe_allow_html=True)
    st.download_button(label="Dicionário da base PEDE",data=file_data,file_name="Dicionário dados PEDE.pdf",mime="application/pdf")

    st.markdown('''###### <font color='blue'>Estrutura da Base''',unsafe_allow_html=True)
    data_dict = {
    "INSTITUICAO_ENSINO_ALUNO_2020": "Mostra instituição de Ensino do Aluno em 2020",
    "NOME": "Nome do Aluno (dados estão anonimizados)",
    "IDADE_ALUNO_2020": "Idade do Aluno em 2020",
    "PEDRA_2020": "Classificação do Aluno baseado no número do INDE (2020), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294",
    "IAA_2020": "Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2020",
    "IEG_2020": "Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2020",
    "IPS_2020": "Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2020",
    "IDA_2020": "Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2020",
    "IPP_2020": "Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2020",
    "IPV_2020": "Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2020",
    "IAN_2020": "Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2020",
    "INDE_2020": "Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2020.",
    "DESTAQUE_IEG_2020": "Observações dos Avaliadores Sobre o Aluno referente ao 'Indicador de Engajamento' em 2020",
    "DESTAQUE_IDA_2020": "Observações dos Avaliadores Sobre o Aluno referente ao 'Indicador de Aprendizagem' em 2020",
    "DESTAQUE_IPV_2020": "Observações dos Avaliadores Sobre o Aluno referente ao 'Indicador de Ponto de Virada' em 2020",
    "PONTO_VIRADA_2020": "Campo do Tipo Booleano que sinaliza se o Aluno atingiu o 'Ponto de Virada' em 2020",
    "PEDRA_2021": "Classificação do Aluno baseado no número do INDE (2021), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294",
    "IAA_2021": "Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2021",
    "IEG_2021": "Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2021",
    "IPS_2021": "Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2021",
    "IDA_2021": "Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2021",
    "IPP_2021": "Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2021",
    "IPV_2021": "Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2021",
    "IAN_2021": "Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2021",
    "INDE_2021": "Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2021.",
    "REC_EQUIPE_1_2021": "Recomendação: da Equipe de Avalição: 1 em 2021",
    "REC_EQUIPE_2_2021": "Recomendação: da Equipe de Avalição: 2 em 2021",
    "REC_EQUIPE_3_2021": "Recomendação: da Equipe de Avalição: 3 em 2021",
    "REC_EQUIPE_4_2021": "Recomendação: da Equipe de Avalição: 4 em 2021",
    "REC_PSICO_2021": "Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2021",
    "PONTO_VIRADA_2021": "Campo do Tipo Booleano que sinaliza se o Aluno atingiu o 'Ponto de Virada' em 2021",
    "PEDRA_2022": "Classificação do Aluno baseado no número do INDE (2022), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294",
    "IAA_2022": "Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2022",
    "IEG_2022": "Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2022",
    "IPS_2022": "Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2022",
    "IDA_2022": "Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2022",
    "IPP_2022": "Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2022",
    "IPV_2022": "Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2022",
    "IAN_2022": "Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2022",
    "INDE_2022": "Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2022.",
    "REC_PSICO_2022": "Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2022",
    "REC_AVA_1_2022": "Recomendação da Equipe de Avalição 1 em 2022",
    "REC_AVAL_2_2022": "Recomendação da Equipe de Avalição: 2 em 2022",
    "REC_AVAL_3_2022": "Recomendação da Equipe de Avalição: 3 em 2022",
    "REC_AVAL_4_2022": "Recomendação da Equipe de Avalição: 4 em 2022",
    "DESTAQUE_IEG_2022": "Observações dos Mestres Sobre o Aluno referente ao 'Indicador de Engajamento' em 2022",
    "DESTAQUE_IDA_2022": "Observações dos Mestres Sobre o Aluno referente ao 'Indicador de Aprendizagem' em 2022",
    "DESTAQUE_IPV_2022": "Observações dos Mestres Sobre o Aluno referente ao 'Indicador de Ponto de Virada' em 2022",
    "PONTO_VIRADA_2022": "Campo do Tipo Booleano que sinaliza se o Aluno atingiu o 'Ponto de Virada' em 2022",
    "INDICADO_BOLSA_2022": "Campo do Tipo Booleano que sinaliza se o Aluno foi indicado para alguma Bolsa no Ano de 2022"
    }
    df = pd.DataFrame(list(data_dict.items()), columns=["Nome da Coluna", "Detalhamento dos dados"])

    st.markdown('''A base contém 50 colunas referente ao período de 2020 a 2022, com colunas adicionais no decorrer dos anos.''', unsafe_allow_html=True)
    st.table(df)

with tab8:
    st.markdown(''' O Ponto de virada indica que o aluno atingiu um passo mágico, é a conquista de uma habilidade fundamental, é medido através das notas, avaliações e outros dados, e demonstra que o aluno teve um grande progresso, essa evolução o ajudará a enfrentar vários desafios que encontrará pela frente, assim como:''' )
    st.markdown('''
    - Os alunos poderão superar dificuldades em matérias específicas e melhorar seu desempenho acadêmico,
    - Isso pode incluir avanços em leitura, matemática, ciências e outras áreas,
    - O ponto de virada traz consigo uma sensação de realização e confiança,
    - Os alunos se sentirão mais capazes e confiantes em suas habilidades,
    - Eles desenvolverão habilidades de comunicação, resolução de conflitos, empatia e trabalho em equipe,
    - Isso os ajudará a lidar com situações sociais e emocionais,
    - O ponto de virada também envolve uma ampliação da visão de mundo,
    - Os alunos estarão mais abertos a diferentes culturas, perspectivas e oportunidades,
    - Os alunos serão incentivados a assumir o protagonismo em suas vidas,
    - Eles tomarão decisões mais conscientes e terão maior autonomia,
    - O ponto de virada ensina a importância da persistência e da resiliência,
    - Os alunos saberão que podem superar obstáculos com esforço contínuo.
    ''')
