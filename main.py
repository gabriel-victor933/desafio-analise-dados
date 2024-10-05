import pandas 

movie_data = pandas.read_csv("netflix_titles.csv")

# Obtendo todas as colunas
columns = movie_data.columns.values
print(f"A tabela possui as seguintes colunas: {columns}\n")

# Quantidade de filmes disponiveis
movies = movie_data[movie_data.type == "Movie"]
print(f"A Quantidade de filmes Disponiveis é: {len(movies)}\n")

# OS 5 diretores com mais filmes e series: 
director_series = movie_data['director'].value_counts()
print("Os 5 diretores com mais filmes são:")
print(director_series[0:5])

# Diretores que atuaram como atores em suas proprias produções
director_in_cast = movie_data.dropna(subset=['director','cast']).apply(lambda row: row['director'] in row['cast'], axis=1)

director_in_cast.to_csv('teste.csv')

print("Gabriel" in "Gabriel victor Alves Santana")
