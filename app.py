import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title='Credit Scoring - Módulo 38',
    page_icon='💳',
    layout='wide'
)


@st.cache_resource
def carregar_modelo(caminho_modelo: str = 'model_final.pkl'):
    caminho = Path(caminho_modelo)
    if not caminho.exists():
        st.error("Arquivo 'model_final.pkl' não encontrado. Coloque o modelo na mesma pasta do app.py.")
        st.stop()

    with open(caminho, 'rb') as arquivo:
        objeto = pickle.load(arquivo)

    return objeto


def preparar_base(base: pd.DataFrame, features: list) -> pd.DataFrame:
    # Copia a base para evitar alterar o arquivo original enviado pelo usuário.
    base_modelo = base.copy()

    # Remove colunas que podem aparecer no arquivo, mas não devem entrar na modelagem.
    colunas_remover = ['data_ref', 'index', 'mau']
    base_modelo = base_modelo.drop(columns=[col for col in colunas_remover if col in base_modelo.columns], errors='ignore')

    # Garante que todas as colunas esperadas pelo modelo existam.
    for col in features:
        if col not in base_modelo.columns:
            base_modelo[col] = pd.NA

    # Mantém a mesma ordem de colunas usada no treinamento.
    base_modelo = base_modelo[features]

    return base_modelo


st.title('Credit Scoring - Módulo 38')
st.write('Aplicação para escorar uma base de clientes usando o modelo treinado no projeto final.')

modelo_objeto = carregar_modelo()

if isinstance(modelo_objeto, dict):
    modelo = modelo_objeto['modelo']
    features = modelo_objeto['features']
    threshold = modelo_objeto.get('threshold', 0.5)
else:
    modelo = modelo_objeto
    features = None
    threshold = 0.5

st.sidebar.header('Configurações')
threshold = st.sidebar.slider('Ponto de corte', min_value=0.0, max_value=1.0, value=float(threshold), step=0.01)

arquivo_csv = st.file_uploader('Suba um arquivo CSV para escoragem', type=['csv'])

if arquivo_csv is not None:
    try:
        base = pd.read_csv(arquivo_csv)
    except UnicodeDecodeError:
        arquivo_csv.seek(0)
        base = pd.read_csv(arquivo_csv, encoding='latin1')
    except Exception as erro:
        st.error(f'Erro ao carregar o CSV: {erro}')
        st.stop()

    st.subheader('Prévia da base enviada')
    st.dataframe(base.head())

    st.write('Dimensão da base enviada:', base.shape)

    if features is None:
        st.warning('O modelo não trouxe a lista de features. A base será enviada diretamente ao pipeline carregado.')
        base_modelo = base.copy()
    else:
        base_modelo = preparar_base(base, features)

    if st.button('Escorar base'):
        try:
            prob_mau = modelo.predict_proba(base_modelo)[:, 1]
            pred_mau = (prob_mau >= threshold).astype(int)

            resultado = base.copy()
            resultado['score_mau'] = prob_mau
            resultado['classificacao_mau'] = pred_mau
            resultado['classificacao'] = resultado['classificacao_mau'].map({0: 'bom', 1: 'mau'})

            st.subheader('Resultado da escoragem')
            st.dataframe(resultado.head(50))

            col1, col2, col3 = st.columns(3)
            col1.metric('Quantidade de clientes', len(resultado))
            col2.metric('Taxa prevista de maus', f"{resultado['classificacao_mau'].mean() * 100:.2f}%")
            col3.metric('Score médio de mau', f"{resultado['score_mau'].mean():.4f}")

            csv_resultado = resultado.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label='Baixar resultado em CSV',
                data=csv_resultado,
                file_name='base_escorada.csv',
                mime='text/csv'
            )
        except Exception as erro:
            st.error(f'Erro ao escorar a base: {erro}')
else:
    st.info('Envie um arquivo CSV para iniciar a escoragem.')
