import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class Pagelayout(PageLayout):
    def __init__(self):
        super(Pagelayout, self).__init__()
        btn1 = Button(text='Page 1')
        btn1.background_color = get_color_from_hex('#FF0000')
        btn2 = Button(text='Page 2')
        btn2.background_color = get_color_from_hex('#00FF00')
        btn3 = Button(text='Page 3')
        btn3.background_color = get_color_from_hex('#0000FF')

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)


class Page_Layout(App):
    def build(self):
        return Pagelayout()


if __name__ == '__main__':
    Page_Layout().run()
