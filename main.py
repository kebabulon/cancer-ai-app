import flet as ft
from router.router import Router
from providers.data_provider import DataProvider

def main(page: ft.Page):
    page.title = "CancerAI"

    page.window_min_width = 1250
    page.window_min_height = 760
    
    page.window_width = page.window_min_width
    page.window_height = page.window_min_height

    router = Router(page)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = router.route_change
    page.on_view_pop = view_pop

    DataProvider.initialize()

    page.go("/login")


ft.app(target=main)