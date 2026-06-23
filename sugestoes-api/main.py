from fastapi import FastAPI
from database import select_operation
from connection_api import create_connection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/sugestoes")
async def verifica_sugestoes():
    """
    Retorna uma Lista de Objetos Sugestao. Se não houver, retornar uma Lista Vazia.
    """
    client = create_connection()
    if client is None:
        raise HTTPException(status_code=500, detail="Erro na Conexão com o Banco de Dados.")
    sugestoes = select_operation(client,"sugestao_marmita")
    return JSONResponse(content=sugestoes,status_code=200)

@app.get("/sugestoes/{id}")
async def verifica_sugestao(id:str):
    """
    Procura uma Sugestao pelo ID do paciente paciente, retornando um 
    objeto. Se não houver, retorna 404.
    """
    client = create_connection()
    if client is None:
        raise HTTPException(status_code=500, detail="Erro na Conexão com o Banco de Dados.")
    try:
        sugestao = select_operation(client,"sugestao_marmita",id)
    except Exception as e:
        if e.code == "22P02":
            raise HTTPException(status_code=400,detail="ID deve estar no formato UUID. ID fornecido é Inválido")
    if sugestao is None:
        raise HTTPException(status_code=404, detail="Sugestão não encontrada.")
    return JSONResponse(content=sugestao, status_code=200)