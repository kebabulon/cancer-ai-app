import flet as ft

class Navigator:
    page: ft.Page

    @classmethod
    def initialize(self, page):
        self.page = page
    
    @classmethod
    def go(self, path, **params):
        self.page.go(path, **params)
