import pandas as p
def main():
    # df_people =p.read_table("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/name.basics.tsv")
    df_people= p.read_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/people1.csv")

    #
    # df_people['deathYear'] = df_people['deathYear'].astype(int)
    #
    # df_people['birthYear'] = df_people['birthYear'].astype(int)
    df_people = df_people[['nconst', 'primaryName',  'primaryProfession', 'knownForTitles']]

    # df_princ = df_princ[['nconst']]
    # df_princ['nconst'] = df_princ['nconst'].astype('int')
    #
    # df = p.DataFrame(df_princ['nconst'].unique(), columns=['nconst'])
    # print(df.head())
    # df_unique  = p.DataFrame(df_list,columns=[ 'nconst'])

#     print(df_unique.dtypes)
#     print(df_unique.head())
    #get principal unique nconst and popluate using left join in people table df_principals=
    # df_people['nconst'] = df_people['nconst'].str.slice(2, ).fillna(0).astype('int')
    # df_people.loc[df_people['deathYear'].str.isdigit() == False, 'deathYear'] = 0
    # df_people['deathYear'] = df_people['deathYear'].astype(int)
    # df_people.loc[df_people['birthYear'].str.isdigit() == False, 'birthYear'] = 0
    # df_people['birthYear'] = df_people['birthYear'].astype(int)
    # df_people['knownForTitles'] = '{'+df_people['knownForTitles']+'}'
    # df_title = p.read_csv(r"/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title2.csv")
    # df_principals['tconst'] = df_principals['tconst'].str.slice(2, ).fillna(0).astype('int')
    # df_principals['nconst'] = df_principals['nconst'].str.slice(2, ).fillna(0).astype('int')
    # df_title = df_title[['tconst']]
    p.set_option('display.max_columns', None)
    #--df_people = df_people.join(df_title.set_index('tconst'), on="tconst", how="inner")
    # df_principals = p.read_csv(r"/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/principals.csv")
    # df_principals = df_principals[['tconst', 'ordering','nconst','category']]
    print(df_people.head())
    # print(df_people.dtypes)
    # df_people = df_people.join(df.set_index('nconst'), on="nconst", how="outer")
    # df_people = df_people[['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']]
    df_people.to_csv("/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/people2.csv",  index = False)

# # \copy principals(tconst, ordering, nconst, category, job, characters) FROM '/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/principals1.csv'(format csv, delimiter ',', header true);
if __name__ == '__main__':
    main()
# # \copy title(tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes) FROM '/Users/deepika/Desktop/CSCI620/Assignment_1/IMDB/ModifiedData/title1.csv'(format csv, delimiter ',', header true);