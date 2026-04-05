import flet as ft
from datetime import datetime

class PrintView(ft.Column):
    def __init__(self, on_back=None, lista_permisos=None):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        permisos = lista_permisos or []

        btn_volver = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            tooltip="Volver al Panel",
            on_click=lambda e: on_back() if on_back else None
        )

        btn_imprimir = ft.ElevatedButton(
            "Imprimir Documento",
            icon=ft.Icons.PRINT,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_700,
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=12
            ),
            on_click=lambda e: self.imprimir()
        )

        encabezado = ft.Row(
            controls=[
                btn_volver,
                ft.Container(
                    content=ft.Text("Vista de Impresión", size=24, weight="bold", color=ft.Colors.WHITE),
                    expand=True,
                    alignment=ft.Alignment.CENTER_LEFT
                ),
                btn_imprimir
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        barra_superior = ft.Container(
            content=encabezado,
            padding=ft.padding.all(20),
            bgcolor=ft.Colors.BLUE_800,
            border=ft.border.all(2, ft.Colors.BLUE_900),
            border_radius=10,
            offset=ft.Offset(0, -0.5),
            animate_offset=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            opacity=0,
            animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_IN),
        )

        filas_tabla = []
        for idx, p in enumerate(permisos, start=1):
            filas_tabla.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(idx), size=13, color=ft.Colors.BLACK87)),
                        ft.DataCell(ft.Text(
                            f"{p.get('nombres', '')} {p.get('apellidos', '')}",
                            size=13, color=ft.Colors.BLACK87
                        )),
                        ft.DataCell(ft.Text(
                            p.get('cedula', ''),
                            size=13, color=ft.Colors.BLACK87
                        )),
                        ft.DataCell(ft.Text(
                            p.get('grado_jerarquia', ''),
                            size=13, color=ft.Colors.BLACK87
                        )),
                        ft.DataCell(ft.Text(
                            p.get('tipo_permiso', ''),
                            size=13, color=ft.Colors.BLACK87
                        )),
                        ft.DataCell(ft.Text(
                            p.get('fecha_desde', ''),
                            size=13, color=ft.Colors.BLACK87
                        )),
                        ft.DataCell(ft.Text(
                            p.get('fecha_hasta', ''),
                            size=13, color=ft.Colors.BLACK87
                        )),
                    ],
                )
            )

        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("N°", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Nombre Completo", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Cédula", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Jerarquía", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Tipo", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Inicio", weight=ft.FontWeight.BOLD, size=13)),
                ft.DataColumn(ft.Text("Vencimiento", weight=ft.FontWeight.BOLD, size=13)),
            ],
            rows=filas_tabla,
            border_radius=8,
            column_spacing=25,
            heading_row_color=ft.Colors.GREY_100,
            heading_row_height=45,
            data_row_min_height=40,
            data_row_max_height=50,
            divider_thickness=1,
            border=ft.border.all(1, ft.Colors.GREY_300),
        )

        hoy = datetime.now()

        documento = ft.Container(
            content=ft.Column([
                ft.Container(height=20),
                ft.Text(
                    "REGISTRO DE PERMISOS Y COMISIONES",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BLACK87
                ),
                ft.Text(
                    "Sistema de Gestión de Vacaciones",
                    size=13,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=5),
                ft.Divider(height=2, color=ft.Colors.GREY_400),
                ft.Container(height=10),
                ft.Row([
                    ft.Text(f"Fecha de generación: {hoy.strftime('%d/%m/%Y %H:%M')}", size=12, color=ft.Colors.GREY_600),
                    ft.Text(f"Total de registros: {len(permisos)}", size=12, color=ft.Colors.GREY_600),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=15),
                ft.Container(
                    content=tabla,
                    border_radius=8,
                ),
                ft.Container(height=30),
                ft.Divider(height=1, color=ft.Colors.GREY_300),
                ft.Container(height=10),
                ft.Text(
                    "Este documento fue generado automáticamente por el Sistema de Gestión de Vacaciones",
                    size=10,
                    color=ft.Colors.GREY_500,
                    text_align=ft.TextAlign.CENTER,
                    italic=True
                ),
            ], spacing=0, scroll=ft.ScrollMode.AUTO),
            bgcolor=ft.Colors.WHITE,
            padding=ft.padding.all(30),
            border_radius=8,
            border=ft.border.all(1, ft.Colors.GREY_300),
        )

        contenido_animado = ft.Container(
            content=documento,
            padding=ft.padding.all(25),
            expand=True,
            offset=ft.Offset(0, 0.3),
            animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
            opacity=0,
            animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_IN),
        )

        self.controls = [barra_superior, contenido_animado]

        self._barra = barra_superior
        self._contenido = contenido_animado

    def imprimir(self):
        snack = ft.SnackBar(
            ft.Text("Preparando documento para impresión..."),
            bgcolor=ft.Colors.BLUE_700
        )
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def did_mount(self):
        self._barra.opacity = 1
        self._barra.offset = ft.Offset(0, 0)
        self._contenido.opacity = 1
        self._contenido.offset = ft.Offset(0, 0)
        self.page.update()
