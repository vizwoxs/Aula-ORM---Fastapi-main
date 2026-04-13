from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 
from database import get_db
from models import Curso, Aluno

# Inicializar o fastapi
app = FastAPI(title="Gestão escolar")
templates = Jinja2Templates(directory="templates")

# Rodar api
# No terminal: python -m uvicorn main:app --reload

# Rota
# Métodos http: GET, POST, PUT, DELETE

@app.get("/cursos/cadastro")
def cadastro_curso(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro_curso.html",
        {"request": request}
    )
