import flet as ft
from router.routes import ROUTES
from router.navigator import Navigator

from providers.data_provider import DataProvider
from providers.app_prodiver import AppProvider

from compontents.dashboard.stats import Stats
from compontents.dashboard.analyze import Analyze

class Dashboard(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.DASHBOARD_ROUTE)

        self.stats = Stats()
        self.analyze = Analyze()

        self.active_view = ft.Container(
            content=self.stats
        )

        def change_active_view(view):
            self.active_view.content = view
            self.active_view.update()

        self.appbar = ft.AppBar(
            title=ft.Text("Dashboard"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Журнал", on_click=lambda _: change_active_view(self.stats)),
                        ft.ElevatedButton("Анализ", on_click=lambda _: change_active_view(self.analyze))
                    ]
                )
            ]

        )

        self.controls = [
            self.active_view,
        ]
    
    def rehydrate(self):
        # update stats from pop up using page.views[0]
        self.stats.update()
        pass