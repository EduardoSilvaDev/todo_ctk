from app.views.main_view import MainView

class Controller:
    def __init__(self):
        self.view = MainView(self)
    
    def show(self):
        self.view.initialize()
        self.view.open()
        