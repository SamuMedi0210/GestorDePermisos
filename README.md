# Sistema de Gestión de Vacaciones y Comisiones

Aplicación de escritorio para la gestión integral de permisos, vacaciones y comisiones de personal militar.

## Características

- **Gestión de Permisos**: Crear, editar y eliminar registros de permisos y vacaciones
- **Vista de Comisiones**: Visualizar personal actualmente en comisión
- **Impresión de Registros**: Generar documentos listos para imprimir con todos los permisos
- **Interfaz Intuitiva**: Diseño moderno con animaciones suaves
- **Base de Datos Local**: Almacenamiento seguro en SQLite

## Requisitos

- Python 3.8 o superior
- Flet framework

## Instalación y Ejecución

### Instalación de dependencias

```bash
python3 -m pip install --break-system-packages flet flet-cli flet-desktop flet-web
```

### Ejecutar la aplicación

Desde el directorio del proyecto:

```bash
cd login
flet run main.py
```

La aplicación se abrirá automáticamente en `http://127.0.0.1:8000`

## Credenciales de Acceso

- **Usuario**: `admin`
- **Contraseña**: `1234`

## Funcionalidades

### Panel de Administrador
- Visualizar todos los permisos registrados en una tabla
- Agregar nuevos permisos
- Editar permisos existentes
- Eliminar registros

### Personal en Comisión
- Ver únicamente el personal con permisos activos (vigentes hoy)
- Información completa: nombre, jerarquía, cargo, tipo de permiso y fechas
- Interfaz con indicador visual de permisos activos

### Vista de Impresión
- Generar documento profesional con todos los permisos registrados
- Formato listo para imprimir en papel
- Incluye fecha de generación y conteo de registros
- Tabla completa con información detallada

## Estructura del Proyecto

```
login/
├── main.py                    # Punto de entrada de la aplicación
├── seed_data.py              # Datos de prueba
├── controllers/
│   └── main_controller.py    # Lógica de navegación y control
├── models/
│   ├── user_model.py         # Modelo de usuarios
│   └── permiso_model.py      # Modelo de permisos (CRUD)
├── views/
│   ├── login_view.py         # Vista de login
│   ├── admin_view.py         # Panel de administrador
│   ├── permission_view.py    # Formulario de permisos
│   ├── commission_view.py    # Vista de comisiones activas
│   └── print_view.py         # Vista de impresión
└── data/
    └── permisos.db           # Base de datos SQLite
```

## Datos de Ejemplo

Al iniciar la aplicación por primera vez, se cargarán automáticamente 5 registros de prueba con personal en diferentes estados de comisión.

## Tipos de Permiso Disponibles

- Extraordinario
- Vacacional
- Pre Maternal
- Post Maternal
- Paternal
- Operacional
- Reposo

## Notas

- Todos los permisos se almacenan localmente en la base de datos SQLite
- Los cambios se guardan automáticamente
- Las fechas se manejan en formato DD/MM/AAAA
- La vista de comisiones solo muestra permisos con fecha de vencimiento ≥ fecha actual
