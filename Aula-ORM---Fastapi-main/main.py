from fastapi import FastAPI, Depends, HTTPException, Request, Form

# Inicializar o fastapi
app = FastAPI(title="Gestão escolar")

# Rodar api
# No terminal: python -m uvicorn main:app --reload

# Rota
# Métodos http: GET, POST, PUT, DELETE
@app.get("/")
def tela_inicial():
    return {"mensagem":"Bem-vindo ao sistema de gestão escolar"}

# Banco de dados
alunos = {
    1:{"nome": "Gabriel", "idade": 34},
    2:{"nome": "Cassio", "idade": 34},
    3:{"nome": "Emilly", "idade": 34},
}
@app.get("/alunos")
def listar_alunos():
    return {"alunos":alunos}