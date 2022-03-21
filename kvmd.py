from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList
from kivymd.uix.dropdownitem import MDDropDownItem
from functools import partial
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar,MDFloatingActionButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer
import random
Window.size=(360,600)
Builder.load_string("""
<scr>:
    orientation:"vertical"
    MDToolbar:
        title:"My Wallet"
        pos_hint: {"x":0,"y":0}
        left_action_items:[["menu", lambda *args: root.ids.nav_drawer.set_state("open")]]
        right_action_items:[["language-python", lambda *args: app.rightmenu()]]
        elevation:11
    MDTextField:
        id:txt
        hint_text:"Dialog Title"
        pos_hint: {"center_x":0.5,"center_y":0.5}
        size_hint_x: 0.7
        helper_text:"Don't leave Empty"
        # on_focus: helper_text
    MDFillRoundFlatButton:
        text:"Submit"
        pos_hint: {"center_x":0.5,"center_y":0.5}
        on_press: app.open_dialog()
    MDBottomAppBar:
        MDToolbar:
            title:"Airtel Money App"
            left_action_items:[["menu", lambda *args: nav_drawer.set_state("open")]]
            right_action_items:[["clock", lambda *args: app.rightmenu()]]
            mode: 'free-end'

        MDNavigationDrawer:
            id: nav_drawer
    # MDFloatingActionButton:
        
    #     icon: "language-python"
    #     on_press: print("take action now")
    # ScrollView:
    #     MDList:
    #         id:cont
""")
class scr(BoxLayout):
    pass
    # def __init__(self,**kwargs):
    #     super(scr,self).__init__(**kwargs)
    #     for i in range(0,100):
    #         with self.canvas.before:
    #             Color(random.uniform(0,.999),random.uniform(0,.999),random.uniform(0,.999),1)
    #             self.el=Ellipse()
    #             self.el.size=(random.randint(20,200),random.randint(20,200))
    #             self.el.pos=(random.randint(0,Window.width),random.randint(0,Window.height)) 
class myapp(MDApp):
    def leftmenu(self,*args):
        self.root.ids.nav_draw.set_state("open")
        # print("open up the left menu")
    def rightmenu(self,*args):
        print("open up the right menu")
    def clickont(self,*args):
        self.theme_cls.primary_palette=args[0].text
        # self.theme_cls.color =args[0].text
        self.dia.dismiss()
    def openlist(self,*args):
        pass
    def open_dialog(self,*args):
        color_scroll=ScrollView()
        color_list=MDList()
        for color in ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']:
            color_list.add_widget(OneLineListItem(text=color,on_press=self.clickont))
        color_scroll.add_widget(color_list)
        self.dia=MDDialog()
        self.dia.add_widget(color_scroll)
        self.dia.size_hint_x=.7
        self.dia.open()
    def build(self):
        self.title='kvmd using kv language'
        return scr()
if __name__ == "__main__":
    myapp().run()
