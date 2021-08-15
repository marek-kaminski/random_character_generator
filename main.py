from kivy.app import App
from kivy_deps import sdl2, glew
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
# from kivy.uxi.widget import Widget
from kivy.uix.scrollview import ScrollView
from STALKER_RPG import stalker_rpg
from STALKER_RPG import simple_printing
from STALKER_RPG import printer
from test_function import warhammer_fantasy_rpg


class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("This is a\nmultiline\nlabel")
    def on_button_click(self):
        from test1 import abc_list_cleared
        #need to add the "self." property before my_text, otherwise it will be a local variable
        # from test_function import warhammer_fantasy_rpg
        # print(warhammer_fantasy_rpg(1))

        abc = "szkoła"
        self.my_text = str(warhammer_fantasy_rpg(1))

    def on_button_clear(self):
        abc_list_cleared = 0
        #need to add the "self." property before my_text, otherwise it will be a local variable

        self.my_text = str(abc_list_cleared)



class ScrollViewExample(ScrollView):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
