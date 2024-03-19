import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq
import schedule  
import time  
import pyodbc 


def job(): 
    
    Produto     = pd.read_excel(r"C:\Users\Eryck de Noronha\Documents\GitHub\BigQuery_Python\arquivos\execel\ecommecer\Produto.xlsx")
    
    projeto     ='projetopython-417314'
    dataset     ='Ecommerce'
    BQproduto   ='Produto'
    parameretro ='replace'

    credencial = service_account.Credentials.from_service_account_file(
    r'C:\Users\Eryck de Noronha\Documents\BigQuery_python_git\Google BigQuery\altenticação\projetopython-417314-d20993336969.json',
    scopes=['https://www.googleapis.com/auth/bigquery']
    )

    Produto.to_gbq(destination_table=f'{projeto}.{dataset}.{BQproduto}',   
            project_id=projeto,
            if_exists=parameretro,
            credentials=credencial)   

schedule.every(10).seconds.do(job) # escolher a frequencia 
while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas  