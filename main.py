# tarefa2_matheus_martins_guerra
from faker import Faker


fake = Faker()


usuarios = {}


for id_usuario in range(1, 16):
    nombre = fake.unique.name()
    direccion = fake.unique.address().replace("\n", ", ")
    correo = fake.unique.email()
    telefono = fake.unique.phone_number()


    usuarios[id_usuario] = {
        'nombre': nombre,
        'direccion': direccion,
        'correo': correo,
        'telefono': telefono
    }


for id_usuario, datos in usuarios.items():
    print(f"ID {id_usuario}: {datos}" + '\n')
