import pandas 

netflix_data = pandas.read_csv("netflix_titles.csv")

# Obtendo todas as colunas
columns = netflix_data.columns.values
print(f"A tabela possui as seguintes colunas: {columns}\n")


# Quantidade de filmes disponiveis
movies = netflix_data[netflix_data.type == "Movie"]
print(f"\nA Quantidade de filmes Disponiveis é: {len(movies)}\n")


# OS 5 diretores com mais filmes e series: 
director_series = netflix_data['director'].value_counts()
print("\nOs 5 diretores com mais filmes são:")
print(director_series[0:5])


# Diretores que atuaram como atores em suas proprias produções
netflix_data["director_in_cast"] = netflix_data.dropna(subset=['director','cast']).apply(lambda row: row['director'] in row['cast'], axis=1)
directors_in_cast = netflix_data[netflix_data.director_in_cast == True].director.unique()

print("\nLista de Diretores que atuaram em suas próprias produções:")
print(directors_in_cast)


# Duração média dos filmes
movies_data = netflix_data[netflix_data.type == "Movie"]

def transform_to_int(data):
    return int(data[:-4])

mean_duration = movies_data['duration'].dropna().transform(transform_to_int).mean()

print("\nA duração média dos filmes é de {:.2f} minutos".format(mean_duration))


# OS 5 Paises com mais filmes
director_series = netflix_data['country'].value_counts()
print("\nOs 5 paises com mais filmes são:")
print(director_series[0:5])

# Duração média dos filmes
tv_show_data = netflix_data[netflix_data.type == "TV Show"]

def transform_season_to_int(data):
    if 'Seasons' in data:
        return int(data[:-8])
    else: 
        return int(data[:-7])

mean_seasons = tv_show_data['duration'].dropna().transform(transform_season_to_int).mean()


print(f"\nA quantidade média de temporadas de uma serie é de {round(mean_seasons)} temporada(s)")
