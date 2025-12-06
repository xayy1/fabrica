import pandas as pd
import os 

csv_path='sales.csv'
if not os.path.exists(csv_path):
    data=[
        {'date':'2025-12-01',
           'product':'camisa',
           'price':50,
           'quantity':2},
        {'date':'2025-12-01',
           'product':'vestido',
           'price':80,
           'quantity':25},
        {'date':'2025-12-01',
           'product':'tenis',
           'price':530,
           'quantity':210},
        {'date':'2025-12-01',
           'product':'relógio',
           'price':300,
           'quantity':269},
        {'date':'2025-12-01',
           'product':'mochila',
           'price':90,
           'quantity':315},
        {'date':'2025-12-01',
           'product':'óculos',
           'price':216,
           'quantity':192},
        {'date':'2025-12-01',
           'product':'cinto',
           'price':25,
           'quantity':902},
        {'date':'2025-12-01',
           'product':'bermuda',
           'price':75,
           'quantity':207},
        {'date':'2025-12-01',
           'product':'celular',
           'price':3008,
           'quantity':70},
        {'date':'2025-12-01',
           'product':'anel',
           'price':890,
           'quantity':90},
 
           ]
    df_example= pd.DataFrame(data)
    df_example.to_csv(csv_path,index= False)
    print('criado com sucesso,parabéns.',csv_path)

df=pd.read_csv(csv_path,parse_dates=['date'])

required={'date','product','price','quantity'}
if not required.issubset(set(df.columns)):
    print('as colunas estão erradas')

df['total']=df['price']*df['quantity']
df[['total']].to_csv('total.csv',index=False)
print('sucesso')