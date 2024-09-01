# Clase que representa un libro
class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase que representa un usuario de la biblioteca
class Usuario:
    def _init_(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def _str_(self):
        return f"Usuario {self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join([str(libro) for libro in self.libros_prestados])


# Clase que representa la biblioteca
class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}  # ISBN como clave, Libro como valor
        self.usuarios_registrados = {}  # ID de usuario como clave, Usuario como valor
        self.ids_usuarios = set()  # Conjunto para mantener IDs únicos de usuarios

    # Añadir un libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    # Dar de baja a un usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado del sistema.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"No se encontró un libro con ISBN {isbn}.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        libro = self.libros_disponibles[isbn]
        usuario.prestar_libro(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    # Devolver un libro de un usuario
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario {usuario.nombre} no tiene un libro con ISBN {isbn}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, filtro, criterio):
        resultados = []
        for libro in self.libros_disponibles.values():
            if filtro == "titulo" and criterio.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif filtro == "autor" and criterio.lower() in libro.autor.lower():
                resultados.append(libro)
            elif filtro == "categoria" and criterio.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados de un usuario
    def listar_libros_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            return f"Usuario con ID {id_usuario} no encontrado."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Añadir libros a la biblioteca
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción", "123456789")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "987654321")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar un usuario
    usuario1 = Usuario("Juan Pérez", 1)
    biblioteca.registrar_usuario(usuario1)

    # Prestar un libro
    biblioteca.prestar_libro(1, "123456789")

    # Listar libros prestados del usuario
    print(usuario1.listar_libros_prestados())

    # Devolver el libro
    biblioteca.devolver_libro(1, "123456789")

    # Buscar libros por título
    resultados_busqueda = biblioteca.buscar_libros("titulo", "Cien años")
    for libro in resultados_busqueda:
        print(libro)