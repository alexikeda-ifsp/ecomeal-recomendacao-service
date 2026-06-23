from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from database import select_operation
from connection_api import create_connection


app = FastAPI()



@app.get("/sugestoes/")
async def verifica_sugestoes():

    connection = create_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    sugestoes = select_operation(
        connection,
        "sugestao_marmita"
    )


    connection.close()


    return JSONResponse(
        content=sugestoes,
        status_code=200
    )




@app.get("/sugestoes/{id}")
async def verifica_sugestao(id: str):

    connection = create_connection()


    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    sugestao = select_operation(
        connection,
        "sugestao_marmita",
        id
    )


    connection.close()


    if not sugestao:
        raise HTTPException(
            status_code=404,
            detail="Sugestão não encontrada"
        )


    return JSONResponse(
        content=sugestao[0],
        status_code=200
    )