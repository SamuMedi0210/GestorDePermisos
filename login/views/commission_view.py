import flet as ft
from datetime import datetime

class CommissionView(ft.Column):
    def __init__(self, on_back=None, lista_permisos=None):
        super().__init__()
        self.expand = True
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        permisos = lista_permisos or []
        hoy = datetime.now().date()

        permisos_activos = []
        for p in permisos:
            try:
                fecha_hasta = datetime.strptime(p.get("fecha_hasta", ""), "%d/%m/%Y").date()
                if fecha_hasta >= hoy:
                    permisos_activos.append(p)
            except:
                pass

        btn_volver = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            tooltip="Volver al Panel",
            on_click=lambda e: on_back() if on_back else None
        )

        encabezado = ft.Row(
            controls=[
                btn_volver,
                ft.Container(
                    content=ft.Text("Personal en Comisión", size=24, weight="bold", color=ft.Colors.WHITE),
                    expand=True,
                    alignment=ft.Alignment.CENTER_LEFT
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        barra_superior = ft.Container(
            content=encabezado,
            padding=ft.padding.all(20),
            bgcolor=ft.Colors.ORANGE_800,
            border=ft.border.all(2, ft.Colors.ORANGE_900),
            border_radius=10,
            offset=ft.Offset(0, -0.5),
            animate_offset=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            opacity=0,
            animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_IN),
        )

        filas = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(
                        f"{p.get('nombres', '')} {p.get('apellidos', '')}",
                        size=14, color=ft.Colors.WHITE, weight=ft.FontWeight.W_500
                    )),
                    ft.DataCell(ft.Text(
                        p.get('grado_jerarquia', ''),
                        size=13, color=ft.Colors.WHITE
                    )),
                    ft.DataCell(ft.Text(
                        p.get('cargo', ''),
                        size=13, color=ft.Colors.WHITE
                    )),
                    ft.DataCell(ft.Container(
                        content=ft.Text(p.get('tipo_permiso', ''), size=12, color=ft.Colors.BLUE_800),
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=6,
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    )),
                    ft.DataCell(ft.Container(
                        content=ft.Text(p.get("fecha_desde", ""), size=13, color=ft.Colors.GREEN_800),
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=6,
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    )),
                    ft.DataCell(ft.Container(
                        content=ft.Text(p.get("fecha_hasta", ""), size=13, color=ft.Colors.RED_800),
                        bgcolor=ft.Colors.RED_50,
                        border_radius=6,
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    )),
                ],
                color={ft.ControlState.HOVERED: ft.Colors.ORANGE_50}
            )
            for p in permisos_activos
        ]

        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nombre Completo", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
                ft.DataColumn(ft.Text("Jerarquía", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
                ft.DataColumn(ft.Text("Cargo", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
                ft.DataColumn(ft.Text("Tipo de Permiso", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
                ft.DataColumn(ft.Text("Inicio", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
                ft.DataColumn(ft.Text("Vencimiento", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, size=13)),
            ],
            rows=filas,
            border_radius=10,
            column_spacing=30,
            heading_row_color=ft.Colors.ORANGE_800,
            heading_row_height=50,
            data_row_min_height=48,
            data_row_max_height=60,
            divider_thickness=1,
        )

        if not permisos_activos:
            cuerpo = ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Icon(ft.Icons.PEOPLE_OUTLINE, size=70, color=ft.Colors.GREY_300),
                    ft.Text("No hay personal en comisión actualmente.", color=ft.Colors.GREY_400, size=16),
                    ft.Text(
                        "Los permisos activos aparecerán aquí.",
                        color=ft.Colors.GREY_300, size=13
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        else:
            cuerpo = ft.Column(
                controls=[
                    ft.Container(height=8),
                    ft.Row([
                        ft.Text(
                            f"Personal Activo en Comisión  ({len(permisos_activos)})",
                            size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
                        ),
                        ft.Container(
                            content=ft.Text(f"Hoy: {hoy.strftime('%d/%m/%Y')}", size=13, color=ft.Colors.ORANGE_800),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=6,
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                        )
                    ], spacing=15),
                    ft.Container(
                        content=tabla,
                        border_radius=12,
                        border=ft.border.all(1, ft.Colors.ORANGE_200),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
                expand=True
            )

        contenido_animado = ft.Container(
            content=cuerpo,
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

    def did_mount(self):
        self._barra.opacity = 1
        self._barra.offset = ft.Offset(0, 0)
        self._contenido.opacity = 1
        self._contenido.offset = ft.Offset(0, 0)
        self.page.update()
