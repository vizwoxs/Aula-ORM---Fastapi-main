# Arquivo onde fica as classes
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabelas Curso e aluno (1:N)
class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    descricao = Column(String(150))

    alunos = relationship("Aluno", back_populates="curso")

    def __repr__(self):
        return f"Curso: ID = {self.id} | Nome: {self.nome} | Carga Horária: {self.carga_horaria}"
class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")

    def __repr__(self):
        return f"Aluno: ID = {self.id} | Nome: {self.nome} | Email: {self.email}"
    

