
#importing kivy methods

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require("1.11.1")
#my app will inherit from the main App class in kivy

class ConnectPage(GridLayout):#ConnectPage class is inheriting from Grid Layout class
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="IP : "))
        self.ip = TextInput(multiline = False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port : "))
        self.port = TextInput(multiline = False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username : "))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

class EpicApp(App):
    def build(self):#initialization method
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()
