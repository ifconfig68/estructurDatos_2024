import requests

url = 'https://solid-space-spork-x5rwgww964v629q5-8000.app.github.dev'

# ejemplo request en GET
#r = requests.get(url)
#print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera']})
print(r.text)