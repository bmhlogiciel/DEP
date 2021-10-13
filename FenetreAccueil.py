# for showing of screen
from kivy import Config

Config.set('graphics', 'multisamples', '0')
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# ------- Begning of program

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from screen_code import screen_helper

Window.size = (700, 600)


class DemoApp(MDApp):
    dialog = None

    def BtnExit(self, args):
        print("Exit")

    def BtnNoExit(self, args):

        print("No Exit")

    @property
    def build(self):
        self.title = 'Hi its BMHcode'
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_def(self):

        print('navigation')

    def clock_def(self):

        print('clock')

    def coffee_def(self):
        print('coffee')

    def logout_def(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text = " Exit of this application ?",
                buttons=[
                    MDFlatButton(
                        text="Non", text_color=self.theme_cls.primary_color,
                        on_press = self.BtnNoExit
                    ),
                    MDFlatButton(
                        text="Yes", text_color=self.theme_cls.primary_color,
                        on_press = self.BtnExit
                    ),
                ],
            )
        self.dialog.open()


DemoApp().run()
