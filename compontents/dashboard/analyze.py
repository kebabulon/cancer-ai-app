import flet as ft

# TODO: maybe change to UserControl
class Analyze(ft.Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            ft.Text("analyze")            
        ]

        self.rehydrate()


    
    def rehydrate(self):
        pass


