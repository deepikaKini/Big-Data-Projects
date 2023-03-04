import pandas as p


df_title = p.read_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title1_project2.csv")
df_people =  p.read_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/member_project2.csv")

df_principals = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.principals.tsv")
# clean id fields
df_title = df_title[['id']]
p.set_option('display.max_columns', None)
# inner join with primary table
df_principals = df_principals.join(df_title.set_index('id'), on="tconst", how="inner")
df_principals = df_principals.join(df_people.set_index('id'), on="nconst", how="inner")
# df_filter_roles = df_principals[df_principals['category'] == "actor"] | df_principals[df_principals['category'] == "actress"] | df_principals[df_principals['category'] == "producer"]


df_principals =df_principals[df_principals['category'].isin(['actor', 'actress', 'producer'])]
df_principals = df_principals[['tconst', 'ordering', 'nconst', 'category',  'characters']]
print(df_principals.head())
print(df_principals.dtypes)
# write file
# df_principals.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/principals.csv", index=False)

df_actor_title_char = df_principals[df_principals['category'].isin(['actor', 'actress'])]
df_actor_title_char = df_actor_title_char.loc[df_actor_title_char["characters"] != "\\N"]
df_actor_rows =df_actor_title_char[['tconst', 'nconst' ,'characters']]



df_actor_rows['characters'] = df_actor_rows['characters'].str.upper()
df_actor_rows['characters'] = df_actor_title_char['characters'].astype(str)
df_actor_rows['tmp'] = df_actor_rows.apply(lambda row: list(zip(row['characters'].split(','))), axis=1)
df_actor_rows = df_actor_rows.explode('tmp')
df_actor_rows[['characters']] = p.DataFrame(df_actor_rows['tmp'].tolist(), index=df_actor_rows.index)
df_actor_rows.drop(columns='tmp', inplace=True)
df_actor_rows['characters'] = df_actor_rows['characters'].astype(str)
# making a list with unique genre values

list_char = set(df_actor_title_char['characters'])
print(df_actor_rows.head())

# making a dataframe using unique genre values and populating an index to treat as primary key
df_char_unique = p.DataFrame(list_char, columns=['characters'])
df_char_unique = df_char_unique.loc[df_char_unique["characters"] != "\\N"]
df_char_unique['id'] = df_char_unique.index.astype(int)
# print(df_char_unique)
# df_actor_title_char = df_actor_rows.join(df_char_unique.set_index('characters'), on="characters", how="left")
df_actor_title_char = df_actor_title_char.merge(df_char_unique, on='characters')
print("\n",df_actor_title_char.shape[0])
# p.set_option('display.max_columns', None)
df_actor_title_char = df_actor_title_char.drop(columns=['characters'])
print(df_char_unique.head())
print(df_actor_title_char.head())

df_char_unique.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/character1.csv", index=False)
df_actor_title_char.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/actor_title_character1.csv", index=False)