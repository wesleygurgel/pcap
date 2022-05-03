from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome='Play 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Play 4', preco=4525.99),
    Produto(id=3, nome='xbox 360', preco=1795.99, em_oferta=True),
    Produto(id=4, nome='pc gamer', preco=199.55),
    Produto(id=5, nome='kinder ovo', preco=9999.55, em_oferta=True),
]


@app.get('/')
async def index():
    return {"Wesley": "Gurgel"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return {"produto": "Não encontrado."}


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
    return None