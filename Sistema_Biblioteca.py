import datetime
class Usuario:
    def __init__(self, nombre_usuario:str, libros_prestados:str):
        self.nombre_usuario = nombre_usuario
        self.libros_prestados = libros_prestados   
class Biblioteca:
    def __init__(self):
        self.usuarios = []
    def crear_perfil_usuario(self, nombre_usuario:str, contrasena:str):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                print(f"El usuario {nombre_usuario} ya existe.")
                return
        nuevo_usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre_usuario} creado con éxito.")

    def autenticar_usuario(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                print(f"Bienvenido {nombre_usuario}")
                return usuario
        print("Nombre de usuario o contraseña incorrectos.")
        return None

    def cambiar_contrasena(self, nombre_usuario, contrasena_actual, nueva_contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena_actual:
                usuario.cambiar_contrasena(nueva_contrasena)
                return
        print("Nombre de usuario o contraseña actual incorrectos.")
class Bibliotecario:
    def __init__(self, usuario:str,contraseña:str):
        self.usuario=usuario
        self.contraseña=contraseña
class Catalogo:
    def __init__(self):
        pass
class Prestamo:
    def __init__(self, fecha_prestamo:datetime,fecha_devolucion:datetime,libro:str):
        self.fecha_prestamo=fecha_prestamo
        self.fecha_devolucion=fecha_devolucion
        self.libro=libro
class Libro:
    def __init__(self,titulo:str,autor:str,genero:str,ISBN:int):
        self.titulo= titulo
        self.autor= autor
        self.genero= genero
        self.ISBN= ISBN