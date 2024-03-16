import flet as ft

class Stats(ft.Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            ft.Text("stats")            
        ]

        self.rehydrate()


    
    def rehydrate(self):
        pass

