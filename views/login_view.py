import flet as ft
from flet_route import Params, Basket
from flet import ElevatedButton, TextField, Checkbox, Text, Row, Column, TextButton
from flet_core.control_event import ControlEvent

def login(page:ft.Page,params:Params,basket:Basket):
    page.title = "login"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_resizable = True
    
    #Fields
    username = TextField(label="Username",text_align=ft.TextAlign.LEFT,border_radius=20,bgcolor="#f5f5f5")
    password = TextField(label="Password",text_align=ft.TextAlign.LEFT,border_radius=20,password=True,bgcolor="#f5f5f5")
    tncs = Checkbox(label="show password",value=False)
    button_submit = ElevatedButton(text="login",disabled=True,bgcolor="#808080",color="#ffffff")
    dhaa = Text(value="Don't have an account?",color="#808080")
    forgot_password_text = Text(value="forgot password?",color="#808080")
    signup_text = TextButton(text="signup",style=ft.ButtonStyle(ft.colors.BLUE))
    reset_text = TextButton(text="reset",style=ft.ButtonStyle(ft.colors.BLUE))
    
    #Create rows
    button_row = Row(spacing=10,alignment=ft.MainAxisAlignment.CENTER)
    username_row = Row(spacing=10,alignment=ft.MainAxisAlignment.CENTER)
    password_row = Row(spacing=5,alignment=ft.MainAxisAlignment.CENTER)
    show_password_row = Row(spacing=5,alignment=ft.MainAxisAlignment.CENTER)
    dhaa_row = Row(spacing=0,alignment=ft.MainAxisAlignment.CENTER)
    forgot_password_row = Row(spacing=0,alignment=ft.MainAxisAlignment.CENTER)
    #Add button to row
    button_row.controls.append(button_submit)
    username_row.controls.append(username)
    password_row.controls.append(password)
    show_password_row.controls.append(tncs)
    dhaa_row.controls.append(dhaa)
    dhaa_row.controls.append(signup_text)
    forgot_password_row.controls.append(forgot_password_text)
    forgot_password_row.controls.append(reset_text)
    
    #Create a column to store the fields in rows
    login_view = Column(spacing=8)
    #Add fields and row to column
    login_view.controls.append(username_row)
    login_view.controls.append(password_row)
    login_view.controls.append(show_password_row)
    login_view.controls.append(dhaa_row)
    login_view.controls.append(forgot_password_row)
    login_view.controls.append(button_row)
    
    main_container = ft.Container(padding=20)
    main_container.content = login_view
    
    #Show password
    def show_password(e:ControlEvent) -> None:
        if tncs.value:
            password.password = False
        else:
            password.password = True
        page.update()
        
    def validate(e:ControlEvent) -> None:
        #Check if username and password is empty
        if all([username.value,password.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()
            
    username.on_change = validate
    password.on_change = validate
    tncs.on_change = show_password
    signup_text.on_click = lambda e: page.go("/")
    
    return ft.View("/login/",
                   controls=[main_container],vertical_alignment=ft.MainAxisAlignment.CENTER)

