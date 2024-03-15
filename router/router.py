import flet as ft
from urllib.parse import parse_qs, urlparse
from router.routes import ROUTES

from pages.login import Login


class Navigator:
    page: ft.Page

    @classmethod
    def set_page(self, page):
        self.page = page
    
    @classmethod
    def go(self, path, **params):
        self.page.go(path, **params)

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.pages = {
            ROUTES.LOGIN_ROUTE: Login,
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
