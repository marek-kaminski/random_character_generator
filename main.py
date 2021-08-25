from kivy.app import App
from kivy_deps import sdl2, glew
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uxi.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from Warhammer_fantasy_RPG import warhammer_fantasy_rpg
from STALKER_RPG import stalker_rpg
from Star_Wars_RPG_homebrew import Star_Wars_rpg
from DnD_RPG import dnd_rpg

class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("This is a\nmultiline\nlabel")
    character_amount = 1
    character_amount_display = StringProperty("1")

    # need to add the "self." property before my_text, otherwise it will be a local variable
    def on_button_add(self):

        self.character_amount += 1
        character_amount = 1
        character_amount += 1
        self.character_amount_display = str(self.character_amount)
        return character_amount

    def on_button_remove(self):
        if self.character_amount >1:
            self.character_amount -= 1
            self.character_amount_display = str(self.character_amount)
        else:
            pass
    def on_button_click_STALKER(self):
        stalker_rpg(self.character_amount)
        stalker_character = stalker_rpg(self.character_amount)

        abc_list_cleared = [
            str(stalker_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))
        self.my_text = str(abc_list_cleared)

    def on_button_click_Star_Wars(self):
        Star_Wars_rpg(self.character_amount)
        starwars_character = Star_Wars_rpg(self.character_amount)
        abc_list_cleared = [
            str(starwars_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))
        self.my_text = str(abc_list_cleared)

    def on_button_click_Warhammer_fantasy(self):
        warhammer_fantasy_rpg(self.character_amount)
        starwars_character = warhammer_fantasy_rpg(self.character_amount)
        abc_list_cleared = [
            str(starwars_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))
        self.my_text = str(abc_list_cleared)

    def on_button_click_DnD(self):
        dnd_rpg(self.character_amount)
        dnd_character = dnd_rpg(self.character_amount)
        abc_list_cleared = [
            str(dnd_character).replace('[', "").replace(',', "").replace("'", "").replace(']', "").replace('"', "").replace('\\n', "\n")]
        abc_list_cleared = (' '.join(abc_list_cleared))
        self.my_text = str(abc_list_cleared)




class ScrollViewExample(ScrollView):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
