import pandas as pd
import csv
import logging
logging.basicConfig(level=logging.DEBUG, filename='test.log', filemode='a',
                    format='%(levelname)s- %(asctime)s-%(name)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.info('This info message')
# def changing_status(username):
#     df = pd.read_csv('test.csv')
#     # df.loc[df.usr == username, 'status'] = 0
#
#     df.loc[df['usr'] == username, 'status'] = 0
#     df.to_csv("test.csv", index=False)

    # col1_is_Zero = (df.usr == username)
    # df.loc[col1_is_Zero, 'status'] = 0



    # with open('test.csv', "r+", newline='') as f:
    #     lst=list(csv.reader(f))
    #     print(lst)
    #     for row in lst:
    #         if row[0] == username:
    #             t = lst.index(row)
    #             lst[t][2] = 0
    #             csv_writer=csv.writer(f)
    #             csv_writer.writerows(lst)



# changing_status('ala')
# df = pd.read_csv('test.csv')
# df.replace(to_replace=df['status'].values, value=1, inplace=True)
# df.to_csv('test.csv', mode='w')
#
# df.loc[df["username"] == name] = df.loc[df["username"] == name].replace(0, 1)

# df=pd.read_csv('test.csv')
# df1 = df.filter(['name', 'price'])
# print(df1)

# df2 = df.loc[df["inventory number"] == 0]
# df3=df2.filter(['name', 'price'])
# x=df3['name'].values
# print(df3)
# print(x[0])

# df = pd.read_csv('accounts.csv')
# df1 = df.loc[df['status'] == 0]
# df2 = df1.filter(['usr'])
# print(df2)

try:
    with open('account.csv') as f:
        df = pd.read_csv(f)
except FileNotFoundError as e:
    print(e)
    logging.error(e)