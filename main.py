# for showing of screen
import kivy
kivy.Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen,NoTransition,CardTransition

# Window.size = (300,500)

class Accueil(Screen):
    pass

class Profile(Screen):
    pass

class Personnel(Screen):
    pass

class Parametre(Screen):
    pass


class MainApp(MDApp):

    def __init__(self,**kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Green"
        super().__init__(**kwargs)

    @property
    def build(self):
        return Builder.load_file("main.kv")

    def change_fenetre(self,nom_fenetre,direction='avant',mode="",duration="0.5"):
        screen_manager = self.root.ids["screen_manager"]
        if direction == "avant":
            mode = "push"
            direction = 'left'

        elif direction == "arriere":
            mode='pop'
            direction = "right"

        elif direction == "None":
            screen_manager.transition = NoTransition
            screen_manager.current = nom_fenetre

        screen_manager.transition = CardTransition(direction=direction, mode=mode,duration=duration)
        screen_manager.current = nom_fenetre





MainApp().run()
