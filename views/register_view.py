import flet as ft
from flet import ElevatedButton, TextField, Checkbox, Text, Row, Column, TextButton
from flet_core.control_event import ControlEvent
from flet_route import Params, Basket

def register(page:ft.Page,params:Params,basket:Basket):
    #Initialise page properties
    page.title = "register"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_resizable = True
    
    #Fields
    username = TextField(label="Username",text_align=ft.TextAlign.LEFT,border_radius=20,bgcolor="#f5f5f5")
    password = TextField(label="Password",text_align=ft.TextAlign.LEFT,border_radius=20,password=True,bgcolor="#f5f5f5")
    tncs = Checkbox(label="show password",value=False)
    button_submit = ElevatedButton(text="signup",disabled=True,bgcolor="#808080",color="#ffffff")
    ahaa = Text(value="Already have an account?",color="#808080")
    login_text = TextButton(text="login",style=ft.ButtonStyle(ft.colors.BLUE))
    
    #Create rows
    button_row = Row(spacing=10,alignment=ft.MainAxisAlignment.CENTER)
    username_row = Row(spacing=10,alignment=ft.MainAxisAlignment.CENTER)
    password_row = Row(spacing=5,alignment=ft.MainAxisAlignment.CENTER)
    show_password_row = Row(spacing=5,alignment=ft.MainAxisAlignment.CENTER)
    ahaa_row = Row(spacing=0,alignment=ft.MainAxisAlignment.CENTER)
    #Add button to row
    button_row.controls.append(button_submit)
    username_row.controls.append(username)
    password_row.controls.append(password)
    show_password_row.controls.append(tncs)
    ahaa_row.controls.append(ahaa)
    ahaa_row.controls.append(login_text)
    
    #Create a column to store the fields in rows
    reigster_view = Column(spacing=8)
    #Add fields and row to column
    reigster_view.controls.append(username_row)
    reigster_view.controls.append(password_row)
    reigster_view.controls.append(show_password_row)
    reigster_view.controls.append(ahaa_row)
    reigster_view.controls.append(button_row)
    
    
    #Create a container to store columns
    main_container = ft.Container(padding=20)
    #Add column to container
    main_container.content = reigster_view
    
   
    
    #Show password
    def show_password(e:ControlEvent) -> None:
        if tncs.value:
            password.password = False
        else:
            password.password = True
        page.update()
    
    #validate password
    def is_secure_password(password):
        # Minimum length requirement
        if len(password) < 8:
            return False
    
        # At least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
    
        # At least one lowercase letter
        if not any(char.islower() for char in password):
            return False
    
        # At least one digit
        if not any(char.isdigit() for char in password):
            return False
    
        # At least one special character
        special_characters = "!@#$%^&*()-_+=<>?/[]{},.:;"
        if not any(char in special_characters for char in password):
            return False
    
        # If all requirements are met, return True
        return True
    
    #validate fields
    def validate(e:ControlEvent) -> None:
        #Check if username and password is empty
        if all([username.value,is_secure_password(password.value)]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        #Check if username is less than 250 characters
        if len(username.value) > 20:
            username.error_text = "Username must be less than 250 characters"
        else:
            username.error_text = None
        page.update()
    
    #On field Change        
    username.on_change = validate
    password.on_change = validate
    tncs.on_change = show_password
    login_text.on_click = lambda e: page.go("/login/")
    
    return ft.View("/",
                   controls=[main_container],vertical_alignment=ft.MainAxisAlignment.CENTER)
       
