from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,ObjectProperty,BooleanProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
#import kivy
#print('----'*10,kivy.__version__)
#class PBoxLayout(Popup)
class G():
    app = App.get_running_app()

class Sta_man(BoxLayout):
    pass
class MasBox(BoxLayout):
    pass
class RV(RecycleView,G):
    mainclass=ObjectProperty(None)
    def __init__(self,**kwargs):
        super(RV, self).__init__(**kwargs)
        self.viewclass=self.mainclass
        self.data = [{'name':'!!!','lastdate':'2025-2-13','lasttext':'I hope you enjoy','index':str(x)} for x in range(100)]

class Person(BoxLayout,G):
    name=StringProperty('')
    lasttext=StringProperty('')
    lastdate=StringProperty('')
    index=StringProperty('')
    def on_touch_down(self,*args):
        self.parent.parent.parent.selected=int(self.index)

class Inbox(BoxLayout,G):
    pass

class Task(BoxLayout,G):
    name=StringProperty('')
    lasttext=StringProperty('')
    lastdate=StringProperty('')
    index=StringProperty('')
class SideBox(BoxLayout):
    def __init__(self,**kwargs):
        super(SideBox, self).__init__(**kwargs)
        self.size_hint=None,None
        self.size=500,700
        self.pos=100,100
        self.selected=0
        self.RE=RV(mainclass=Person)
        self.orientation='vertical'
        self.add_widget(self.RE)

class TasksL(SideBox,G):
    def __init__(self,**kwargs):
        super(TasksL, self).__init__(**kwargs)
        
        self.RE=RV(mainclass=Task)

class History(SideBox,G):
    def __init__(self,**kwargs):
        super(History, self).__init__(**kwargs)
        self.RE.data=[{'text':str(x)}for x in range(100)]
        self.RE.viewclass=Label

class Pbutton(Button,G):
    def on_release(self):
        self.parent.parent.inputed.text+=self.text

class Call_box(GridLayout,G):
    cols=2
    def __init__(self,name='+966567353177',**kwargs):
        super(Call_box,self).__init__(**kwargs)
        self.caller.text=str(name)

class Dashboard(BoxLayout,G):
    pass

class Phone(BoxLayout,G):
    def back(self):
        self.inputed.text=self.inputed.text[:-1]
    def call(self):
        self.parent.parent.parent.parent.parent.add_caller(caller=self.inputed.text)
        self.parent.remove_widget(self)

class Core_app(BoxLayout,G):
    def add_caller(self,caller='+966 567 353 177'):
        self.calls.add_widget(Call_box(name=caller))
    def open_phone(self):
        self.calls.add_widget(Phone())
    def open_sta(self):
        self.calls.add_widget(Sta_man())
    def open_mail(self):
        self.calls.add_widget(Inbox())
    def open_tasks(self):
        self.calls.add_widget(TasksL())
    def open_his(self):
        self.calls.add_widget(History())
    def open_dash(self):
        self.calls.add_widget(Dashboard())

class Call(App):
    def build(self):
        return Core_app()

Call().run()