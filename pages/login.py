import flet as ft
from router.routes import ROUTES

class Login(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.LOGIN_ROUTE)

        self.appbar = ft.AppBar(
            title=ft.Text("Login")
        )

        self.controls = [
            ft.Text("test"),
        ]
        