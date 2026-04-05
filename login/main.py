import flet as ft
from views.login_view import LoginView
from controllers.main_controller import MainController
from seed_data import seed_permisos

def main(page: ft.Page):
    page.title = "Sistema de Vacaciones"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    seed_permisos()

    main_controller = MainController(page)

    login_view = LoginView(on_login_click=main_controller.attempt_login)

    main_controller.set_login_view(login_view)

    page.add(login_view)

if __name__ == "__main__":
    ft.run(main)
