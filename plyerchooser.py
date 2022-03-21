from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Canvas,Color,Ellipse,Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
# from kivy.core.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from plyer import sms,notification,filechooser
import random, sys
#permission
#path*2
#send uncomment
#version
class home(BoxLayout):
    def __init__(self,**kwargs):
        super(home,self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding=40
        self.add_widget(Button(text='Select Folder',on_press=self.select_folder))
        self.add_widget(Button(text='Open',on_press=self.select_file))
        self.add_widget(Button(text='Save',on_press=self.file_saver))
        self.name=Label(text='')
        self.add_widget(self.name)
        
    def select_folder(self,*args):
        choose=filechooser.choose_dir(multiple=False,title='Select Folder',preview=False,icon=None,show_hidden=False,on_selection=self.selected)
    def select_file(self,*args):
        choose=filechooser.open_file(multiple=False,title='Open File Dialog',preview=False,icon=None,show_hidden=False,on_selection=self.selected)
    def file_saver(self,*args):
        choose=filechooser.save_file(multiple=False,title='Save File Dialog',preview=False,icon=None,show_hidden=False,on_selection=self.selected)
    def selected(self,args):
        try:
            self.name.text=args[0]
        except:
            pass
class myapp(App):
    def build(self):
        self.title="plyer chooser"
        return home()
if __name__ == "__main__":
    myapp().run()
