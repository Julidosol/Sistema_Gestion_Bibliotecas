import Sistema_Biblioteca
if __name__ == "__main__":
    biblioteca = Sistema_Biblioteca.Biblioteca()

    while True:
        print("\n Bienvenido A Bibliotech")
        print("1. Crear perfil de usuario")
        print("2. Iniciar sesión")
        print("3. Cambiar contraseña")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_usuario = input("Introduce el nombre de usuario: ")
            contrasena = input("Introduce la contraseña: ")
            biblioteca.crear_perfil_usuario(nombre_usuario, contrasena)

        elif opcion == "2":
            nombre_usuario = input("Introduce el nombre de usuario: ")
            contrasena = input("Introduce la contraseña: ")
            usuario = biblioteca.autenticar_usuario(nombre_usuario, contrasena)

        elif opcion == "3":
            nombre_usuario = input("Introduce el nombre de usuario: ")
            contrasena_actual = input("Introduce la contraseña actual: ")
            nueva_contrasena = input("Introduce la nueva contraseña: ")
            biblioteca.cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")