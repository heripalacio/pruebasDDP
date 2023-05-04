import requests

# Prueba del método "hello"
response = requests.get("http://localhost:8000/hello")
assert response.status_code == 200
assert response.json() == {"message": "Hello FastAPI"}

# Prueba del método "is_prime"
response = requests.get("http://localhost:8000/IsPrime/17")
assert response.status_code == 200
assert response.json() == {"is_prime": True}

response = requests.get("http://localhost:8000/IsPrime/21")
assert response.status_code == 200
assert response.json() == {"is_prime": False}

