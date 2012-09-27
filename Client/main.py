from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen


#class MainScreen(Screen):
#    pass

#class SettingsScreen(Screen):
#    pass

#class LoginScreen(Screen):
#	pass
	
# Create the screen manager

def switch(instance):
	sm.current = "login"


Login = Screen(name='login')
Main = Screen(name='main')
Settings = Screen(name='settings')

MainLayout = FloatLayout()

MainLayout.add_widget(TextInput(pos_hint={'x':.2,'top':1},size_hint=(0.8,0),size=(0,30),text='search',multiline=False))

classes = StackLayout(padding=3,size_hint=(.2,1),orientation="lr-tb")

for userClass in ['Sleep','Diet','Work','Commute']:
	myBtn = Button(pos_hint=(0,0),size_hint=(1,0),size=(125,55),text=userClass,name=userClass)
	myBtn.bind(on_release=switch)
	classes.add_widget(myBtn)
MainLayout.add_widget(classes)

Main.add_widget(MainLayout)


sm = ScreenManager(size_hint=(1,1))
sm.add_widget(Login)
sm.add_widget(Main)
sm.add_widget(Settings)

sm.current = 'main'

class LoggerApp(App):
    def build(self):
        return sm
        
LoggerApp().run()