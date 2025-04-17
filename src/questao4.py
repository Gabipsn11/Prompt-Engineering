from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, validator
from datetime import date
import uuid

app = FastAPI()

# Modelo Pydantic para Item
class Item(BaseModel):
    nome: constr(max_length=25)  # String com até 25 caracteres
    valor: float  # Valor float
    data: date  # Data no formato YYYY-MM-DD

    # Validação para data não futura
    @validator("data")
    def data_nao_futura(cls, v):
        if v > date.today():
            raise ValueError("A data não pode ser futura")
        return v

# Endpoint POST para processar Item
@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    try:
        # Converte Item para dict e adiciona UUID
        item_dict = item.dict()
        item_dict["uuid"] = str(uuid.uuid4())
        return item_dict
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Instruções de teste:
# 1. Instale dependências: pip install fastapi pydantic uvicorn
# 2. Execute: uvicorn main:app --reload
# 3. Teste com cURL:
# curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"nome": "Produto Teste", "valor": 99.99, "data": "2023-10-15"}'
# Resposta esperada:
# {
#   "nome": "Produto Teste",
#   "valor": 99.99,
#   "data": "2023-10-15",
#   "uuid": "123e4567-e89b-12d3-a456-426614174000"
# }