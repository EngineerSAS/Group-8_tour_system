
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '324')
Config.set('graphics', 'height', '540')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.navigationrail import MDNavigationRailMenuButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.widget import MDAdaptiveWidget
from kivy.uix.popup import Popup
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel


Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'

fonts = "assets/font/"

VISITOR_NOTE = '''
WELCOME TO AFIT TOUR SYSTEM
WE ARE GLAD TO HAVE YOU WITH US.
OUR TOUR TIMES ARE SCHEDULED AS FOLLOWS:
FRIDAY: 12:00HRS TO 16:00HRS
SATURDAY: 12:00HRS TO 16:00HRS
SUNDAT: 12:00HRS TO 18:00HRS

THANKS FOR COMPLYING'''

HELP_STR = '''
WE HOPE YOU ENJOYED YOUR EXPERIENCE.
FOR MORE INFORMATION CALL:
AFIT TOUR TEAM: 01-11211222
OR EMAIL US AT tours@afit.edu.ng

WE ANTICIPATE ANOTHER EXPERIENCE WITH YOU


SWENG GROUP-8 PROJECT'''

ERROR_MSG = '''
SORRY WE ARE STILL BUILDING THIS PAGE

WE WOULD BE DONE SOON

AFIT TOURS'''

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Manager(MDScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()
    
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        content_ = MDLabel(text="Welcome this pop up", adaptive_size=True, color=(1,1,1,1))
        self._popup = Popup(title="Load file", content=content_, size_hint=(0.9, 0.9))
        self._popup.open()
    
    def show_popup(self, btn):
        if btn == 'visiting':
            title = 'VISITING SCHEDULE'
            _content = VISITOR_NOTE
        elif btn == 'help':
            title = 'NEED HELP'
            _content = HELP_STR
        elif btn == 'error':
            title = 'UNDER CONSTRUCTION'
            _content = ERROR_MSG
        popup = Popup(title=title,
        content=MDLabel(text=str(_content), halign='center', valign='center'),
        size_hint=(0.9, 0.8))
        popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()
            self.dismiss_popup()

class TourApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.font_styles.update(
            {
                "H1": [f"{fonts}DINAlternate-bold", 96, False, -1.5],
                "H2": [f"{fonts}DINAlternate-bold", 60, False, -0.5],
                "H3": [f"{fonts}DINAlternate-bold", 48, False, 0],
                "H4": [f"{fonts}avenir_heavy", 34, False, 0.25],
                "H5": [f"{fonts}DINAlternate-bold", 24, False, 0],
                "H6": [f"{fonts}DINAlternate-bold", 20, False, 0.15],
                "Button": [f"{fonts}DINAlternate-bold", 14, True, 1.25],
                "Body1": [f"{fonts}DINAlternate-bold", 16, False, 0.5],
                "Body2": [f"{fonts}DINAlternate-bold", 14, False, 0.25],
            }
        )   

        

    def build(self):
        #Window.size = [324,600]
        #Builder.load_file("places.kv")
        return Builder.load_file("manager.kv")
    
    def dismiss_popup(self):
        self._popup.dismiss()
    
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()
            self.dismiss_popup()


if __name__ == "__main__":
    TourApp().run()
