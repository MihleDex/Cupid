import flet as ft
from flet import ElevatedButton, TextField, Checkbox, Text, Row, Column
from flet_core.control_event import ControlEvent


def main(page:ft.Page) -> None:
    
    page.title = "register"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 360
    page.window_height = 800
    page.window_resizable = False
    
    
    
    #Fields
    username = TextField(label="Username",text_align=ft.TextAlign.LEFT,border_radius=20,bgcolor="#f5f5f5")
    password = TextField(label="Password",text_align=ft.TextAlign.LEFT,border_radius=20,password=True,bgcolor="#f5f5f5")
    tncs = Checkbox(label="I accept the terms and conditions",value=False)
    button_submit = ElevatedButton(text="Submit",disabled=True)
    
    
    #Create a column to store the fields in rows
    reigster_view = Column(spacing=10)
    #Add fiels to column
    reigster_view.controls.append(username)
    reigster_view.controls.append(password)
    reigster_view.controls.append(tncs)
    reigster_view.controls.append(button_submit)
    
    
    #Create a container to store columns
    main_container = ft.Container(padding=20)
    #Add column to container
    main_container.content = reigster_view
    
    #add views to page
    page.add(main_container)
    
    #adjust container according to window size
    def validate(e:ControlEvent) -> None:
        #Check if username and password is empty
        print(username.value, password.value, tncs.value)
        if all([username.value, password.value, tncs.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        #Check if username is less than 250 characters
        if len(username.value) > 20:
            username.error_text = "Username must be less than 250 characters"
        else:
            username.error_text = None
            
        
        page.update()
            
    username.on_change = validate
    password.on_change = validate
    tncs.on_change = validate
    page.update()
    

    
ft.app(target=main)