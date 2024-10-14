# app/main.py
from fastapi import FastAPI, HTTPException
from app.operacoes.somar import ClasseSomar
from app.operacoes.subtrair import ClasseSubtracao
from app.operacoes.multiplicar import ClasseMultiplicacao
from app.operacoes.dividir import ClasseDivisao

app = FastAPI()

# Dicionário de operações
operacoes = {
    "soma": ClasseSomar.realizar_operacao,
    "subtracao": ClasseSubtracao.realizar_operacao,
    "multiplicacao": ClasseMultiplicacao.realizar_operacao,
    "divisao": ClasseDivisao.realizar_operacao
}

@app.get("/operacao/")
async def calcular_operacao(operacao: str, a: float, b: float):
    if operacao not in operacoes:
        raise HTTPException(status_code=400, detail="Operação inválida.")
    
    resultado = operacoes[operacao](a, b)
    return {"operacao": operacao, "resultado": resultado}
