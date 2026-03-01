# Importamos el modelo Libro desde la app biblioteca
from biblioteca.models import Libro

# Importamos herramientas para SQL y anotaciones
from django.db import connection
from django.db.models import Count


# =====================================================
# 1. RECUPERACIÓN DE REGISTROS
# =====================================================

# Recupera todos los libros registrados en la base de datos
libros = Libro.objects.all()

# Recupera solo los libros cuyo autor sea "Gabriel García Márquez"
libros_garcia_marquez = Libro.objects.filter(
    autor="Gabriel García Márquez"
)

# Recupera los libros que tienen más de 200 páginas
libros_mas_200_paginas = Libro.objects.filter(
    paginas__gt=200
)


# =====================================================
# 2. FILTROS Y EXCLUSIONES
# =====================================================

# Aplica un filtro para mostrar solo libros disponibles
libros_disponibles = Libro.objects.filter(
    disponible=True
)

# Excluye todos los libros que tengan menos de 100 páginas
libros_menos_100_paginas = Libro.objects.exclude(
    paginas__lt=100
)


# =====================================================
# 3. CONSULTAS PERSONALIZADAS CON SQL
# =====================================================

# Ejecuta una consulta SQL directa utilizando raw()
# Devuelve objetos del modelo Libro ordenados por título
libros_ordenados_sql = Libro.objects.raw(
    "SELECT * FROM biblioteca_libro ORDER BY titulo"
)

# Ejecuta una consulta SQL personalizada usando connection.cursor()
# Cuenta cuántos libros hay por autor
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT autor, COUNT(*) 
        FROM biblioteca_libro
        GROUP BY autor
    """)
    conteo_por_autor = cursor.fetchall()


# =====================================================
# 4. CAMPOS ESPECÍFICOS Y ANOTACIONES
# =====================================================

# Recupera solo los títulos de todos los libros
titulos_libros = Libro.objects.values('titulo')

# Agrega una anotación para contar cuántos libros hay por autor
libros_por_autor = Libro.objects.values(
    'autor'
).annotate(
    total_libros=Count('id')
)