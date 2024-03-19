# %%
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq

# %%
Produto     = pd.read_excel(r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\Produto.xlsx")
#items       = pd.read_excel(r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\items.xlsx")
#ordens      = pd.read_excel(r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\Ordens.xlsx")
#Categoria   = pd.read_excel(r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\Categoria.xlsx")
#clientes    = pd.read_csv  (r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\Clientes.csv",delimiter=",")

# %%
#Categoria.head()

# %%
projeto     ='projetopython-417314'
dataset     ='Ecommerce'
BQproduto   ='Produto'
#BQitems     ='Items'
#BQordens    ='Ordens'
#BQCategoria ='Categoria'
#BQclientes  ='clientes'
parameretro ='replace'    

# %%
credencial = service_account.Credentials.from_service_account_file(
    r'C:\Users\Eryck de Noronha\Documents\BigQuery_python_git\Google BigQuery\altenticação\projetopython-417314-d20993336969.json',
    scopes=['https://www.googleapis.com/auth/bigquery']
)

# %%
Produto.to_gbq(destination_table=f'{projeto}.{dataset}.{BQproduto}',   
          project_id=projeto,
          if_exists=parameretro,
          credentials=credencial)

# %%
#items.to_gbq(destination_table=f'{projeto}.{dataset}.{BQitems}',   
#          project_id=projeto,
#          if_exists=parameretro,
#          credentials=credencial)

# %%
#ordens.to_gbq(destination_table=f'{projeto}.{dataset}.{BQordens}',   
#          project_id=projeto,
#          if_exists=parameretro,
#          credentials=credencial)

# %%
#Categoria.to_gbq(destination_table=f'{projeto}.{dataset}.{BQCategoria}',   
#          project_id=projeto,
#          if_exists=parameretro,
#          credentials=credencial)

# %%
# Realiza a carga de tabela de clientes 
#clientes.to_gbq(destination_table=f'{projeto}.{dataset}.{BQclientes}',   
#          project_id=projeto,
#          if_exists=parameretro,
#          credentials=credencial)


