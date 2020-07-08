import certifi
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest


KV = """
Screen:
    GridLayout:
        rows: 2
        ScrollView:
            MDLabel:
                id: mdlab
                text: "Benvenuti su Wikipedia Reader!"
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
        MDRaisedButton:
            id: mdbu
            text: "CERCA ARTICOLO CASUALE"
            size_hint_x: 1
            on_press: app.random_search_button()
"""


class WikiReaderApp(MDApp):

    def build(self):
        self.title = "WikipediaReader"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(KV)

    def random_search_button(self):
        endpoint = "https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json"
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())

    def get_data(self, request, response):
        random_article = response["query"]["random"][0]
        random_title = random_article["title"]
        endpoint = f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={random_title.replace(' ', '%20')}"
        self.data_request = UrlRequest(endpoint,
                                       on_success=self.set_textarea,
                                       ca_file=certifi.where())

    def set_textarea(self, request, response):
        page_info = response["query"]["pages"]
        page_id = next(iter(page_info))
        page_title = page_info[page_id]["title"]
        page_extract = page_info[page_id]["extract"]
        self.root.ids["mdlab"].text = f"{page_title}\n\n{page_extract}"



WikiReaderApp().run()