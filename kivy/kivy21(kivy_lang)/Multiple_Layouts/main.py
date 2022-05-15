import kivy
from kivy.app import App

kivy.require('2.1.0')

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout


class MultipleLayout(PageLayout):
    pass


class MyApp(App):
    def build(self):
        return MultipleLayout()


if __name__ == '__main__':
    MyApp().run()
