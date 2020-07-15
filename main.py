import certifi
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog


class WikiReaderApp(MDApp):

    info_dialog = None
    contact_dialog = None

    def build(self):
        self.title = "WikipediaReader"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        return Builder.load_file("wikireader.kv")

    def normal_search_button(self):
        query = self.root.ids["mdtext"].text
        self.get_data(title=query)

    def random_search_button(self):
        endpoint = "https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json"
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())

    def get_data(self, *args, title=None):
        if title == None:
            response = args[1]
            random_article = response["query"]["random"][0]
            title = random_article["title"]
        endpoint = f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={title.replace(' ', '%20')}"
        self.data_request = UrlRequest(endpoint,
                                       on_success=self.set_textarea,
                                       ca_file=certifi.where())

    def set_textarea(self, request, response):
        page_info = response["query"]["pages"]
        page_id = next(iter(page_info))
        page_title = page_info[page_id]["title"]
        try:
            content = page_info[page_id]["extract"]
        except KeyError:
            content = f"Ci spiace, ma la ricerca '{page_title}' non ha prodotto risultati!\n\nRiprova! "
        self.root.ids["mdlab"].text = f"{page_title}\n\n{content}"

    def show_app_info_dialog(self):
        app_info = "Wikipedia reader\n\nMade with <3"
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title = "Informazioni App",
                text = app_info,
                auto_dismiss = True
            )
        self.info_dialog.open()

    def show_contact_info_dialog(self):
        app_info = "Contatti:\n\nme@myself.com"
        if not self.contact_dialog:
            self.contact_dialog = MDDialog(
                title = "I Nostri Contatti",
                text = app_info,
                auto_dismiss = True
            )
        self.contact_dialog.open()



WikiReaderApp().run()