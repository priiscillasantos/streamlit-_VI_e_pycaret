<<<<<<< HEAD
# Projeto Final - Credit Scoring com PyCaret e Streamlit

Este projeto foi desenvolvido como parte do Módulo 38 do curso Profissão Cientista de Dados da EBAC.

O objetivo é construir um modelo de credit scoring para prever a probabilidade de inadimplência de clientes de cartão de crédito. O projeto contempla análise exploratória, tratamento de dados, regressão logística, pipeline com Scikit-learn, avaliação por métricas como Acurácia, AUC, Gini e KS, além de modelagem com PyCaret utilizando LightGBM.

## Arquivos do projeto

- `Mod38Projeto.ipynb`: notebook com o desenvolvimento completo do projeto.
- `app.py`: aplicação Streamlit para realizar a escoragem de novas bases.
- `model_final.pkl`: modelo final treinado e salvo em pickle.
- `requirements.txt`: bibliotecas necessárias para execução.
- `README.md`: documentação do projeto.

## Etapas desenvolvidas

1. Carregamento da base de dados.
2. Separação das safras de desenvolvimento e out of time.
3. Análise descritiva univariada.
4. Análise descritiva bivariada.
5. Tratamento de valores ausentes.
6. Tratamento de outliers.
7. Criação de variáveis dummies.
8. Treinamento de modelo de regressão logística.
9. Avaliação por Acurácia, AUC, Gini e KS.
10. Criação de pipeline com Scikit-learn.
11. Aplicação de PCA.
12. Modelagem com PyCaret utilizando LightGBM.
13. Salvamento do modelo treinado em pickle.
14. Desenvolvimento de aplicação Streamlit.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
=======
# Projeto Final - Módulo 38

Este projeto desenvolve um modelo de credit scoring para cartão de crédito e uma aplicação Streamlit para escoragem de bases em CSV.

## Arquivos principais

- `Mod38Projeto_resolvido.ipynb`: notebook completo com análise, modelagem, pipeline, PyCaret e salvamento do modelo.
- `app.py`: aplicação Streamlit para carregar um CSV e gerar o score dos clientes.
- `model_final.pkl`: arquivo gerado pelo notebook com o pipeline treinado.
- `requirements.txt`: bibliotecas necessárias para execução.

## Como executar

Primeiro, execute o notebook `Mod38Projeto_resolvido.ipynb` para gerar o arquivo `model_final.pkl`.

Depois, rode a aplicação:

```bash
streamlit run app.py
```

Na aplicação, envie um arquivo CSV com as variáveis do modelo e clique em **Escorar base**.

## Entrega

Suba no GitHub:

- notebook;
- `app.py`;
- `requirements.txt`;
- vídeo ou GIF da aplicação funcionando;
- README explicando como rodar o projeto.
>>>>>>> 0091b9f (Adiciona projeto final de credit scoring)
