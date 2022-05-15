import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MainWidget(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MyApp().run()
