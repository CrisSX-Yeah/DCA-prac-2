import sys
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

class User:
    user_id_counter = 1
    users = []

    def __init__(self, username, email, password, role):
        self.id = User.user_id_counter
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.messages = []
        User.user_id_counter += 1
        User.users.append(self)

    @staticmethod
    def register():
        print("\n--- Registro de Usuario ---")
        username = input("Nombre de usuario: ")
        email = input("Email: ")
        if not is_valid_email(email):
            print("El email no tiene un formato válido.")
            return None
        password = input("Contraseña: ")
        confirm_password = input("Repite tu contraseña: ")

        if password != confirm_password:
            print("Las contraseñas no coinciden.")
            return None

        role_option = input("Elige el tipo de usuario:\n1. Usuario Normal\n2. Administrador\nOpción: ")
        if role_option == '1':
            role = 'normal'
        elif role_option == '2':
            role = 'administrador'
        else:
            print("Opción no válida.")
            return None

        for user in User.users:
            if user.email == email:
                print("El email ya está registrado.")
                return None

        new_user = User(username, email, password, role)
        print(f"Usuario '{username}' registrado exitosamente.")
        return new_user

    @staticmethod
    def login():
        print("\n--- Inicio de Sesión ---")
        email = input("Email: ")
        if not is_valid_email(email):
            print("El email no tiene un formato válido.")
            return None
        password = input("Contraseña: ")

        for user in User.users:
            if user.email == email and user.password == password:
                print(f"Bienvenido, {user.username} ({'Admin' if user.role == 'administrador' else 'Usuario'}).")
                return user

        print("Email o contraseña incorrectos.")
        return None

class Incidence:
    incidence_id_counter = 1
    incidences = []

    def __init__(self, title, description, author):
        self.id = Incidence.incidence_id_counter
        self.title = title
        self.description = description
        self.author = author
        self.status = 'nueva'  # nueva, abierta, cerrada, rechazada
        self.comments = []
        Incidence.incidence_id_counter += 1
        Incidence.incidences.append(self)

    @staticmethod
    def add_incidence(user):
        if user.role == 'administrador':
            print("\n--- Añadir Nueva Incidencia ---")
        else:
            print("\n--- Informar de una Nueva Incidencia ---")
        title = input("Título: ")
        description = input("Descripción: ")
        new_incidence = Incidence(title, description, user)
        if user.role == 'administrador':
            new_incidence.status = 'abierta'
            print(f"Incidencia '{title}' creada y abierta directamente.")
        else:
            print(f"Incidencia '{title}' creada y enviada para revisión.")
        return new_incidence

    @staticmethod
    def view_incidences(user, status_filter=None, own=False):
        if own:
            incidences = [i for i in Incidence.incidences if i.author == user]
        else:
            incidences = Incidence.incidences

        if status_filter:
            incidences = [i for i in incidences if i.status == status_filter]

        if not incidences:
            print("No hay incidencias para mostrar.")
            return

        # Ordenar incidencias por ID
        incidences.sort(key=lambda x: x.id)

        # Mostrar lista de incidencias
        print("\n--- Lista de Incidencias ---")
        for incidence in incidences:
            print(f"ID: {incidence.id} | Título: {incidence.title} | Autor: {incidence.autor} | Estado: {incidence.status}")

        while True:
            print("\nOpciones:")
            print("1. Elige ID de la incidencia para ver detalles")
            print("0. Volver")
            option = input("Opción: ")

            if option == '1':
                try:
                    incidence_id = int(input("Ingrese el ID de la incidencia: "))
                    selected_incidence = next((i for i in incidences if i.id == incidence_id), None)
                    if selected_incidence:
                        Incidence.show_incidence_details(user, selected_incidence)
                    else:
                        print("ID de incidencia no válido.")
                except ValueError:
                    print("Ingrese un número válido.")
            elif option == '0':
                break
            else:
                print("Opción no válida.")

    @staticmethod
    def show_incidence_details(user, incidence):
        while True:
            print(f"\n--- Detalles de Incidencia ID {incidence.id} ---")
            print(f"Título: {incidence.title}")
            print(f"Estado: {incidence.status}")
            print(f"Autor: {incidence.author.username}")
            print(f"Descripción: {incidence.description}")
            if incidence.comments:
                print("--- Comentarios ---")
                for comment in incidence.comments:
                    role_tag = " (Administrador)" if comment['user'].role == 'administrador' else ""
                    print(f"{comment['user'].username}{role_tag}: {comment['message']}")
            else:
                print("Sin comentarios.")

            print("\nOpciones:")
            if incidence.status == 'abierta' or user.role == 'administrador':
                print("1. Añadir comentario")
            if user.role == 'administrador':
                if incidence.status == 'abierta':
                    print("2. Cerrar incidencia")
                elif incidence.status == 'cerrada':
                    print("2. Reabrir incidencia")
                elif incidence.status == 'nueva':
                    print("2. Abrir incidencia")
                    print("3. Rechazar incidencia")
            print("0. Volver")
            option = input("Opción: ")

            if option == '1' and (incidence.status == 'abierta' or user.role == 'administrador'):
                message = input("Escribe tu comentario: ")
                incidence.comments.append({'user': user, 'message': message})
                print("Comentario añadido.")
            elif option == '2' and user.role == 'administrador':
                if incidence.status == 'abierta':
                    incidence.status = 'cerrada'
                    print("Incidencia cerrada.")
                elif incidence.status == 'cerrada':
                    incidence.status = 'abierta'
                    print("Incidencia reabierta.")
                elif incidence.status == 'nueva':
                    incidence.status = 'abierta'
                    print("Incidencia abierta.")
                    # Enviar mensaje al autor
                    incidence.author.messages.append(f"Tu incidencia '{incidence.title}' ha sido abierta.")
                else:
                    print("Acción no disponible.")
            elif option == '3' and user.role == 'administrador' and incidence.status == 'nueva':
                incidence.status = 'rechazada'
                reason = input("Indica el motivo del rechazo: ")
                # Enviar mensaje al autor
                incidence.author.messages.append(f"Tu incidencia '{incidence.title}' ha sido rechazada. Motivo: {reason}")
                print("Incidencia rechazada.")
            elif option == '0':
                break
            else:
                print("Opción no válida.")

def user_menu(user):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Home")
        if user.role == 'administrador':
            print("2. Añadir nueva incidencia")
            print("3. Ver todas las incidencias")
            print("4. Ver mensajes de los administradores")
            print("5. Ver incidencias abiertas")
            print("6. Ver incidencias cerradas")
            print("7. Ver incidencias entrantes")
        else:
            print("2. Informar de una nueva incidencia")
            print("3. Ver mis incidencias")
            print("4. Ver todas las incidencias")
            print("5. Ver mensajes de los administradores")
        print("0. Cerrar sesión")

        option = input("Opción: ")

        if option == '1':
            print(f"\nBienvenido a la página Home, {user.username}.")
        elif option == '2':
            Incidence.add_incidence(user)
        elif option == '3':
            if user.role == 'administrador':
                Incidence.view_incidences(user)
            else:
                Incidence.view_incidences(user, own=True)
        elif option == '4':
            if user.messages:
                print("\n--- Mensajes de Administradores ---")
                for message in user.messages:
                    print(f"- {message}")
                user.messages.clear()
            else:
                print("No tienes mensajes nuevos.")
        elif option == '5':
            if user.role == 'administrador':
                Incidence.view_incidences(user, status_filter='abierta')
            else:
                Incidence.view_incidences(user, status_filter='abierta')
        elif option == '6' and user.role == 'administrador':
            Incidence.view_incidences(user, status_filter='cerrada')
        elif option == '7' and user.role == 'administrador':
            Incidence.view_incidences(user, status_filter='nueva')
        elif option == '0':
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")

def main_menu():
    while True:
        print("\n--- Local Bug Tracker ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("0. Salir")

        option = input("Opción: ")

        if option == '1':
            User.register()
        elif option == '2':
            user = User.login()
            if user:
                user_menu(user)
        elif option == '0':
            print("Gracias por usar el Local Bug Tracker.")
            # sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main_menu()
