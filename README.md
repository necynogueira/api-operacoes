
# FastAPI Operations API

Este projeto é uma API simples desenvolvida com [FastAPI](https://fastapi.tiangolo.com/), que realiza operações matemáticas (soma, subtração, multiplicação e divisão).

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar e Ativar o Ambiente Virtual

No Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scriptsctivate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

A aplicação pode ser executada diretamente no terminal com o seguinte comando:

```bash
uvicorn app.main:app --reload
```

## Endpoints Disponíveis

### `/operacao`

Realiza uma operação matemática (soma, subtração, multiplicação ou divisão).

- **Método**: `GET`
- **Parâmetros**:
  - `operacao`: Tipo da operação (`soma`, `subtracao`, `multiplicacao`, `divisao`).
  - `a`: Primeiro número.
  - `b`: Segundo número.
  
- **Exemplo de Requisição**:
  
  ```bash
  http://127.0.0.1:8000/operacao?operacao=soma&a=5&b=3
  ```

- **Exemplo de Resposta**:

  ```json
  {
    "operacao": "soma",
    "resultado": 8
  }
  ```
