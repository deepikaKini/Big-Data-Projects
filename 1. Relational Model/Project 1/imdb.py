import pandas as p
import numpy as np


def main():
    # cleaning the primary table and saving it:
    # cleaning involves conversion of primary key from string to integer,
    # cleaning the integer columns to hold integer(else hold 0),
    #removing invalid rows which don't map to primary table
    #   (eg: Adult movies removed from primary table)
    ##primary table title basics
    df_basics = p.read_table(r"/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.basics.tsv",
                             low_memory=False)  # , nrows = 500)
    # print(df_basics.dtypes)
    #clean table columns
    df_basics['tconst'] = df_basics['tconst'].str.slice(2, ).fillna(0).astype('int')
    # clean endyear
    df_basics.loc[df_basics['endYear'].str.isdigit() == False, 'endYear'] = 0
    df_basics['endYear'] = df_basics['endYear'].astype('int')
    # clean startYear
    df_basics.loc[df_basics['startYear'].str.isdigit() == False, 'startYear'] = 0
    df_basics['startYear'] = df_basics['startYear'].astype('int')
    # clean isAdult
    df_basics.loc[df_basics['isAdult'].str.isdigit() == False, 'isAdult'] = 0
    df_basics['isAdult'] = df_basics['isAdult'].astype('int')
    # clean runtimeMinutes
    df_basics.loc[df_basics['runtimeMinutes'].str.isdigit() == False, 'runtimeMinutes'] = 0
    df_basics['runtimeMinutes'] = df_basics['runtimeMinutes'].astype('int')

    # filter out adult movies
    df_basics = df_basics.loc[df_basics["isAdult"] == 0]

    # make a table with primary key and genres array
    df_basics['genres'] = df_basics['genres'].to_list()
    df_genre = p.DataFrame().assign(tconst=df_basics['tconst'], genres=df_basics['genres'])

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
    # df_basics.drop(['genres'])

    print(df_genre)
    print(list_genre)

    # making a dataframe using unique genre values and populating an index to treat as primary key
    df_genre_unique = p.DataFrame(list_genre, columns=['genres'])
    # df_genre_unique = df_genre_unique.astype(str)
    # df_genre_unique.rename(columns={"genres": "genres"})
    df_genre_unique["genre_tconst"] = df_genre_unique.index.astype(int)
    print(df_genre_unique)
    print(df_genre)

    # populating the foreign key in the primary genre table
    df_genre = df_genre.merge(df_genre_unique, on="genres")
    # df_genre =
    print(df_genre.loc[df_genre["tconst"] == 1])

    df_genre = df_genre.drop(columns=['genres'])
    df_basics = df_basics.drop(columns=['genres'])
    print(df_genre)
    print(df_basics.dtypes)

    # view data for checks
    p.set_option('display.max_columns', None)
    # print(df_basics.head())
    df_basics.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title2.csv", index=False)
    df_genre.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/genre_title_mapping.csv",
                    index=False)
    df_genre_unique.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/unique_genre.csv",
                           index=False)

    ########ratings file

    ##episode file
    #reading file
    df_epi = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.episode.tsv")
    #cleaning id column
    df_epi['tconst'] = df_epi['tconst'].str.slice(2, ).fillna(0).astype('int')
    df_epi['parentTconst'] = df_epi['parentTconst'].str.slice(2, ).fillna(0).astype('int')
    #testing if tconst can be made a primary key
    print(p.Series(df_epi['tconst']).is_unique)
    df_epi.loc[df_epi['seasonNumber'].str.isdigit() == False, 'seasonNumber'] = 0
    df_epi['seasonNumber'] = df_epi['seasonNumber'].astype('int')
    df_epi.loc[df_epi['episodeNumber'].str.isdigit() == False, 'episodeNumber'] = 0
    df_epi['episodeNumber'] = df_epi['episodeNumber'].astype('int')
    p.set_option('display.max_columns', None)

    #joining to get rows which are present in the title
    df_epi = df_epi.join(df_title.set_index('tconst'), on="parentTconst", how="inner")
    df_epi = df_epi[['tconst', 'parentTconst', 'seasonNumber', 'episodeNumber']]
    print(df_epi.head())

    df_epi.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/episode.csv", index=False)

    ##principals file
    #read file
    df_principals = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.principals.tsv")
    #clean id fields
    df_principals['tconst'] = df_principals['tconst'].str.slice(2, ).fillna(0).astype('int')
    df_principals['nconst'] = df_principals['nconst'].str.slice(2, ).fillna(0).astype('int')
    df_title = df_title[['tconst']]
    p.set_option('display.max_columns', None)
    #inner join with primary table
    df_principals = df_principals.join(df_title.set_index('tconst'), on="tconst", how="inner")
    df_principals = df_principals[['tconst', 'ordering', 'nconst', 'category', 'job', 'characters']]
    print(df_principals.head())
    print(df_principals.dtypes)
    #write file
    df_principals.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/principals.csv", index=False)

    ##akas file
    #read file
    df_akas = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.akas.tsv", low_memory=False,
                           nrows=10)
    #clean primary key
    df_akas['titleId'] = df_akas['titleId'].str.slice(2, ).fillna(0).astype('int')
    p.set_option('display.max_columns', None)
    print(df_akas.head())
    print(df_akas.dtypes)
    #inner join
    df_akas = df_akas.join(df_title.set_index('tconst'), on="titleId", how="inner")
    df_akas = df_akas[['titleId', 'ordering', 'title', 'region', 'language', 'types', 'attributes', 'isOriginalTitle']]
    print(df_akas.head())
    #write file
    df_akas.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/akas.csv", index=False)


    ##people file
    df_people = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/name.basics.tsv")
    df_people['nconst'] = df_people['nconst'].str.slice(2, ).fillna(0).astype('int')
    df_people.loc[df_people['deathYear'].str.isdigit() == False, 'deathYear'] = 0
    df_people['deathYear'] = df_people['deathYear'].astype(int)
    df_people.loc[df_people['birthYear'].str.isdigit() == False, 'birthYear'] = 0
    df_people['birthYear'] = df_people['birthYear'].astype(int)
    df_people['knownForTitles'] = '{'+df_people['knownForTitles']+'}'
    #gets unique nconst from Principals file to do outer join. helps apply FK constraint
    df = p.DataFrame(df_princ['nconst'].unique(), columns=['nconst'])
    df_people = df_people.join(df.set_index('nconst'), on="nconst", how="outer")
    df_people = df_people[['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']]

    df_people.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/people.csv",  index = False)

    ##crew file
    df_crew = p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/title.crew.tsv")
    df_title = df_title[['tconst']]
    df_crew['tconst'] = df_crew['tconst'].str.slice(2, ).fillna(0).astype('int')
    #creating separate tables
    df_director = df_crew[['tconst', 'directors']]
    df_writer = df_crew[['tconst', 'writers']]

    #creating multiple rows for each record
    df_director['tmp'] = df_director.apply(lambda row: list(zip(row['directors'].split(','))), axis=1)
    df_director = df_director.explode('tmp')
    df_director[['directorId']] = p.DataFrame(df_director['tmp'].tolist(), index=df_director.index)
    df_director.drop(columns=['tmp', 'directors'], inplace=True)
    df_director = df_director.loc[df_director["directorId"] != "\\N"]
    df_director['directorId'] = df_director['directorId'].str.slice(2, ).fillna(0).astype('int')
    df_director = df_director.join(df_title.set_index('tconst'), on="tconst", how="inner")

    # creating multiple rows for each record
    df_writer['tmp'] = df_writer.apply(lambda row: list(zip(row['writers'].split(','))), axis=1)
    df_writer = df_writer.explode('tmp')
    df_writer[['writerId']] = p.DataFrame(df_writer['tmp'].tolist(), index=df_writer.index)
    df_writer.drop(columns=['tmp', 'writers'], inplace=True)
    df_writer = df_writer.loc[df_writer["writerId"] != "\\N"]
    df_writer['writerId'] = df_writer['writerId'].str.slice(2, ).fillna(0).astype('int')
    print(df_writer.head())
    df_writer = df_writer.join(df_title.set_index('tconst'), on="tconst", how="inner")

    #gets unique nconst from Principals file to do outer join. helps apply FK constraint
    df = p.DataFrame(df_director['nconst'].unique(), columns=['nconst'])
    df_people = df_people.join(df.set_index('nconst'), on="nconst", how="outer")
    # gets unique nconst from Principals file to do outer join. helps apply FK constraint
    df = p.DataFrame(df_writer['nconst'].unique(), columns=['nconst'])
    df_people = df_people.join(df.set_index('nconst'), on="nconst", how="outer")


    df_director.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/director_mapping.csv",
                       index=False)
    df_writer.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/writer_mapping.csv", index=False)
    #rewriting people file with extra nconst
    df_people.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/people.csv", index=False)

if __name__ == '__main__':
    main()