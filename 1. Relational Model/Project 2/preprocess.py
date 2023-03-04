import pandas as p

df_title = p.read_table(r'/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.basics.tsv', dtype='unicode')


# clean endyear
df_title.loc[df_title['endYear'].str.isdigit() == False, 'endYear'] = 0
df_title['endYear'] = df_title['endYear'].astype('int')
# clean startYear
df_title.loc[df_title['startYear'].str.isdigit() == False, 'startYear'] = 0
df_title['startYear'] = df_title['startYear'].astype('int')
# clean isAdult
df_title.loc[df_title['isAdult'].str.isdigit() == False, 'isAdult'] = 0
df_title['isAdult'] = df_title['isAdult'].astype('int')
# clean runtimeMinutes
df_title.loc[df_title['runtimeMinutes'].str.isdigit() == False, 'runtimeMinutes'] = 0
df_title['runtimeMinutes'] = df_title['runtimeMinutes'].astype('int')

# filter out adult movies
df_title = df_title.loc[df_title['isAdult'] == 0]

# make a table with primary key and genres array
df_title['genres'] = df_title['genres'].to_list()
df_genre = p.DataFrame().assign(tconst=df_title['tconst'], genres=df_title['genres'])

# populate primary key values by splitting array
df_genre['genres'] = df_genre['genres'].astype(str)
df_genre['tmp'] = df_genre.apply(lambda row: list(zip(row['genres'].split(','))), axis=1)
df_genre = df_genre.explode('tmp')
df_genre[['genres']] = p.DataFrame(df_genre['tmp'].tolist(), index=df_genre.index)
df_genre.drop(columns='tmp', inplace=True)
df_genre['genres'] = df_genre['genres'].astype(str)
# making a list with unique genre values
list_genre = set(df_genre['genres'])

# drop genre in the primary table
# df_title.drop(['genres'])

print(df_genre)
print(list_genre)

# making a dataframe using unique genre values and populating an index to treat as primary key
df_genre_unique = p.DataFrame(list_genre, columns=['genres'])
# df_genre_unique = df_genre_unique.astype(str)
# df_genre_unique.rename(columns={'genres': 'genres'})
df_genre_unique['genre_tconst'] = df_genre_unique.index.astype(int)
print(df_genre_unique)
print(df_genre)

# populating the foreign key in the primary genre table
df_genre = df_genre.merge(df_genre_unique, on='genres')
# # df_genre =
# print(df_genre.loc[df_genre['tconst'] == 1])
p.set_option('display.max_columns', None)
df_genre = df_genre.drop(columns=['genres'])
df_title = df_title.drop(columns=['genres'])
df_genre = df_genre.rename(columns={'tconst': 'title', 'genre_tconst': 'genre'})

print(df_genre.head())
df_genre = df_genre[['title','genre']]
print(df_genre.head())
print(df_title.dtypes)

# view data for checks

# print(df_title.head())
#df_title.to_csv('/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title2.csv', index=False)
df_genre.to_csv('/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/genre_title_mapping.csv',
               index=False)
df_genre_unique.to_csv('/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/unique_genre.csv',
                       index=False)

print(df_title)
df_rating = p.read_table('/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.ratings.tsv', dtype='unicode')
df_rating['numVotes']=df_rating['numVotes'].astype(str)
print(df_rating.head())

p.set_option('display.max_columns', None)
df_title = df_title.join(df_rating.set_index('tconst'), on='tconst', how='left')
df_title = df_title.rename(columns={'tconst': 'id', 'titleType': 'type', 'primaryTitle': 'title', 'runtimeMinutes': 'runtime',
                   'averageRating': 'avgRating'})
cols = list(df_title.columns.values)
print(cols)
print(df_title.head())
df_title  = df_title[['id','type', 'title', 'originalTitle', 'startYear', 'endYear', 'runtime', 'avgRating', 'numVotes']]

cols = list(df_title.columns.values)
print(cols)
print(df_title.head())
df_title.to_csv('/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title1_project2.csv', index=False)
