import kivy
from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder

kivy.require('2.1.0')

Builder.load_string('''
<ScrollableLabel>:
    text: 'You are learning kivy'
    Label:
        text: root.text
        font_size: 50
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


if __name__ == '__main__':
    runTouchApp(ScrollableLabel())
