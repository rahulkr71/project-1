from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window

Window.size = (360,640)

Builder.load_file('main.kv')

class WelcomeScreen(Screen):
    pass

class UsernameScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Prac5App(MDApp):
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightBlue'
        return WindowManager()

Prac5App().run()