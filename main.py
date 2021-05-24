from kivymd.app import MDApp                 # Importing all the necessary libraries
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window


kv = """
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: "Rate Finder"
    Screen:
        rate_me: rate_me
        rate_public: rate_public
        gst: gst
        pieces: pieces

        MDTextField:
            id: rate_me
            hint_text: 'Rate for You  '
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            size_hint_x: None
            width: 300
            required: True
            mode: "rectangle"
            input_filter: "int"
        
        MDTextField:
            id: rate_public
            hint_text: 'Rate for Public '
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300
            required: True
            mode: "rectangle"
            input_filter: "int"

        MDTextField:
            id: gst
            hint_text: 'Enter GST (in %) '
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300
            required: True
            mode: "rectangle"
            input_filter: "int"

        MDTextField:
            id: pieces
            hint_text: 'No. of Pieces  '
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300
            required: True
            mode: "rectangle"
            input_filter: "int"

        MDRaisedButton:
            text: 'Find'
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_press:
                app.margin()
"""

class MainApp(MDApp):
    icon = 'icon.png'
    def build(self):
        return Builder.load_string(kv)

    rate_me = ObjectProperty(None)
    rate_public = ObjectProperty(None)
    gst = ObjectProperty(None)
    pieces = ObjectProperty(None)

    def margin(self):
        p = int(self.root.ids.rate_public.text)
        m = int(self.root.ids.rate_me.text)
        g = int(self.root.ids.gst.text)
        margin = ((m * g) / 100) + m
        margin_percent = 100 - ((margin / p) * 100)
        single = margin / int(self.root.ids.pieces.text)
        self.dialog = MDDialog(title='Margin', text="Margin: {:.2f}%\nPrice of Single Piece: {:.2f}".format(margin_percent,single), size_hint=(0.8,1), buttons=[MDRaisedButton(text='Try another one', text_color=self.theme_cls.primary_color, on_release=self.close_dialog), MDFlatButton(text='Exit', text_color=self.theme_cls.primary_color, on_release=self.close_app)])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()  

    def close_app(self):
        App.get_running_app().stop()
        window.close()

MainApp().run()
