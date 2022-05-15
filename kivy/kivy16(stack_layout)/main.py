import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

kivy.require('2.1.0')


class StacklayoutApp(App):
    def build(self):
        # lr-tb, tb-lr, rl-tb, tb-rl, lr-bt, bt-lr, rl-bt, bt-rl
        SL = StackLayout(orientation='tb-lr')
        btn1 = Button(text="B1",
                      font_size=20,
                      size_hint=(.2, .1))
        btn2 = Button(text="B2",
                      font_size=20,
                      size_hint=(.2, .1))
        btn3 = Button(text="B3",
                      font_size=20,
                      size_hint=(.2, .1))
        btn4 = Button(text="B4",
                      font_size=20,
                      size_hint=(.2, .1))
        btn5 = Button(text="B5",
                      font_size=20,
                      size_hint=(.2, .1))
        btn6 = Button(text="B6",
                      font_size=20,
                      size_hint=(.2, .1))
        btn7 = Button(text="B7",
                      font_size=20,
                      size_hint=(.2, .1))
        btn8 = Button(text="B8",
                      font_size=20,
                      size_hint=(.2, .1))
        btn9 = Button(text="B9",
                      font_size=20,
                      size_hint=(.2, .1))
        btn10 = Button(text="B10",
                       font_size=20,
                       size_hint=(.2, .1))

        SL.add_widget(btn1)
        SL.add_widget(btn2)
        SL.add_widget(btn3)
        SL.add_widget(btn4)
        SL.add_widget(btn5)
        SL.add_widget(btn6)
        SL.add_widget(btn7)
        SL.add_widget(btn8)
        SL.add_widget(btn9)
        SL.add_widget(btn10)

        return SL


if __name__ == "__main__":
    StacklayoutApp().run()
