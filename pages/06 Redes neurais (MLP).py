import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Datathon Modelo",  page_icon="💎",layout = "wide")
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

st.subheader(':blue[Machine Learn - Redes Neurais (MLP) 🤖]', divider='blue')
st.markdown('''Realizei o modelo <b><font color='blue'>MLP (MultiLayer Perceptron)</b></font> onde puxei a previsão da nota de 2023. Foram realizadas as seguintes etapas para realização do modelo.''', unsafe_allow_html=True)
st.markdown('''
            1. Upload de dados,<br>
        2. Definir variáveis de entrada (X) e variável de saída (y),<br>
        3. Dividir os dados em conjunto de treino e teste,<br>
        4. Normalizar os dados (recomendado para redes neurais),<br>
        5. Criar o modelo de rede neural (MLP),    
            a. Camada de entrada e primeira camada oculta,<br>
            b. Segunda camada oculta,<br>
            c. Camada de saída para prever a nota,<br>
        6. Compilar o modelo,<br>
        7. Treinar o modelo,<br>
        8. Avaliar o modelo no conjunto de teste,<br>
        9. Fazer previsões.''', unsafe_allow_html=True)
        
#Upload de dados
df = pd.read_csv('https://github.com/wesleyesantos/StreamlitDatathon/raw/refs/heads/main/assets/df_aluno.csv')

with st.container():
    # Definir variáveis de entrada (X) e variável de saída (y)
    X = df[['IEG','IAN', 'IAA', 'IPS','IDA','IPP', 'IPV']]  # Variáveis preditoras
    y = df['INDE']  # Variável de saída (nota)

    # Dividir os dados em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizar os dados (recomendado para redes neurais)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Criar o modelo de rede neural (MLP)
    model = Sequential()
        # Camada de entrada e primeira camada oculta
    model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
        # Segunda camada oculta
    model.add(Dense(units=32, activation='relu'))
        # Camada de saída para prever a nota
    model.add(Dense(units=1, activation='linear'))

    # Compilar o modelo
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Treinar o modelo
    model.fit(X_train_scaled, y_train, epochs=100, batch_size=10, verbose=1)

    # Avaliar o modelo no conjunto de teste
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error no conjunto de teste: {mse}')

    # Fazer previsões
    novos_dados = df[['IEG','IAN', 'IAA', 'IPS','IDA','IPP', 'IPV']]  # Exemplo de novos dados (aluno em 2023)
    novos_dados_scaled = scaler.transform(novos_dados)
    predicao = model.predict(novos_dados_scaled)
    print(f'Previsão de nota: {predicao[0][0]:.2f}')

    y_test = np.array(y_test).flatten()
    y_pred = np.array(y_pred).flatten() 

    t0, t1, t2, t3, t4, t5, t6 = st.tabs(tabs=['Real x Pred', 'Errors', 'Residuals', 'Learning Curve', 'Pred Errors', 'Correlation', 'Feature Importance' ])

    with t0:
        st.markdown('''Esse gráfico permite comparar as previsões do modelo diretamente com os valores reais. Se o modelo for preciso, os pontos devem se alinhar em torno da linha y = x. Os pontos que estão mais próximos da linha diagonal indicam boas previsões.''')
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=y_test, y=y_pred.flatten(), mode='markers', name='Previsões', marker=dict(color='blue')))
        fig.add_trace(go.Scatter(x=[min(y_test), max(y_test)], y=[min(y_test), max(y_test)], mode='lines', name='Linha de referência', line=dict(color='red', dash='dash')))
        fig.update_layout(title='Previsões vs. Valores Reais', xaxis_title='Valores Reais', yaxis_title='Previsões', showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with t1:
        st.markdown('''O histograma dos erros (ou resíduos) mostra a distribuição dos erros de previsão (diferença entre valores reais e previstos). Idealmente, a distribuição deve ser próxima de uma distribuição normal centrada em zero, o que indica que os erros são pequenos e simetricamente distribuídos. Como o modelo está concentrando os valores ao redor de zero e simetricamente distribuidos, podemos constatar que o modelo está fazendo previsões consistentes.''')
        residuals = y_test - y_pred
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=residuals, nbinsx=20, marker_color='blue', opacity=0.75))
        fig.update_layout(title='Distribuição dos Erros de Previsão (Resíduos)', xaxis_title='Erro de Previsão (Resíduos)', yaxis_title='Frequência', bargap=0.2)
        st.plotly_chart(fig, use_container_width=True)

    with t2:
        st.markdown('''Um gráfico de resíduos compara os erros de previsão (resíduos) com os valores reais. Ele ajuda a identificar padrões sistemáticos de erro, como erros de previsão maiores em determinados intervalos de valores reais. Assim como nos erros os resíduos bem distribuidos ao redor do valor zero mosstra que esse é um bom modelo.''')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=y_pred, y=residuals, mode='markers', name='Resíduos', marker=dict(color='blue')))
        fig.add_trace(go.Scatter(x=[min(y_pred), max(y_pred)], y=[0, 0], mode='lines', name='Linha de referência (y=0)', line=dict(color='red', dash='dash')))
        fig.update_layout(title='Gráfico de Resíduos', xaxis_title='Previsões', yaxis_title='Resíduos', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with t3:
        st.markdown('''Mostra o desempenho do modelo ao longo das épocas de treinamento. A curva de aprendizado pode ser útil para verificar se o modelo está se ajustando aos dados adequadamente (sem underfitting ou overfitting).''')
        history = model.fit(X_train_scaled, y_train, validation_data=(X_test_scaled, y_test), epochs=100, verbose=0)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(1, len(history.history['loss']) + 1)), y=history.history['loss'], mode='lines+markers', name='Perda no Treinamento', line=dict(color='blue'),  marker=dict(color='blue')))
        fig.add_trace(go.Scatter(x=list(range(1, len(history.history['val_loss']) + 1)), y=history.history['val_loss'], mode='lines+markers', name='Perda na Validação', line=dict(color='red'), marker=dict(color='red')))
        fig.update_layout(title='Curva de Aprendizado', xaxis_title='Épocas', yaxis_title='Erro Quadrático Médio (MSE)', showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    with t4:
        st.markdown('''O boxplot dos resíduos mostra a distribuição dos erros de previsão, destacando os outliers, a mediana e o intervalo interquartil dos resíduos.O boxplot nos ajuda a identificar possíveis outliers nas previsões do modelo, que indicam alguns casos onde o modelo não se saiu bem.''')
        fig = go.Figure()
        fig.add_trace(go.Box(y=residuals, name='Resíduos', marker_color='blue'))
        fig.update_layout(title='Boxplot dos Erros de Previsão (Resíduos)', yaxis_title='Erro de Previsão (Resíduos)', xaxis_title='', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with t5:
        st.markdown('''Visualiza a correlação entre os recursos (variáveis independentes) e a variável alvo (notas). Esse gráfico pode ajudar a entender a relação entre os dados históricos e o desempenho acadêmico. Altos valores de correlação entre as variáveis independentes e a variável alvo indicam que essas variáveis são bons preditores do desempenho acadêmico.''')
        corr = df[['IEG','IAN', 'IAA', 'IPS','IDA','IPP', 'IPV', 'INDE']]
        corr_matrix = corr.corr()
        fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns, colorscale='Viridis', colorbar=dict(title='Correlação'), zmin=-1, zmax=1))
        fig.update_layout(title='Matriz de Correlação entre as Variáveis', xaxis_title='Variáveis', yaxis_title='Variáveis',xaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns), yaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns))
        st.plotly_chart(fig, use_container_width=True)
    
    with t6:
        st.markdown('''Podemos visualizar os pesos das primeiras camadas do MLP para obter uma ideia da importância das características. Isso é  útil para redes mais simples, mas geralmente não é interpretável em redes mais profundas.''')
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        importances = model.feature_importances_
        indices = np.argsort(importances)   
        fig = go.Figure()
        fig.add_trace(go.Bar(y=[X.columns[i] for i in indices], x=importances[indices], orientation='h', marker=dict(color='blue')))
        fig.update_layout(title='Importância das Características', xaxis_title='Importância Relativa', yaxis_title='Características', yaxis=dict(tickvals=[X.columns[i] for i in indices]),   showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
