from kivy.app import App
from kivy_deps import sdl2, glew
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
# from kivy.uxi.widget import Widget
from kivy.uix.scrollview import ScrollView

from Warhammer_fantasy_RPG import warhammer_fantasy_rpg
from STALKER_RPG import stalker_rpg
from Star_Wars_RPG_homebrew import Star_Wars_rpg
from DnD_RPG import dnd_rpg


class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("This is a\nmultiline\nlabel")
    def on_button_click_STALKER(self):
        stalker_rpg(1)
        stalker_character = stalker_rpg(1)
        abc_list_cleared = [
            str(stalker_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))

        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abc_list_cleared)

    def on_button_click_Star_Wars(self):
        Star_Wars_rpg(1)
        starwars_character = Star_Wars_rpg(1)
        abc_list_cleared = [
            str(starwars_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))

        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abc_list_cleared)

    def on_button_click_Warhammer_fantasy(self):
        warhammer_fantasy_rpg(1)
        starwars_character = warhammer_fantasy_rpg(1)
        abc_list_cleared = [
            str(starwars_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))

        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abc_list_cleared)

    def on_button_click_DnD(self):
        dnd_rpg(1)
        dnd_character = dnd_rpg(1)
        abc_list_cleared = [
            str(dnd_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))

        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = str(abc_list_cleared)


    def on_button_clear(self):
        abc_list_cleared = 0
        #need to add the "self." property before my_text, otherwise it will be a local variable
        self.my_text = ""



class ScrollViewExample(ScrollView):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
