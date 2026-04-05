from models.permiso_model import PermisoModel
from datetime import datetime, timedelta

def seed_permisos():
    PermisoModel.create_table()

    permisos_existentes = PermisoModel.get_all()
    if len(permisos_existentes) > 0:
        return

    hoy = datetime.now().date()

    datos_ejemplo = [
        {
            "nombres": "Juan",
            "apellidos": "Pérez García",
            "cedula": "12345678",
            "telefono": "0414-1234567",
            "grado_jerarquia": "Capitán",
            "cargo": "Comandante de Pelotón",
            "tipo_permiso": "Vacacional",
            "fecha_elaboracion": hoy.strftime("%d/%m/%Y"),
            "fecha_desde": (hoy + timedelta(days=5)).strftime("%d/%m/%Y"),
            "fecha_hasta": (hoy + timedelta(days=20)).strftime("%d/%m/%Y"),
            "dir_domiciliaria": "Calle Principal 123, Apartado",
            "dir_emergencia": "Calle Principal 123, Apartado",
            "observaciones": "Permiso aprobado"
        },
        {
            "nombres": "María",
            "apellidos": "López Martínez",
            "cedula": "87654321",
            "telefono": "0424-9876543",
            "grado_jerarquia": "Sargento",
            "cargo": "Especialista en Comunicaciones",
            "tipo_permiso": "Extraordinario",
            "fecha_elaboracion": hoy.strftime("%d/%m/%Y"),
            "fecha_desde": (hoy - timedelta(days=2)).strftime("%d/%m/%Y"),
            "fecha_hasta": (hoy + timedelta(days=10)).strftime("%d/%m/%Y"),
            "dir_domiciliaria": "Avenida Central 456, Maracay",
            "dir_emergencia": "Avenida Central 456, Maracay",
            "observaciones": "Comisión activa"
        },
        {
            "nombres": "Carlos",
            "apellidos": "Rodríguez Fuentes",
            "cedula": "11223344",
            "telefono": "0416-5554444",
            "grado_jerarquia": "Teniente",
            "cargo": "Jefe de Operaciones",
            "tipo_permiso": "Vacacional",
            "fecha_elaboracion": hoy.strftime("%d/%m/%Y"),
            "fecha_desde": (hoy + timedelta(days=15)).strftime("%d/%m/%Y"),
            "fecha_hasta": (hoy + timedelta(days=30)).strftime("%d/%m/%Y"),
            "dir_domiciliaria": "Calle del Este 789, Valencia",
            "dir_emergencia": "Calle del Este 789, Valencia",
            "observaciones": "Pendiente de confirmación"
        },
        {
            "nombres": "Ana",
            "apellidos": "González Hernández",
            "cedula": "55667788",
            "telefono": "0412-3332221",
            "grado_jerarquia": "Cabo",
            "cargo": "Operador de Sistemas",
            "tipo_permiso": "Reposo",
            "fecha_elaboracion": hoy.strftime("%d/%m/%Y"),
            "fecha_desde": (hoy - timedelta(days=5)).strftime("%d/%m/%Y"),
            "fecha_hasta": (hoy - timedelta(days=1)).strftime("%d/%m/%Y"),
            "dir_domiciliaria": "Urb. Las Mercedes 321, Barquisimeto",
            "dir_emergencia": "Urb. Las Mercedes 321, Barquisimeto",
            "observaciones": "Finalizado"
        },
        {
            "nombres": "Roberto",
            "apellidos": "Silva Jiménez",
            "cedula": "99887766",
            "telefono": "0414-7778889",
            "grado_jerarquia": "Mayor",
            "cargo": "Subdirector de Recursos",
            "tipo_permiso": "Paternal",
            "fecha_elaboracion": hoy.strftime("%d/%m/%Y"),
            "fecha_desde": (hoy - timedelta(days=10)).strftime("%d/%m/%Y"),
            "fecha_hasta": (hoy + timedelta(days=25)).strftime("%d/%m/%Y"),
            "dir_domiciliaria": "Avenida Libertador 1000, Caracas",
            "dir_emergencia": "Avenida Libertador 1000, Caracas",
            "observaciones": "Licencia parental activa"
        },
    ]

    for datos in datos_ejemplo:
        PermisoModel.save(datos)

if __name__ == "__main__":
    seed_permisos()
    print("Datos de prueba insertados correctamente")
