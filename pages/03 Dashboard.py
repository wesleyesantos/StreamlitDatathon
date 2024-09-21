import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout = "wide")
st.markdown("""<style>[data-testid="stSidebar"] {background: linear-gradient(180deg, #00c6ff, #0072ff);padding: 20px;}.icon-container {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<font face= Helvetica><b><u>Desenvolvedor</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Wesley E. dos Santos  
                - Fiap Postech - 3DTAT''')
    linkedin_url = "https://www.linkedin.com/in/wesleyesantos/"
    youtube_url = "https://www.youtube.com/@Wesley_santos-Excel_PowerBI"
    st.sidebar.markdown(f"""<div class="icon-container"><a href="{linkedin_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/linkedin.png?raw=true" width="30"/></a><a href="{youtube_url}" target="_blank"><img src="https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/youtube.png?raw=true" width="30"/></a></div>""", unsafe_allow_html=True)
    st.sidebar.image('https://github.com/wesleyesantos/StreamlitDatathon/blob/main/images/eu.jpg?raw=true', use_column_width=True)
    
st.subheader(':blue[Dashboard 🎯]',divider='blue')

st.markdown('''Aqui trago as métricas que gerei com a análise do relatório PEDE da PASSOS MÁGICOS, onde separei por 3 tópicos, sendo eles Evolução dos alunos, onde trago alguns pontos de vista quanto a alunos que foram melhores ou piores em certos perídos ou até mesmo que progrediram ou regrediram sua pedra no decorrer do tempo,  Indicadores de performance trago a análise particular de cada índice e a visão geral dos INDEs, e por terceiro trago a visão dos índices por aluno.''')

df = pd.read_csv("https://github.com/wesleyesantos/StreamlitDatathon/raw/refs/heads/main/assets/df_aluno.csv")
df['ANO'] = df['ANO'].astype(str) 


with st.container():
    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(tabs=["PEDRAS","Ponto de Virada", "Desempenho Acadêmico", "Desempenho Psicossocial", "Desempenho Psicopedagógica", "Análise por Aluno"])

    with tab0:
        st.markdown('''O esquema de classificação das pedras nos mostra os grupos de maios volumes de alunos, podendo ser vistos como níveis baixo, semi-intermediário, intermediário e avançado, abaixo deixo um gráfico pra demonstrar como ranking, a classificação das pedras, sendo Quartzo o nível mais baixo e Topázio que é o maior nível esses dois carregar as menores quantidades de alunos, e na sequência temos os níveis Ágata e Ametista como níveis intermediários que contém as maiores quantidades de alunos conforme visto no gráfico abaixo.''')
        dados = {'Tipo': ['Quartzo', 'Ágata', 'Ametista', 'Topázio'],'INDE_inicial': [2405, 5506, 6868, 8230],'INDE_final': [5506, 6868, 8230, 9294]}
        # Gráfico ranking pedras
        fig = go.Figure()
        for i, tipo in enumerate(dados['Tipo']):
            intervalo = 0 - dados['INDE_inicial'][i]
            text_label = f"<b>{tipo}</b><br>INDE inicial: {dados['INDE_inicial'][i]}<br>INDE final: {dados['INDE_final'][i]}"
            fig.add_trace(go.Bar(
                x=[tipo],y=[intervalo],base=dados['INDE_inicial'][i],
                name=tipo,text=text_label,textposition='inside',textfont=dict(color='white',size=14),
                marker=dict(color='rgba(55, 128, 191, 0.7)',line=dict(color='rgba(55, 128, 191, 1.0)',width=20))))
            fig.update_layout(width=800, height=650,xaxis=dict(showline=False,showgrid=False,zeroline=False,visible=False),
            yaxis=dict(showline=False,showgrid=False,zeroline=False,visible=False),
            barmode='overlay',showlegend=False)
        col, col0 = st.columns([1, 2])
        with col:
            st.plotly_chart(fig, use_container_width=True)
    
        # Gráfico Pedras por ano (INDE)
        df_pedra_aluno = df.groupby(['PEDRA', 'ANO']).size().reset_index(name='Contagem').sort_values(by='Contagem', ascending=False)
        ordem_pedras = ['Quartzo', 'Ágata', 'Ametista', 'Topázio']
        df_pedra_aluno['PEDRA'] = pd.Categorical(df_pedra_aluno['PEDRA'], categories=ordem_pedras, ordered=True)
        df_pedra_aluno = df_pedra_aluno.sort_values(by='PEDRA')
        fig1 = px.line(df_pedra_aluno, x='PEDRA', y='Contagem', color='ANO')
        fig1.update_layout(width=800, height=600, autosize=True, legend_title='Período', title='Quantidade de alunos por Pedra', xaxis_title='', yaxis_title='')
        with col0:
            st.plotly_chart(fig1, use_container_width=True)

        # Gráfico Volume de alunos por pedra e fase
        df_pedra_aluno2 = df.groupby(['PEDRA', 'FASE'])['NOME'].count().reset_index()
        st.markdown('''##### <font color='blue'>PEDRAS''', unsafe_allow_html=True)
        st.markdown('''.''', unsafe_allow_html=True)
        fig = px.box(df_pedra_aluno2, x='FASE', y='NOME', color='PEDRA', title='INDE detalhado por FASE e PEDRA', labels={'FASE': 'Fase', 'PEDRA': 'PEDRA'}, points="all")
        st.plotly_chart(fig, use_container_width=True)
        
        
    #Ponto de Virada
    with tab1:
        c0, c1, c2 = st.columns([1,1,5])
        df_pv = df[df['PONTO_VIRADA'] == 1]
        df_pv = df_pv.groupby("ANO")["PONTO_VIRADA"].count()

        with c0:
           st.metric(label='Total de Alunos PV 2020', value=df_pv.loc['2020'])

        with c1:
           st.metric(label='Total de Alunos (PV-2021)', value=df_pv.loc['2021'])

        with c2:
           st.metric(label='Total de Alunos (PV-2022)', value=df_pv.loc['2022'])

        st.markdown('''O ponto de virada se mostrou uma métrica bem instável ao analisarmos por fazer de cada ano, mas a partir daqui já podemos notar que as primeiras fases se sobressaem na quantidade de alunos que atingiram o mesmo, o que faz todo sentido uma vez que o PV é um passo mágico de quando o aluno está desenvolvendo de novas habilidades e os alunos mais novos tendem a aprender habilidades fundamentais.''')
        df_filtered = df[df['PONTO_VIRADA'] == 1]
        fig0 = px.histogram(df_filtered, x='FASE', color='ANO', barmode='group',color_discrete_sequence=["#5865F2","#07AFF2","#8D07F2", "#4007F2", "#071BF2","#0765F2"], labels={'FASE': 'Fase', 'count': 'Quantidade de Alunos'}, title='Quantidade de Alunos com Ponto de Virada por Fase e Ano')
        fig0.update_layout(xaxis_title='Fase', yaxis_title='Quantidade de Alunos que atingiram PV',legend_title_text='Ano', width=800, height=500)
        fig0.update_traces(texttemplate='%{y}', textposition='outside')
        st.plotly_chart(fig0, use_container_width=True)
        # Paleta de cores PASSOS MAGICOS - color_discrete_sequence=["#5865F2","#07AFF2","#8D07F2", "#4007F2", "#071BF2","#0765F2"],

    # PEDRAS    
    with tab2:
        st.markdown('''O gráfico abaixo traz um overview quando ao desenvolvimento acadêmico dos alunos por ano que são os indicadores IEG, IDA, IAN.''')
        df_grouped = df.groupby('ANO')[['IEG', 'IDA', 'IAN']].mean().reset_index()
        df_toshow = df_grouped.set_index('ANO')
        df_grouped['ANO'] = df_grouped['ANO'].astype(int)
        fig2 = go.Figure()
        for column in ['IEG', 'IDA', 'IAN']:
            fig2.add_trace(go.Scatter(x=df_grouped['ANO'], y=df_grouped[column], mode='lines', name=column))
        fig2.update_layout(title='Média dos indicadores de desempenho IEG, IDA e IAN por ano', xaxis_title='Ano', yaxis_title='Média', legend_title='Indicadores', height=600)
        fig2.update_xaxes(tickmode='linear', tick0=df_grouped['ANO'].min(), dtick=1)
        
        col1, col2 = st.columns([1,2])
        with col1:
            st.table(df_toshow)
            st.markdown('''- <b>IEG (Índice do Engajamento Global)</b>, ao analisar esse gráfico vi que teve uma queda considerável do ano de 2020 para 2021 e em 2022 houve uma grande superação demonstrando que em 2022 houve muito mais participação dos alunos.''', unsafe_allow_html=True)
            st.markdown('''- <b>IDA (Índice do Desenvolvimento Acadêmico)</b>, teve uma queda nos brusca nos dois primeiros anos apontados nessa análise, e no último ano houve uma recuperação mas não retornou ao seu nível normal do primeiro ano, demonstrando que em questão de notas, frequência e participação ainda temos um problema.''', unsafe_allow_html=True)
            st.markdown('''- <b>IAN (Índice do Acompanhamento Nutricional)</b>, Teve uma queda constante não demonstrando nenhum pico de retorno a seus níveis normais de 2020 pra cá, demonstrando assim um problema com nutrição e bem estar dos alunos.''', unsafe_allow_html=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)
    
        st.divider()
        st.markdown('''##### <font color='blue'>IEG''', unsafe_allow_html=True)
        st.markdown('''Observando o gráfico abaixo podemos ver que ao retirar os outliers o IEG se mantém de 8 pra cima com exceção a algumas situações específicas como nas fases 2, 3 e 6 no ano de 2021, com isso seria interessar a escola verificar os eventos em 2021 que atrapalharam o engajamento dos alunos para realizar um trabalho preventivo em anos futuros uma vez que os níveis se regularizam no ano seguinte.''', unsafe_allow_html=True)
        fig3 = px.box(df, x='FASE', y='IEG', color='ANO', title='IEG detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IEG': 'IEG'}, points="all")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown('''##### <font color='blue'>IDA''', unsafe_allow_html=True)
        st.markdown('''O desenvolvimento acadêmico varia bastante, tendo um pico ali inicialmente na fase 0 ele segue com a mediana entre 5 e 7 no geral de todas as fases.''', unsafe_allow_html=True)
        fig4 = px.box(df, x='FASE', y='IDA', color='ANO', title='IDA detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IDA': 'IDA'}, points="all")
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown('''##### <font color='blue'>IAN''', unsafe_allow_html=True)
        st.markdown('''O acompanhamento nutricional mesmo quebrado por fase não demonstrou melhoras, sendo um indicador para entrar como alerta para melhor acompanhamento e desenvolvimento de questões alimentares dos alunos e seu bem estar.''', unsafe_allow_html=True)
        fig5 = px.box(df, x='FASE', y='IAN', color='ANO', title='IAN detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IAN': 'IAN'}, points="all")
        st.plotly_chart(fig5, use_container_width=True)
    # Desempenho Acadêmico
    with tab3:
        st.markdown('''O gráfico abaixo traz um overview quando ao desenvolvimento Psicossocial dos alunos por ano que são os indicadores IAA e IPS.''')
        df_grouped2 = df.groupby('ANO')[['IAA', 'IPS']].mean().reset_index()
        df_toshow = df_grouped2.set_index('ANO')
        df_grouped2['ANO'] = df_grouped2['ANO'].astype(int)
        fig3 = go.Figure()
        for column in ['IAA', 'IPS']:
            fig3.add_trace(go.Scatter(x=df_grouped2['ANO'], y=df_grouped2[column], mode='lines', name=column))
        fig3.update_layout(title='Média dos indicadores de desempenho IAA e IPS por ano', xaxis_title='Ano', yaxis_title='Média', legend_title='Indicadores', height=600)
        fig3.update_xaxes(tickmode='linear', tick0=df_grouped2['ANO'].min(), dtick=1)
        col3, col4 = st.columns([1,2])
        with col3:
            st.table(df_toshow)
            st.markdown('''- <b>IAA (Índice de Atendimento e Acompanhamento)</b>, em questão de atendimento e acompanhamento dos alunos temos um índice bem estável, mesmo com uma queda mínima no decoorer desses 3 últimos anos. ''', unsafe_allow_html=True)
            st.markdown('''- <b>IPS (Índice de Participação Social)</b>, o estimulo a participação de projetos comunitários tem crescido aos poucos, mas é um ponto positivo mostrando que a passos mágicos tem incentivado e promovido a criação mais cidadãos de bem.''', unsafe_allow_html=True)
        with col4:
            st.plotly_chart(fig3, use_container_width=True)
    
        st.divider()
        st.markdown('''##### <font color='blue'>IAA''', unsafe_allow_html=True)
        st.markdown('''Os níveis do IAA são ótimos mesmo quando os abrimos por fases, somente na fase 6 que tem uma variação que é importante atuar mais afundo nas turmas, alunos ou até acontecimentos específicos que levaram o indicador a ter essa variação.''', unsafe_allow_html=True)
        fig4 = px.box(df, x='FASE', y='IAA', color='ANO', title='IAA detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IAA': 'IAA'}, points="all")
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown('''##### <font color='blue'>IPS''', unsafe_allow_html=True)
        st.markdown('''O IPS tem uma mediana melhor do segregada do que quando tinhamos avaliado a mediana geral do indicador anteriormente, agora podemos ver que a mediana segue em 7.5 na maior parte das fases, demonstrando que os alunos da Passos mágicos tem participado ativamento em atividades comunitárias.''', unsafe_allow_html=True)
        fig5 = px.box(df, x='FASE', y='IPS', color='ANO', title='IPS detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IPS': 'IPS'}, points="all")
        st.plotly_chart(fig5, use_container_width=True)
    # Desempenho Psicossocial
    with tab4:
        st.markdown('''O gráfico abaixo traz um overview quando ao desenvolvimento Psicopedagógico dos alunos por ano que são os indicadores IPP e IPV.''')
        df_grouped3 = df.groupby('ANO')[['IPP', 'IPV']].mean().reset_index()
        df_toshow = df_grouped3.set_index('ANO')
        df_grouped2['ANO'] = df_grouped3['ANO'].astype(int)
        fig4 = go.Figure()
        for column in ['IPP', 'IPV']:
            fig4.add_trace(go.Scatter(x=df_grouped3['ANO'], y=df_grouped3[column], mode='lines', name=column))
        fig4.update_layout(title='Média dos indicadores de desempenho IPP e IPV por ano', xaxis_title='Ano', yaxis_title='Média', legend_title='Indicadores', height=600)
        fig4.update_xaxes(tickmode='linear', tick0=df_grouped3['ANO'].min(), dtick=1)
        col5, col6 = st.columns([1,2])
        with col5:
            st.table(df_toshow)
            st.markdown('''- <b>IPP (Índice de Progresso Pessoal)</b>, esse índice é muito importante apesar de um resultado não muito estável quando olhamos uma média de todos os alunos, aqui podemos considerar que tem alunos novos que ainda não desenvolveram muito suas skills sociais e resiliência em algum cenário que necessita de resolver problemas mais complexos.''', unsafe_allow_html=True)
            st.markdown('''- <b>IPV (Índice de Permanência e Valorização)</b>, esse índice é um feedback e o retorno está muito bom, ele se manteve bem estável ali na casa do 7,2 a 7,4.''', unsafe_allow_html=True)
        with col6:
            st.plotly_chart(fig4, use_container_width=True)

        st.divider()
        st.markdown('''##### <font color='blue'>IPP''', unsafe_allow_html=True)
        st.markdown('''O progresso pessoal dos alunos teve uma queda considerável no ano de 2022 com exceção a fase 6, o indicador teve uma pequena estabilidade quando comparado os anos de 2020 e 2021, tendo progressos na maior parte das fases e uma leve queda nas fases 3, 4 e 5.''', unsafe_allow_html=True)
        fig4 = px.box(df, x='FASE', y='IPP', color='ANO', title='IPP detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IPP': 'IPP'}, points="all")
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown('''##### <font color='blue'>IPV''', unsafe_allow_html=True)
        st.markdown('''Os medidores de presença dos alunos e realização de provas e atividades segue com medias entre 6.56 e 7.5, no geral variando acima da casa dos 7, só a terceira fase que deixou um gap nesse indicador.''', unsafe_allow_html=True)
        fig5 = px.box(df, x='FASE', y='IPV', color='ANO', title='IPV detalhado por Fase e Ano', labels={'FASE': 'Fase', 'IPV': 'IPV'}, points="all")
        st.plotly_chart(fig5, use_container_width=True)
    # Desempenho Psicopedagógica
    with tab5:
        #FILTROS
        if 'aluno_selecionado' not in st.session_state:
            st.session_state['aluno_selecionado'] = []

        if 'ano_selecionado' not in st.session_state:
            st.session_state['ano_selecionado'] = None

        if 'turma_selecionada' not in st.session_state:
            st.session_state['turma_selecionada'] = None

        if 'fase_selecionada' not in st.session_state:
            st.session_state['fase_selecionada'] = None

        if 'comparador_inde' not in st.session_state:
            st.session_state['comparador_inde'] = 'Nenhum'

        if 'valor_inde' not in st.session_state:
            st.session_state['valor_inde'] = 0


        df_aluno = df.set_index('NOME')
        
        col7, col8= st.columns([3,1])
        with col7:
            aluno_selecionado = st.multiselect('Selecione um ou mais alunos', df_aluno.index.unique(), key='aluno_selecionado')
            
        with col8:
            anos_disponiveis = df['ANO'].unique()
            ano_selecionado = st.selectbox('Selecione o ano', [None] + list(anos_disponiveis), key='ano_selecionado')

        col9, col10, col11, col12 = st.columns(4)
        with col9:
            turmas_disponiveis = df['TURMA'].unique()
            turma_selecionada = st.selectbox('Selecione a turma', [None] + list(turmas_disponiveis), key='turma_selecionada')

        with col10:
            fases_disponiveis = df['FASE'].unique()
            fase_selecionada = st.selectbox('Selecione a fase', [None] + list(fases_disponiveis), key='fase_selecionada')

        with col11:
            comparador_inde = st.selectbox('Filtrar INDE por', ['Nenhum', 'Maior que', 'Menor que'], key='comparador_inde')

        with col12:
            valor_inde = st.number_input('Digite o valor para o INDE', step=1, key='valor_inde')

        if st.button('Limpar Filtros', type="primary"):
            st.session_state['aluno_selecionado'] = []
            st.session_state['ano_selecionado'] = None
            st.session_state['turma_selecionada'] = None
            st.session_state['fase_selecionada'] = None
            st.session_state['comparador_inde'] = 'Nenhum'
            st.session_state['valor_inde'] = 0

        df_filtrado = df_aluno.copy()
        df_filtrado['PONTO_VIRADA'] = df_filtrado['PONTO_VIRADA'].replace({0: 'Não', 1: 'Sim'})

        if aluno_selecionado:
            df_filtrado = df_filtrado[df_filtrado.index.isin(aluno_selecionado)]

        if ano_selecionado:
            df_filtrado = df_filtrado[df_filtrado['ANO'] == ano_selecionado]

        if turma_selecionada:
            df_filtrado = df_filtrado[df_filtrado['TURMA'] == turma_selecionada]

        if fase_selecionada:
            df_filtrado = df_filtrado[df_filtrado['FASE'] == fase_selecionada]

        if comparador_inde == 'Maior que':
            df_filtrado = df_filtrado[df_filtrado['INDE'] > valor_inde]
        elif comparador_inde == 'Menor que':
            df_filtrado = df_filtrado[df_filtrado['INDE'] < valor_inde]

        st.write('Resultado dos filtros:')
        st.table(df_filtrado)

