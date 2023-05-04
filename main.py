from fastapi import FastAPI

app = FastAPI()

# Método para saludar
@app.get("/hello")
async def hello():
    return {"message": "Hello FastAPI"}

# Método para determinar si un número es primo
@app.get("/IsPrime/{number}")
async def is_prime(number: int):
    if number < 2:
        return {"is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

# Método para obtener el número fibonacci en una posición dada
@app.get("/fibonacci/{position}")
async def fibonacci(position: int):
    if position < 1:
        return {"error": "La posición debe ser un número entero mayor o igual a 1."}
    elif position == 1 or position == 2:
        return {"fibonacci": 1}
    else:
        a = 1
        b = 1
        for i in range(2, position):
            c = a + b
            a = b
            b = c
        return {"fibonacci": b}
