import kivy
from kivy.app import App
from kivy.uix.label import Label

# 2
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

kivy.require('2.1.0')


class MyFirstApp(App):
    def build(self):
        # lbl = Label(text='Hello World')
        # lbl = Label(text='Hello World and Good Morning', font_size='20sp', color=[0.41, 0.42, 0.74, 1])
        lbl = Label(text="[color=ff3333][b]'Hello World'[/b][/color]\n[color=3333ff]Good Morning[/color]",
                    font_size='20sp', markup=True)
        """
        [b][/b] → 太字を有効にする
        [i][/i] → イタリック体のテキストをアクティブにする
        [u][/u] → 下線テキスト
        [s][/s] →取り消し線付きテキスト
        [font=][/font] → フォントを変更する
        [サイズ=][/size]]です。→ フォントサイズを変更する
        [色=#][/color] → 文字色の変更
        [ref=][/ref] -> インタラクティブゾーンを追加します。参照＋参照内部のバウンディングボックスがLabel.refsで利用可能になります。
        [anchor=] -> テキストにアンカーを入れる。テキスト内のアンカーの位置はLabel.anchorsで取得できます。
        [sub][/sub] -> 前のテキストからの相対的な添え字の位置でテキストを表示します。
        [sup][/sup] -> 前のテキストと相対的な上付き文字の位置でテキストを表示します。
        """

        return lbl


class Demo(MDApp):
    def build(self):
        screen = Screen()

        l = MDLabel(text="Welcome", pos_hint={'center_x': 0.8, 'center_y': 0.8},
                    theme_text_color='Custom',
                    text_color=(0.5, 0, 0.5, 1),
                    font_style='Caption'
                    )

        l1 = MDLabel(text="Welcome", pos_hint={'center_x': 0.8, 'center_y': 0.5},
                     theme_text_color='Custom',
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H2'
                     )

        l2 = MDLabel(text="Welcome", pos_hint={'center_x': 0.8, 'center_y': 0.2},
                     theme_text_color='Custom',
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H1'
                     )

        screen.add_widget(l)
        screen.add_widget(l1)
        screen.add_widget(l2)
        return screen


if __name__ == '__main__':
    # MyFirstApp().run()
    Demo().run()
