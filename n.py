import pandas as pd

# Criar DataFrame com dados dos alunos
data = pd.DataFrame({
    'alunos': ['ADRIEL', 'ALINE', 'MARCIA', 'JOÃO', 'PEDRO', 'CARLA'],
    'nota 1': [8.0, 7.5, 5.0, 9.0, 6.0, 7.0],
    'nota 2': [10.0, 8.5, 5.0, 9.5, 6.5, 8.0]
})

# Adicionar aluno novo
data.loc[6] = ['MARCOS', 6.7, 10.0]

# Alteração de nota (alterando a nota do Pedro para 7.0)
data.iloc[4, 2] = 7.0

# Calcular a média
data['media'] = data[['nota 1', 'nota 2']].mean(axis=1)

# Definir condições de aprovação e reprovação
alunos_aprovados = data[data['media'] >= 7]  # Alunos aprovados
alunos_reprovados = data[data['media'] < 7]   # Alunos reprovados

# Número de alunos reprovados
numero_rep = alunos_reprovados.shape[0]

# Maior e menor nota
maior_nota = data[data['media'] == data['media'].max()]
aluno_menor_nota = data[data['media'] == data['media'].min()]

# Mostrar apenas as colunas de notas
notas_geral = data[['nota 1', 'nota 2']]

# Média da turma
media_turma = data['media'].mean()

# Ordenar valores por média (em ordem decrescente)
data = data.sort_values(by='media', ascending=False).reset_index(drop=True)

# grupos 
grupos = data.groupby('media')

# Exibindo os resultados
print("_" * 30)
print('DATAFRAME:')
print(data)

print("_" * 30)
print('MEDIAS:')
print(data.loc[:, ['alunos', 'media']])

print("_" * 30)
print('ALUNOS APROVADOS:')
print(alunos_aprovados)

print("_" * 30)
print('ALUNOS REPROVADOS:')
print(alunos_reprovados)

print("_" * 30)
print(f'MAIOR MÉDIA: {maior_nota}')

print("_" * 30)
print(f'MENOR MÉDIA: {aluno_menor_nota}')

print("_" * 30)
print('MÉDIA GERAL DA TURMA:')
print(media_turma)

print("_" * 30)
print('GRUPOS')
print(grupos[['nota 1', 'nota 2', 'media']].mean())

