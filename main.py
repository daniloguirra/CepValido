import requests
from acesso_cep import BuscaEndereco

cep = 48903170
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json")
# print(r.text)

bairro, cidade, uf = objeto_cep.acesso_via_cep()
print("\n")
print(bairro, cidade, uf)

