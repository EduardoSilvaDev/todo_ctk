

class WindowBase:
    def __init__(self, *args, width=800, height=600, **kwargs):
        super().__init__(*args, **kwargs)  # Chama CTk ou CTkToplevel
        self.width = width
        self.height = height

    def initialize(self):
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.center()

    def open(self):
        self.mainloop()

    def close(self):
        print('Encerrando...')
        self.destroy()

    def center(self):
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.width / 2))
        y = int((screen_height / 2) - (self.height / 2))
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
