# Questão 4: Endpoint FastAPI para Processar Item

## Enunciado
Utilizando uma ferramenta de IA generativa, crie um endpoint com FastAPI que valide e processe a entrada de um objeto do tipo `Item`. Siga as especificações abaixo:
1. Estrutura do `Item`:
   - **nome**: `string` com tamanho máximo de 25 caracteres.
   - **valor**: `float`.
   - **data**: valor do tipo *date*, que não pode ser superior à data atual.
2. Requisitos:
   - O endpoint deve validar os valores recebidos.
   - Após a validação, o corpo da requisição (`Item`) deve ser retornado com um novo campo adicional: `uuid`, contendo um identificador único gerado dinamicamente.

## Prompt
Crie um código em Python usando FastAPI para um endpoint que valide e processe um objeto `Item` com os campos:
- `nome`: string, máximo 25 caracteres.
- `valor`: float.
- `data`: date, não superior à data atual.
O endpoint deve:
1. Validar os campos, retornando erros se as regras forem violadas.
2. Retornar o `Item` com um campo adicional `uuid` (identificador único).
Forneça o código completo com dependências (FastAPI, Pydantic, uuid, datetime), validações via Pydantic, comentários explicativos e um exemplo de teste (ex.: cURL). Estruture a resposta com o código e instruções claras.

## Resposta
O código para o endpoint está no arquivo `src/questao4.py`. Abaixo está uma explicação dos passos:

1. **Definir Dependências**:
   - FastAPI para a API, Pydantic para validação, `uuid` para IDs únicos, `datetime` para verificar datas.

2. **Criar Modelo Pydantic**:
   - Definir `Item` com `nome` (máximo 25 caracteres), `valor` (float), e `data` (date).
   - Validar que a data não seja futura.

3. **Implementar Endpoint**:
   - Criar um endpoint POST que valida o `Item`, adiciona um UUID, e retorna o objeto.

4. **Teste**:
   - Instruções de teste estão no código (cURL/Postman).

Consulte `src/questao4.py` para o código completo.