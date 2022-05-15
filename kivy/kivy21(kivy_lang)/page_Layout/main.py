import kivy
from kivy.app import App

kivy.require("2.1.0")
from kivy.uix.pagelayout import PageLayout


class pagelayout(PageLayout):
    pass


class MyApp(App):
    def build(self):
        return PageLayout()


if __name__ == '__main__':
    MyApp().run()
