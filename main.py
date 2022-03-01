from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class MainWidget(Widget):
    pass


class AudioVidApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager


AudioVidApp().run()
