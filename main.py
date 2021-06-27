
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from STALKER_RPG import stalker_rpg
import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput




class MyGrid(GridLayout):
    """coment"""





class WarhammerApp (App):
    def build(self):
        mylayout = GridLayout(cols=3, rows=3, padding = 50,  row_default_height=40)
        mylabel = Label(text= "My App", pos_hint={'center_x': 0.5 })
        printed_text = Label(text="hi")
        Button1 = Button(text="DmD 5e",   size_hint_x=None, width=150, height=100)
        Button2 = Button(text="Warhammer 4ed",  size_hint_x=None, width=150, height=100)
        Button3 = Button(text="S.T.A.L.K.E.R RPG", size_hint_x=None, width=150, height=100)
        asa = 'Hello world'
        textinput = TextInput(text=asa)

        def change_text():
            print(12)

        Button1.bind(on_press= lambda a: print(mylabel.text))
        Button2.bind(on_press= lambda a: change_text())
        Button3.bind(on_press= lambda a: stalker_rpg())
        mylayout.add_widget(Button1)
        mylayout.add_widget(Button2)
        mylayout.add_widget(Button3)
        mylayout.add_widget(printed_text)
        mylayout.add_widget(textinput)
        return mylayout


if __name__ == "__main__":
    WarhammerApp().run()
