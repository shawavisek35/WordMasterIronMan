
#importing kivy methods

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require("1.11.1")
#my app will inherit from the main App class in kivy

class ConnectPage(GridLayout):#ConnectPage class is inheriting from Grid Layout class
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="IP : "))#for adding a textview
        self.ip = TextInput(multiline = False)#for adding edit text
        self.add_widget(self.ip)#taking input

        self.add_widget(Label(text="Port : "))
        self.port = TextInput(multiline = False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username : "))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.join = Button(text = "join")
        self.join.bind(on_press = self.join_button)#for binding a function to the button
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self,instance):
        #grabbing the values inserted by the user in the above method
        port = self.port.text
        ip = self.ip.text
        name = self.username.text

        print(f"Attempting to join : {ip} : {port} as {name}")

class EpicApp(App):
    def build(self):#initialization method
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()
