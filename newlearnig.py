from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import logging
class one(Screen):
    def __init__(self,**kwargs):
        super(one,self).__init__(**kwargs)
        self.count=0
    def inc(self,*args):
        self.count+=1
        self.ids.show.text=str(self.count)
    def dec(self,*args):
        self.count-=1
        self.ids.show.text=str(self.count)
Builder.load_string('''
<one>:
	BoxLayout:
		orientation: "vertical"
        MDCard:
            size_hint: .4,.4
            elevation: 11
            spacing: 4
            pos_hint: {"center_x":.5,"center_y":.5}
            GridLayout:
                rows: 3
                cols: 1
                Button:
                    text: "+"
                    on_press: root.inc()
                CodeInput:
                    text: ""
                    id: show
                Button:
                    text: "-"
                    on_press: root.dec()
        #Widget:
            #size_hint_y:1.8
''')
class myapp(MDApp):
    def build(self,*args):
        return one()
if __name__=="__main__":
    myapp().run()