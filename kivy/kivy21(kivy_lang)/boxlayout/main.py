import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MainWidget(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MyApp().run()
