from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class MainWidget(Widget):
    pass


class AudioVidApp(App):
    pass


AudioVidApp().run()
