import requests

r = requests.get('http://pulse-rest-testing.herokuapp.com/')
print(r)

b = requests.post('http://pulse-rest-testing.herokuapp.com/books', data={'title': 'Big book', 'author': 'Herman'})
print(b.text)
r = b.json()
id = r['id']
# id = 1581
b = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id}')
b = requests.put(f'http://pulse-rest-testing.herokuapp.com/books/{id}', data={'title': 'Books'})
b = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id}')
print(b)
b = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/')
r = b.json()
for key in r:
    if (key['id']) == id:
        print('есть книга в списке')
    if (key['title']) == 'Books':
        print('книга изминилась в списке')

b = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id}')
print(b.text)

rol = requests.post('http://pulse-rest-testing.herokuapp.com/roles',
                    data={'name': 'Why', 'type': 'type1', 'level': 12, 'book': id})
rol1 = rol.json()
id_rol = rol1['id']
# id_rol = 131
rol = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/{id_rol}')
rolj = rol.json()
print(rolj)
b = requests.put(f'http://pulse-rest-testing.herokuapp.com/roles/{id_rol}',
                 data={'name': 'Why1', 'type': 'type2', 'level': 15})

rol = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/{id_rol}')
rolj = rol.json()
print(rolj)

b = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{id}')
rol = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/{id_rol}')

