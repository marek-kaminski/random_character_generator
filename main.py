from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
# from kivy.uxi.widget import Widget
from kivy.uix.scrollview import ScrollView
from STALKER_RPG import stalker_rpg
from STALKER_RPG import simple_printing


class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("a")
    def on_button_click(self):
        #need to add the "self." property before my_text, otherwise it will be a local variable

        # stalker_rpg()
        self.my_text = str(stalker_rpg())
        # simple_printing()

# class MainWidget(Widget):
#     pass




class ScrollViewExample(ScrollView):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
