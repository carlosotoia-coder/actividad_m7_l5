apple@Apples-MacBook-Pro actividad_m7_l5 % python3 -m venv venv 
apple@Apples-MacBook-Pro actividad_m7_l5 % source venv/bin/activate
(venv) apple@Apples-MacBook-Pro actividad_m7_l5 % pip install django
Collecting django
  Using cached django-6.0.2-py3-none-any.whl.metadata (3.9 kB)
Collecting asgiref>=3.9.1 (from django)
  Using cached asgiref-3.11.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.5.0 (from django)
  Using cached sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Using cached django-6.0.2-py3-none-any.whl (8.3 MB)
Using cached asgiref-3.11.1-py3-none-any.whl (24 kB)
Using cached sqlparse-0.5.5-py3-none-any.whl (46 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.11.1 django-6.0.2 sqlparse-0.5.5

[notice] A new release of pip is available: 25.2 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
(venv) apple@Apples-MacBook-Pro actividad_m7_l5 % pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (25.2)
Collecting pip
  Using cached pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-26.0.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.2
    Uninstalling pip-25.2:
      Successfully uninstalled pip-25.2
Successfully installed pip-26.0.1
(venv) apple@Apples-MacBook-Pro actividad_m7_l5 % django-admin startproject config proyecto_libros 
(venv) apple@Apples-MacBook-Pro actividad_m7_l5 % django-admin startapp biblioteca 
(venv) apple@Apples-MacBook-Pro actividad_m7_l5 % cd proyecto_libros
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py makemigrations 
Traceback (most recent call last):
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/proyecto_libros/manage.py", line 22, in <module>
    main()
    ~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/proyecto_libros/manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/core/management/__init__.py", line 443, in execute_from_command_line
    utility.execute()
    ~~~~~~~~~~~~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/core/management/__init__.py", line 417, in execute
    django.setup()
    ~~~~~~~~~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/apps/config.py", line 193, in create
    import_module(entry)
    ~~~~~~~~~~~~~^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'biblioteca'
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py startapp biblioteca
Traceback (most recent call last):
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/proyecto_libros/manage.py", line 22, in <module>
    main()
    ~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/proyecto_libros/manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/core/management/__init__.py", line 443, in execute_from_command_line
    utility.execute()
    ~~~~~~~~~~~~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/core/management/__init__.py", line 417, in execute
    django.setup()
    ~~~~~~~~~~~~^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/Users/apple/Desktop/actividad_m7_l5/actividad_m7_l5/venv/lib/python3.13/site-packages/django/apps/config.py", line 193, in create
    import_module(entry)
    ~~~~~~~~~~~~~^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'biblioteca'
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py startapp biblioteca 
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py makemigrations
No changes detected
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py makemigrations
Migrations for 'biblioteca':
  biblioteca/migrations/0001_initial.py
    + Create model Libro
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, biblioteca, contenttypes, sessions
Running migrations:
  Applying biblioteca.0001_initial... OK
(venv) apple@Apples-MacBook-Pro proyecto_libros % python manage.py shell
13 objects imported automatically (use -v 2 for details).

Cmd click to launch VS Code Native REPL
Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from biblioteca.models import Libro
>>> Libro.objects.all()
<QuerySet []>
>>> # Crear libros de prueba
>>> Libro.objects.create(
...     titulo="Cien años de soledad",
...     autor="Gabriel García Márquez",
...     paginas=417,
...     disponible=True
... )
<Libro: Cien años de soledad>
>>> 
>>> Libro.objects.create(
...     titulo="El amor en los tiempos del cólera",
...     autor="Gabriel García Márquez",
...     paginas=348,
...     disponible=True
... )
<Libro: El amor en los tiempos del cólera>
>>> 
>>> Libro.objects.create(
...     titulo="1984",
...     autor="George Orwell",
...     paginas=328,
...     disponible=False
... )
<Libro: 1984>
>>> 
>>> Libro.objects.create(
...     titulo="El principito",
...     autor="Antoine de Saint-Exupéry",
...     paginas=96,
...     disponible=True
... )Libro.objects.all()
  File "<console>", line 6
    )Libro.objects.all()
     ^^^^^
SyntaxError: invalid syntax
>>> Libro.objects.all()
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>, <Libro: 1984>]>
>>> Libro.objects.all()
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>, <Libro: 1984>]>
>>> Libro.objects.filter(autor="Gabriel García Márquez")
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>]>
>>> Libro.objects.filter(paginas__gt=200)
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>, <Libro: 1984>]>
>>> Libro.objects.filter(disponible=True)
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>]>
>>> Libro.objects.exclude(paginas__lt=100)
<QuerySet [<Libro: Cien años de soledad>, <Libro: El amor en los tiempos del cólera>, <Libro: 1984>]>
>>> from django.db.models import Count
>>> Libro.objects.values('autor').annotate(total=Count('id'))
<QuerySet [{'autor': 'Gabriel García Márquez', 'total': 2}, {'autor': 'George Orwell', 'total': 1}]>
>>> exit()
now exiting InteractiveConsole...
(venv) apple@Apples-MacBook-Pro proyecto_libros % 