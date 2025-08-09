import customtkinter as ctk
from tkinter import messagebox as msgbox
from app.Util.window_base import *
ctk.set_appearance_mode('dark')

class MainView(WindowBase, ctk.CTk):
    def __init__(self, controller=None, **kwargs):
        super().__init__(width=800, height=600, **kwargs)
        self.controller = controller
        self.tp_add = None
        
    def initialize(self):
        self.layout_config()
        super().initialize()
        self.layout()
        
    def layout_config(self):
        self.title("List To Do")
        self.center()
        self.protocol('WM_DELETE_WINDOW',self.close)
        self.width = 800
        self.height = 600
        
    def layout(self):
        self.sidebar()
        self.content_default()
    
    def sidebar(self):
        f_sidebar = ctk.CTkFrame(self)
        f_sidebar.pack(side='left',fill='y')
        ctk.CTkButton(f_sidebar,text='Adicionar',command=self.add_item).pack(padx=10,pady=(20,5))

        f_bottom = ctk.CTkFrame(f_sidebar,fg_color='transparent')
        f_bottom.pack(side='bottom',fill='x')
        ctk.CTkButton(f_bottom,text='Configurações').pack(padx=10,pady=5)
        ctk.CTkButton(f_bottom,text='Sair',command=self.close).pack(padx=10,pady=5)
        
    def content_default(self):
        self.f_center = ctk.CTkFrame(self,border_color='darkblue',border_width=2)
        self.f_center.pack(padx=5,pady=5,fill='both',expand=True)
        
        ctk.CTkLabel(self.f_center,text='To Do List').place(relx=0.5,rely=0.5)
        
      
    def add_item(self):
        new_user_window = TP_Adicionar(self, self.controller)
        new_user_window.grab_set()
        new_user_window.focus_set()
        new_user_window.wait_window()
        

class TP_Adicionar(WindowBase, ctk.CTkToplevel):
    def __init__(self, parent, controller=None, **kwargs):
        super().__init__(parent, width=600, height=400, **kwargs)

        self.controller = controller
        self.initialize()

        self.title('Adicionar Item')
        ctk.CTkLabel(self, text='Adicionar').pack()
        ctk.CTkButton(self, text="Clique aqui", command=lambda: print('Clique Aqui')).pack()
