# Guía de Uso - Sistema de Gestión de Vacaciones

## Inicio Rápido

### 1. Iniciar la Aplicación

```bash
./start.sh
```

O manualmente:

```bash
cd login
flet run main.py
```

La aplicación se abrirá en: **http://127.0.0.1:8000**

### 2. Iniciar Sesión

- **Usuario**: `admin`
- **Contraseña**: `1234`

Presiona "Iniciar Sesión"

## Panel de Administrador

Una vez iniciada la sesión, accederás al panel principal donde verás:

- **Tabla de Permisos**: Lista de todos los permisos registrados
- **Menú (☰)**: Opciones principales
- **Buscador**: Busca rápidamente permisos

### Acciones Disponibles

#### Agregar Nuevo Permiso

1. Haz clic en el menú (☰)
2. Selecciona "Agregar Permiso"
3. Completa el formulario:
   - Nombres y Apellidos (obligatorio)
   - Cédula (obligatorio)
   - Teléfono (obligatorio)
   - Grado de Jerarquía (obligatorio)
   - Cargo (obligatorio)
   - Tipo de Permiso (obligatorio)
   - Fechas (obligatorio)
   - Información de contacto y observaciones

4. Presiona "Guardar"

#### Editar Permiso Existente

1. En la tabla de permisos, busca el registro
2. Haz clic en el icono de lápiz (Editar)
3. Modifica los datos necesarios
4. Presiona "Guardar"

#### Eliminar Permiso

1. En la tabla de permisos, busca el registro
2. Haz clic en el icono de basura (Eliminar)
3. Confirma la eliminación

## Vista de Personal en Comisión

Para ver quién está actualmente en comisión:

1. Haz clic en el menú (☰)
2. Selecciona "Personal en Comisión"

**Características:**
- Solo muestra personal con permisos vigentes (fecha de vencimiento ≥ hoy)
- Muestra: nombre, jerarquía, cargo, tipo de permiso y fechas
- Contador de personal activo
- Fecha actual visible

**Ejemplo:**
- Juan Pérez (permiso hasta el 20/04/2026): VISIBLE
- Ana González (permiso vencido el 03/04/2026): NO VISIBLE

## Vista de Impresión

Para generar un documento listo para imprimir:

1. Haz clic en el menú (☰)
2. Selecciona "Imprimir Registros"

**Características:**
- Documento profesional con encabezado
- Tabla completa de todos los permisos
- Información de fecha de generación
- Total de registros
- Formato optimizado para impresora

**Para imprimir:**
- Usa Ctrl+P (o Cmd+P en Mac)
- Selecciona la impresora
- Ajusta configuración según necesites

## Tipos de Permiso

| Tipo | Descripción |
|------|------------|
| Extraordinario | Permisos especiales no programados |
| Vacacional | Vacaciones anuales |
| Pre Maternal | Antes del parto |
| Post Maternal | Después del parto |
| Paternal | Licencia por paternidad |
| Operacional | Comisión operativa |
| Reposo | Descanso médico |

## Datos de Ejemplo Cargados

Se incluyen 5 registros de ejemplo:

1. **Juan Pérez García** - Capitán (Vacacional)
   - Vigencia: 10/04/2026 - 20/04/2026 ✓ ACTIVO

2. **María López Martínez** - Sargento (Extraordinario)
   - Vigencia: 03/04/2026 - 13/04/2026 ✓ ACTIVO

3. **Carlos Rodríguez Fuentes** - Teniente (Vacacional)
   - Vigencia: 20/04/2026 - 05/05/2026

4. **Ana González Hernández** - Cabo (Reposo)
   - Vigencia: 01/04/2026 - 03/04/2026 ✗ VENCIDO

5. **Roberto Silva Jiménez** - Mayor (Paternal)
   - Vigencia: 01/04/2026 - 25/04/2026 ✓ ACTIVO

## Consejos

- Los cambios se guardan automáticamente
- Las fechas deben ingresarse en formato DD/MM/AAAA
- Usa el buscador para encontrar rápidamente personal
- La vista de comisiones se actualiza automáticamente
- Los documentos de impresión incluyen la fecha actual

## Solución de Problemas

**No puedo iniciar sesión:**
- Verifica que escribas exactamente: usuario `admin` y contraseña `1234`
- Recuerda que es sensible a mayúsculas/minúsculas

**Los datos no se guardan:**
- Asegúrate de hacer clic en "Guardar"
- Verifica que todos los campos obligatorios estén completos

**No puedo imprimir:**
- Intenta abrir en Google Chrome o Firefox
- Usa Ctrl+P para abrir el diálogo de impresión
- Verifica la configuración de la impresora

## Contacto y Soporte

Para reportar problemas o sugerencias, contacta al administrador del sistema.
