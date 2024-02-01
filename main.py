import flet as ft
from flet_route import Routing,path
from views.register_view import register
from views.login_view import login

def main(page:ft.Page):
    #Initialise page properties
    
    app_routes = [
        path(url="/",clear=True, view=register),
        path(url="/login/",clear=True,view=login)
    ]
    
    Routing(page=page,app_routes=app_routes)
    
    page.go(page.route)
       
ft.app(target=main)