# tarefa2_matheus_martins_guerra

'''  importanto libreria '''

from faker import Faker

import random

fake = Faker()


usuarios = {}


''' generando usuarios '''

for id_usuario in range(1, 16):
    nombre = fake.unique.name()
    direccion = fake.unique.address().replace("\n", ", ")
    correo = fake.unique.email()
    telefono = fake.unique.phone_number()

    ''' Almacenando los datos de los usuarios en el diccionario '''

    usuarios[id_usuario] = {
        'nombre': nombre,
        'direccion': direccion,
        'correo': correo,
        'telefono': telefono
    }


''' enseñando los datos de los usuarios '''

for id_usuario, datos in usuarios.items():
    print(f"ID {id_usuario}: {datos}" + '\n')


print('\n' + '*' * 26)
print('*' * 2, 'Eligiendo el usuario', '*' * 2)
print('*' * 26 + '\n')


''' eligiendo usuario aleatoriamente '''

afortunado = random.choice(list(usuarios.values()))
print(f"O usuario chamado {afortunado['nombre']} foi o afortunado!")
