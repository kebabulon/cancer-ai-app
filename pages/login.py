import flet as ft

from router.routes import ROUTES
from router.navigator import Navigator

from providers.data_provider import DataProvider


class Login(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.LOGIN_ROUTE)

        self.patient_id_field = ft.TextField(
            label="ID",
            filled=True,
        )
        self.med_id_field = ft.TextField(
            label="Med ID",
            filled=True,
        )

        def login(e):
            # TODO: do sqlite3 queries here
            result = DataProvider.verify_login(int(patient_id_field.value), int(med_id_field.value))
            if result:
                Navigator.go(ROUTES.DASHBOARD_ROUTE)

        self.controls = [
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Row(
                                controls=[self.patient_id_field]
                            ),
                            ft.Row(
                                controls=[self.med_id_field]
                            ),
                            ft.Row(
                                controls=[ft.ElevatedButton(
                                    text="Войти", on_click=login)]
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        ]
