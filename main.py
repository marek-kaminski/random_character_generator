from kivy.app import App
from kivy_deps import sdl2, glew
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
# from kivy.uxi.widget import Widget
from kivy.uix.scrollview import ScrollView
from STALKER_RPG import stalker_rpg
from test_function import warhammer_fantasy_rpg
from test_function import abc_list_cleared

def abcd():
    abbbb = "aaaa\nbb"
    return abbbb




class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("This is a\nmultiline\nlabel")
    def on_button_click(self):
        warhammer_fantasy_rpg(1)
        starwars_character = warhammer_fantasy_rpg(1)
        abc_list_cleared = [
            str(starwars_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"',
                                                                                                                "").replace('\\n', "\n").replace('żółtodziub', "*")]
        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abc_list_cleared)

    def on_button_clear(self):
        abc_list_cleared = 0
        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abcd())



class ScrollViewExample(ScrollView):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
