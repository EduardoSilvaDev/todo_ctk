import customtkinter as ctk
from tkinter import messagebox as msgbox
ctk.set_appearance_mode('dark')

class MainView(ctk.CTk):
    def __init__(self, controller:None):
        super().__init__()
        self.controller = controller
    
    def initialize(self):
        self.layout_config()
        self.layout()
        
    def layout_config(self):
        self.title("List To Do")
        self.center()
        self.protocol('WM_DELETE_WINDOW',self.close)
    def layout(self):
        self.sidebar()
        self.content_default()
    
    def sidebar(self):
        f_sidebar = ctk.CTkFrame(self)
        f_sidebar.pack(side='left',fill='y')
        ctk.CTkButton(f_sidebar,text='Adicionar',command=lambda:msgbox.showwarning('Falta Implementar!',"NOVA TAREFA")).pack(padx=10,pady=(20,5))
        ctk.CTkButton(f_sidebar,text='Adicionar',command=lambda:msgbox.showwarning('Falta Implementar!',"NOVA TAREFA")).pack(padx=10,pady=5)
        ctk.CTkButton(f_sidebar,text='Adicionar',command=lambda:msgbox.showwarning('Falta Implementar!',"NOVA TAREFA")).pack(padx=10,pady=5)
        ctk.CTkButton(f_sidebar,text='Adicionar',command=lambda:msgbox.showwarning('Falta Implementar!',"NOVA TAREFA")).pack(padx=10,pady=5)

        f_bottom = ctk.CTkFrame(f_sidebar,fg_color='transparent')
        f_bottom.pack(side='bottom',fill='x')
        ctk.CTkButton(f_bottom,text='Configurações').pack(padx=10,pady=5)
        ctk.CTkButton(f_bottom,text='Sair',command=self.close).pack(padx=10,pady=5)
    def content_default(self):
        self.f_center = ctk.CTkFrame(self,border_color='darkblue',border_width=2)
        self.f_center.pack(padx=5,pady=5,fill='both',expand=True)
        
        ctk.CTkLabel(self.f_center,text='To Do List').place(relx=0.5,rely=0.5)
        
            
    def open(self):
        self.mainloop()
    def close(self):
        # chamar funcao do controller para fechar a session
        print('Encerrando...')
        self.destroy()
    def center(self):
        self.update_idletasks()
        self.width = 800
        self.height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (self.width / 2))
        y = int((screen_height / 2) - (self.height / 2))
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        
