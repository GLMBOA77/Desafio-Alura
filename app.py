# --- TRATAMENTO DOS DADOS DIA 01 ---
# Carregar as bases de dados e concatenar

#Importando as bibliotecas que vou utilizar
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregamento dos dados
dados_2010_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20101.csv?raw=true')
dados_2010_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20102.csv?raw=true')
dados_2011_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20111.csv?raw=true')
dados_2011_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20112.csv?raw=true')
dados_2012_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20121.csv?raw=true')
dados_2012_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20122.csv?raw=true')
dados_2013_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20131.csv?raw=true')
dados_2013_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20132.csv?raw=true')
dados_2014_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20141.csv?raw=true')
dados_2014_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20142.csv?raw=true')
dados_2015_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20151.csv?raw=true')
dados_2015_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20152.csv?raw=true')
dados_2016_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20161.csv?raw=true')
dados_2016_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20162.csv?raw=true')
dados_2017_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20171.csv?raw=true')
dados_2017_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20172.csv?raw=true')
dados_2018_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20181.csv?raw=true')
dados_2018_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20182.csv?raw=true')
dados_2019_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20191.csv?raw=true')
dados_2019_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20192.csv?raw=true')
dados_2020_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20201.csv?raw=true')

#Concatenando as bases de dados
emprestimos_biblioteca = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1,
                                    dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,
                                    dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)

#Removendo linhas duplicadas
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()

#Importando mais dados
dados_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')

#Mesclando as duas bases de dados
emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)

# --- TRATAMENTO DOS DADOS DIA 02 ---
# Criando a coluna 'CDU' de acordo com a localização

#Criando uma coluna para classificar os CDUs
CDU_lista = []
for cdu in emprestimos_completo['localizacao']:
    if (cdu < 100):
        CDU_lista.append('Generalidades')
    elif (cdu < 200):
        CDU_lista.append('Filosofia e Psicologia')
    elif (cdu < 300):
        CDU_lista.append('Religião')
    elif (cdu < 400):
        CDU_lista.append('Ciências Sociais')
    elif (cdu < 500):
        CDU_lista.append('Classe Vaga')
    elif (cdu < 600):
        CDU_lista.append('Matemática e Ciências Naturais')
    elif (cdu < 700):
        CDU_lista.append('Ciências Aplicadas')
    elif (cdu < 800):
        CDU_lista.append('Belas Artes')
    elif (cdu < 900):
        CDU_lista.append('Linguagem. Lingua. Linguística')
    else:
        CDU_lista.append('Geografia. Biografia. História')

emprestimos_completo['CDU_lista'] = CDU_lista
#Excluindo a coluna 'Registro Sistema'
emprestimos_completo = emprestimos_completo.drop(columns=['registro_sistema'])

#Alterando o tipo da coluna 'Matricula ou Siape'
emprestimos_completo['matricula_ou_siape'] = emprestimos_completo['matricula_ou_siape'].astype('string')

# --- TRATAMENTO DOS DADOS DIA 03 ---
#Verificando os empréstimos por ano

# Configurações da página
st.set_page_config(
    page_title="Análise de dados na biblioteca da UFRN",
    page_icon="📊",
    layout="wide",
)

# Convertendo para datetime
emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])

# --- Conteúdo de Tela ---
#Título do Dashboard
st.title("Dashboard de Análise de Empréstimos na Biblioteca")
#Subtítulo do Dashboard
st.subheader("Análise dos Empréstimos na Biblioteca da UFRN de 2010 a 2020 por período")


#Setando as colunas
col_graf1, col_graf2 = st.columns(2)

# Gráfico 1: Quantidade de Empréstimos por ano
with col_graf1:
    if not emprestimos_completo.empty:
        contagem_emprestimos_ano = emprestimos_completo['data_emprestimo'].dt.year.value_counts().reset_index()
        contagem_emprestimos_ano.columns = ['ano_emprestimo', 'contagem']
        grafico_contagem_empr_ano = px.bar(
            contagem_emprestimos_ano,
            x='ano_emprestimo',
            y='contagem',
            title="Quantidade de Empréstimos por Ano",
            labels={'ano_emprestimo': 'Ano de Empréstimo', 'contagem': 'Número de Empréstimos'}
        )
        grafico_contagem_empr_ano.update_layout(title_x=0.1)
        st.plotly_chart(grafico_contagem_empr_ano, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")

# Gráfico 2: Quantidade de Empréstimos por mês
with col_graf2:
    if not emprestimos_completo.empty:
        contagem_emprestimos_mes = emprestimos_completo['data_emprestimo'].dt.month.value_counts().reset_index()
        contagem_emprestimos_mes.columns = ['mes_emprestimo', 'contagem']
# Adiciona o nome dos meses
        contagem_emprestimos_mes['nome_mes'] = contagem_emprestimos_mes['mes_emprestimo'].map({
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
            7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        })
# Ordena pelo número do mês
        contagem_emprestimos_mes = contagem_emprestimos_mes.sort_values('mes_emprestimo')
        grafico_contagem_empr_mes = px.bar(
            contagem_emprestimos_mes,
            x='nome_mes',
            y='contagem',
            title="Quantidade de Empréstimos por Mês",
            labels={'nome_mes': 'Mês de Empréstimo', 'contagem': 'Número de Empréstimos'}
        )
        grafico_contagem_empr_mes.update_layout(title_x=0.1)
        st.plotly_chart(grafico_contagem_empr_mes, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")
#Explicando o dashboard
st.text("Gráficos com os empréstimos por período pegando a quantidade total de exemplares emprestados por cada ano e também por cada mês e plotando um gráfico de linhas.")
#Adicionando espaçamento
st.markdown("<br><br>", unsafe_allow_html=True)
# --- TRATAMENTO DOS DADOS DIA 04 ---
#Verificando os empréstimos por biblioteca e CDU


#Subtítulo do Dashboard
st.subheader("Análise dos Empréstimos na Biblioteca da UFRN de 2010 a 2020 por tipo de biblioteca e por CDU")
#Setando as colunas
col_graf3, col_graf4 = st.columns(2)

# Gráfico 3: Quantidade de Empréstimos por biblioteca
with col_graf3:
    if not emprestimos_completo.empty:
        contagem_emprestimos_biblioteca = emprestimos_completo['biblioteca'].value_counts().reset_index()
        contagem_emprestimos_biblioteca.columns = ['biblioteca', 'contagem']
        grafico_contagem_empr_biblioteca = px.bar(
            contagem_emprestimos_biblioteca,
            x='contagem',
            y='biblioteca',
            title="Quantidade de Empréstimos por Biblioteca",
            labels={'biblioteca': 'Biblioteca', 'contagem': 'Número de Empréstimos'}
        )
        grafico_contagem_empr_biblioteca.update_layout(title_x=0.1, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_contagem_empr_biblioteca, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")

# Gráfico 4: Quantidade de Empréstimos por CDU
with col_graf4:
    if not emprestimos_completo.empty:
        contagem_emprestimos_cdu = emprestimos_completo['CDU_lista'].value_counts().reset_index()
        contagem_emprestimos_cdu.columns = ['cdu', 'contagem']
        grafico_contagem_empr_cdu = px.bar(
            contagem_emprestimos_cdu,
            x='cdu',
            y='contagem',
            title="Quantidade de Empréstimos por CDU",
            labels={'cdu': 'CDU', 'contagem': 'Número de Empréstimos'}
        )
        grafico_contagem_empr_cdu.update_layout(title_x=0.1, xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_contagem_empr_cdu, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")

#Explicando o dashboard
st.text("Gráficos com os Empréstimos por biblioteca e CDU pegando a quantidade total de exemplares emprestados por cada biblioteca e por cada CDU e plotando dois gráficos de barras, um para cada análise.")
#Adicionando espaçamento
st.markdown("<br><br>", unsafe_allow_html=True)

# --- TRATAMENTO DOS DADOS DIA 05 ---
#Criando boxplots

# Criando DataFrame para Alunos de Graduação - Acervo Circulante
alunos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE GRADUAÇÃO"')
alunos_graduacao_acervo_circulante = alunos_graduacao.query('colecao == "Acervo Circulante"')
alunos_graduacao_acervo_circulante = pd.DataFrame(alunos_graduacao_acervo_circulante)
alunos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_graduacao_acervo_circulante['data_emprestimo'])
alunos_graduacao_acervo_circulante['ano'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_graduacao_acervo_circulante['mes'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.loc[:,['ano','mes']]
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()


st.subheader("Análise dos Empréstimos na Biblioteca da UFRN de 2010 a 2020 por Alunos de Graduação e Pós-Graduação da coleção que mais é emprestada")
# Criando o boxplot
# Gráfico 5: Boxplot de empréstimos mensais por ano (Alunos de Graduação - Acervo Circulante)
col_graf5 = st.columns(1)
with col_graf5[0]:
    if not alunos_graduacao_acervo_circulante.empty:
        fig = px.box(
            alunos_graduacao_acervo_circulante,
            x="ano",
            y="quantidade",
            title="Distribuição de Empréstimos mensais por ano (Alunos de Graduação - Acervo Circulante)"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")


# Criando DataFrame para Alunos de Pós-Graduação - Acervo Circulante
alunos_pos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE PÓS-GRADUAÇÃO"')
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao.query('colecao == "Acervo Circulante"')
alunos_pos_graduacao_acervo_circulante = pd.DataFrame(alunos_pos_graduacao_acervo_circulante)
alunos_pos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_pos_graduacao_acervo_circulante['data_emprestimo'])
alunos_pos_graduacao_acervo_circulante['ano'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_pos_graduacao_acervo_circulante['mes'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.loc[:,['ano','mes']]
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()


# Criando o boxplot
# Gráfico 6: Boxplot de empréstimos mensais por ano (Alunos de Pós-Graduação - Acervo Circulante)
col_graf6 = st.columns(1)
with col_graf6[0]:
    if not emprestimos_completo.empty:
        fig = px.box(
            alunos_pos_graduacao_acervo_circulante,
            x="ano",
            y="quantidade",
            title="Distribuição de Empréstimos mensais por ano (Alunos de Pós-Graduação - Acervo Circulante)"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de empréstimos.")

#Explicando o dashboard
st.text("Dois gráficos de boxplot dos Empréstimos por Alunos de Graduação e Pós-Graduação da coleção que mais é emprestada, no caso foi o acervo circulante para ambos, plotando os gráficos requisitados, um para cada análise.")

#Adicionando espaçamento
st.markdown("<br><br>", unsafe_allow_html=True)

# --- TRATAMENTO DOS DADOS DIA 06 ---
#Concatenar dados e criar gráficos

# Carregar os dados
usuarios_antes_2010 = pd.read_excel('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_6-Novos_dados_novas_analises/Datasets/matricula_alunos.xlsx',
                                        sheet_name='Até 2010',skiprows=1)
usuarios_depois_2010 = pd.read_excel('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_6-Novos_dados_novas_analises/Datasets/matricula_alunos.xlsx',
                                        sheet_name='Após 2010',skiprows=1)
#Concatenando os dados
usuarios = pd.concat([usuarios_antes_2010,usuarios_depois_2010],ignore_index=True)
#Alterando o nome das colunas para o Json
usuarios.rename(columns={
    usuarios.columns[0]: 'matricula_ou_siape',
    usuarios.columns[1]: 'tipo_vinculo_usuario',
    usuarios.columns[2]: 'curso'
}, inplace=True)

usuarios = usuarios[['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']]

#Carregando o json
usuarios_json = pd.read_json('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_6-Novos_dados_novas_analises/Datasets/cadastro_alunos.json')
#Tornando lista
usuarios_graduacao_json = pd.read_json(usuarios_json.registros[0])
#Alterando a tipagem
usuarios_graduacao_json.matricula_ou_siape = usuarios_graduacao_json.matricula_ou_siape.astype('float')
usuarios_graduacao_json.matricula_ou_siape = usuarios_graduacao_json.matricula_ou_siape.astype('string')
#Mesclando os dados
usuarios = pd.concat([usuarios,usuarios_graduacao_json],ignore_index=True)

matricula_apos_2015 = emprestimos_completo.query("tipo_vinculo_usuario == 'ALUNO DE GRADUAÇÃO'")
matricula_apos_2015 = matricula_apos_2015.loc[:,['matricula_ou_siape', 'data_emprestimo']]
matricula_apos_2015 = matricula_apos_2015.query("data_emprestimo.dt.year >= 2015")
matricula_apos_2015 = matricula_apos_2015.dropna()

# Adiciona a coluna 'curso' via merge
matricula_apos_2015 = matricula_apos_2015.merge(usuarios[['matricula_ou_siape', 'curso']], on='matricula_ou_siape', how='left')

# Excluindo valores nulos
matricula_apos_2015 = matricula_apos_2015.dropna()

# Filtrando  cursos
cursos_selecionados = matricula_apos_2015[matricula_apos_2015['curso'].isin([
    'BIBLIOTECONOMIA','CIÊNCIAS SOCIAIS','COMUNICAÇÃO SOCIAL','DIREITO','FILOSOFIA','PEDAGOGIA'
])]

#Convertendo em ano
cursos_selecionados['ANO'] = cursos_selecionados['data_emprestimo'].dt.year
# A Tabela requerida
emprestimos_cursos_selecionados = cursos_selecionados.groupby(['ANO','curso']).size().reset_index(name='QUANTIDADE_EMPRESTIMOS')
emprestimos_cursos_selecionados.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']

#Criando a tabela pivotada
emprestimos_tipo_usuario_curso_pivot = emprestimos_cursos_selecionados.pivot_table(
    index = 'CURSO',
    columns = 'ANO',
    values = 'QUANTIDADE_EMPRESTIMOS',
    fill_value = '-',
    aggfunc= sum,
    margins = True,
    margins_name = 'TOTAL',
)

st.subheader("Tabela pivotada dos Empréstimos na Biblioteca da UFRN de 2010 a 2020 por Alunos de Graduação depois de 2015 filtrando apenas os cursos de Biblioteconomia, Ciências Sociais, Comunicação Social, Direito, Filosofia e Pedagogia, cursos que passarão por avaliação do MEC.")

# Mostrando a tabela pivotada
if not emprestimos_tipo_usuario_curso_pivot.empty:
    st.text("Tabela de Empréstimos por Curso e Ano de graduandos depois de 2015")
    st.dataframe(emprestimos_tipo_usuario_curso_pivot)
else:
    st.warning("Nenhum dado para exibir na tabela pivotada.")

#Explicando o dashboard
st.text("Análise dos Empréstimos por Alunos de Graduação após 2015 em tabela pivotada, filtrando apenas os cursos de Biblioteconomia, Ciências Sociais, Comunicação Social, Direito, Filosofia e Pedagogia.")
#Adicionando espaçamento
st.markdown("<br><br>", unsafe_allow_html=True)

# --- TRATAMENTO DOS DADOS DIA 07 ---
#Analisando diferenças porcentuais desde 2017 entre alunos de pós graduação
# Filtrando os dados para alunos de pós-graduação
alunos_pos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE PÓS-GRADUAÇÃO"')  
alunos_pos_graduacao = alunos_pos_graduacao.loc[:,['data_emprestimo', 'matricula_ou_siape']]
alunos_pos_graduacao = alunos_pos_graduacao.dropna()
alunos_pos_graduacao['data_emprestimo'] = pd.to_datetime(alunos_pos_graduacao['data_emprestimo'])
alunos_pos_graduacao['ANO'] = alunos_pos_graduacao['data_emprestimo'].dt.year
alunos_pos_graduacao = alunos_pos_graduacao.query("ANO >= 2017")
# Contando o número de empréstimos por ano
emprestimos_ano_pos_graduacao = alunos_pos_graduacao.groupby('ANO').size().reset_index(name='QUANTIDADE_EMPRESTIMOS')
#Criando Df do Json para mesclar
usuarios_pos_graduacao_json = pd.read_json(usuarios_json.registros[1])
usuarios_pos_graduacao_json.matricula_ou_siape = usuarios_pos_graduacao_json.matricula_ou_siape.astype('float')
usuarios_pos_graduacao_json.matricula_ou_siape = usuarios_pos_graduacao_json.matricula_ou_siape.astype('string')

#Carregando os dados
usuarios_excel_pos = pd.concat([usuarios_antes_2010,usuarios_depois_2010],ignore_index=True)
#Alterando o nome das colunas para o Json
usuarios.rename(columns={
    usuarios_excel_pos.columns[0]: 'matricula_ou_siape',
    usuarios_excel_pos.columns[1]: 'tipo_vinculo_usuario',
    usuarios_excel_pos.columns[2]: 'curso'
}, inplace=True)

usuarios_excel_pos = usuarios[['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']]


df_pos_graduacao = pd.concat([usuarios_excel_pos, usuarios_pos_graduacao_json],ignore_index=True)


# Adiciona a coluna 'curso' via merge
alunos_pos_graduacao = alunos_pos_graduacao.merge(df_pos_graduacao[['matricula_ou_siape', 'curso']], on='matricula_ou_siape', how='left')
# Excluindo valores nulos
alunos_pos_graduacao = alunos_pos_graduacao.dropna()

#contando a quantidade de empréstimos por ano e curso
alunos_pos_graduacao = alunos_pos_graduacao.groupby(['ANO','curso']).size().reset_index(name='QUANTIDADE_EMPRESTIMOS')
alunos_pos_graduacao.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']


#Criando a tabela pivotada
alunos_pos_graduacao_pivot = alunos_pos_graduacao.pivot_table(
    index = 'CURSO',
    columns = 'ANO',
    values = 'QUANTIDADE_EMPRESTIMOS'
)

#Importando mais dados
previsao_2022 = pd.read_table('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_7-Apresentando_resultados_em_HTML/Dataset/previsao')
previsao_2022 = previsao_2022['curso previsao_2022'].str.split(' ',expand=True)

previsao_2022.index = alunos_pos_graduacao_pivot.index
alunos_pos_graduacao_pivot['2022'] = previsao_2022.iloc[:,1]

#Alterando a tipagem da coluna 2022
alunos_pos_graduacao_pivot['2022'] = alunos_pos_graduacao_pivot['2022'].astype('int')

# Função para calcular a diferença percentual entre anos consecutivos
def diferenca_percentual_ano_anterior(x,y):
  return round(((x / y * 100) - 100),2)

percentual_2018 = diferenca_percentual_ano_anterior(alunos_pos_graduacao_pivot.iloc[:,1],alunos_pos_graduacao_pivot.iloc[:,0])
percentual_2019 = diferenca_percentual_ano_anterior(alunos_pos_graduacao_pivot.iloc[:,2],alunos_pos_graduacao_pivot.iloc[:,1])
percentual_2022 = diferenca_percentual_ano_anterior(alunos_pos_graduacao_pivot.iloc[:,3],alunos_pos_graduacao_pivot.iloc[:,2])

percentual = pd.DataFrame({'2018':percentual_2018,
                           '2019':percentual_2019,
                           '2022':percentual_2022})

percentual.reset_index(inplace=True)
percentual.columns = percentual.columns.str.capitalize()
percentual.Curso = percentual.Curso.str.capitalize()
percentual.reset_index(drop=True, inplace=True)

st.subheader("Análise dos Empréstimos na Biblioteca da UFRN de 2017 a 2022 por Alunos de Pós-Graduação com o percentual de variação anual desde 2017")

# Mostrando a tabela pivotada   
if not percentual.empty:
    st.text("Percentual de Variação Anual dos Empréstimos por Curso (Pós-Graduação)")
    st.dataframe(percentual, use_container_width=True)
else:
    st.warning("Nenhum dado para exibir na tabela pivotada.")

#Explicando o dashboard
st.text("Plotando uma tabela pivotada com o percentual de variação de 2017 a 2022, excluindo o periodo de pandemia")