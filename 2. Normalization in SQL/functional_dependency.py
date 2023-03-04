import pandas as p
import psycopg2
# import time

def fd(df):
    """
    finds functional dependency by comparing row values for all combinations of columns
    If for one pair of rows, if both values don't match for a column but does for the other,
    it breaks and doesn't add this cosmbination of row as fd
    :param df:
    :return:None
    """
    fd_string = ''
    count_of_FDs = 0
    p.set_option('display.max_columns', None)
    #filling na for fd to be seen
    df['avgRating'] = df['avgRating'].fillna(0).astype('int')
    # print(df)
    # print("number of cols" , len(df.columns))
    for col_iterator1 in range(len(df.columns) - 1):
        print()
        fd_string += df.columns[col_iterator1] + "->"
        for col_iterator2 in range(len(df.columns) - 1):#ignoring primay_key   old:col_iterator1 + 1, len(df.columns) - 1
            if col_iterator1 != col_iterator2:
                # print(df.columns[col_iterator1], df.columns[col_iterator2])
                flag= -1
                break_flag = 0
                for index_row1 in range(len(df)):

                    # print(index_row1, len(df)," \n")
                   # print(df[df.columns[col_iterator1]][index])
                   #  print(index_row1)
                    for index_row2 in range(index_row1 + 1, len(df)):
                        # print(df[df.columns[col_iterator1]][index_row2])

                        if df[df.columns[col_iterator1]][index_row1] == df[df.columns[col_iterator1]][index_row2]:

                            # print(df[df.columns[col_iterator1]][index_row2]," ", index_row2, " ", index_row1)
                            if df[df.columns[col_iterator2]][index_row1] == df[df.columns[col_iterator2]][index_row2]:
                                flag = 1
                                continue
                            else:
                                flag  = 0
                                break_flag = 1
                                break
                    if break_flag == 1:
                        break


                if flag == 1 or flag == -1:
                        count_of_FDs +=1
                        # print(df.columns[col_iterator1] + "->" +df.columns[col_iterator2] +"\t")
                        fd_string +=df.columns[col_iterator2] +", "
        fd_string += "\n"
    print(fd_string, "\n", count_of_FDs)

def queries(conn, cursor):
    #bringing in the data and putting in a dataframe
    sql = """ 
        select * from  final_norm_grouped limit 10000
        """
    cursor.execute(sql)
    data_from_database = cursor.fetchall()
    df = p.DataFrame(data_from_database,columns=['movieId', 'type', 'startYear', 'runtime', 'avgRating', 'genreId', 'genre', 'memberId', 'birthYear', 'character', 'primary_key'])


    conn.commit()
    fd(df)

def main():
# creating a connection with the database already created for this project
    conn = psycopg2.connect(
    database='HW2_IMDB', user='postgres', password='127845', host='127.0.0.1',  # or localhost
    port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("select version()")
    queries(conn, cursor)
    conn.close()

if __name__ == '__main__':
    main()