import traceback
from fastapi import FastAPI
import psycopg2

app = FastAPI()

hostname = 'localhost'
database = 'teste_anderson'
username = 'postgres'
pwd = 'THR4sher'
port_id = '5432'

@app.get("/busca")
async def fetch_filtered_data(filtro: str):
    resultados = []

    try:
       
        with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        ) as conn:
            with conn.cursor() as cur:
                print(f"Conexão estabelecida com sucesso. Filtro recebido: {filtro}")

                
                query = "SELECT razao_social FROM relato_cadop_table WHERE razao_social LIKE %s"
                cur.execute(query, (f"{filtro}%",))  
                registros = cur.fetchall()
                print(f"Registros encontrados: {registros}")
                
                
                razao_social_unica = set(registro[0] for registro in registros)
                
             
                resultados.append({"tabela": "relato_cadop_table", "registros": list(razao_social_unica)})

    except Exception as error:
       
        traceback.format_exc(error)
        return {"erro": traceback.format_exc(error)}

    
    return {"resultados": resultados}
