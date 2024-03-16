import flet as ft
from urllib.parse import parse_qs, urlparse
from router.routes import ROUTES

from pages.login import Login
from pages.dashboard import Dashboard

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.pages = {
            ROUTES.LOGIN_ROUTE: Login,
            ROUTES.DASHBOARD_ROUTE: Dashboard,
        }

    def route_change(self, route):
        _route = urlparse(route.route)
        params = parse_qs(_route.query)
        path = _route.path

        is_pop = params.get("pop", [None])[0]
        if not is_pop:
            self.page.views.clear()

        self.page.views.append(
            self.pages[path]()
        )

        self.page.update()