from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
Screen:

    GridLayout:
        rows: 2

        ScrollView:
            MDLabel:
                id: mdlab
                text: "Benvenuti su Wikipedia Reader!"
                # font_style: "H1"
                # padding_x: 30
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None

        MDRaisedButton:
            id: mdbu
            text: "PREMI QUESTO TASTO!"
            size_hint_x: 1 # 0.0 - 1.0
            on_press: app.random_search_button()
"""


class WikiReaderApp(MDApp):

    def build(self):
        self.title = "WikipediaReader"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(KV)

    def random_search_button(self):
        self.root.ids["mdlab"].text = "Tasto ricerca casuale premuto!"


WikiReaderApp().run()