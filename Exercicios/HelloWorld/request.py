import requests

url = "https://jsonplaceholder.typicode.com/users/1"  # API pública de exemplo
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Nome: {data['name']}")
    print(f"E-mail: {data['email']}")
    print(f"Cidade: {data['address']['city']}")
else:
    print("Erro ao buscar dados:", response.status_code)
