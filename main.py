import pandas 

movie_data = pandas.read_csv("netflix_titles.csv")

# Obtendo todas as colunas
columns = movie_data.columns.values
print(f"A tabela possui as seguintes colunas: {columns}")

# Quantidade de filmes disponiveis
movies = movie_data[movie_data.type == "Movie"]
print(f"A Quantidade de filmes Disponiveis é: {movies}")
