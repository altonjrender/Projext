
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label   import Label
from kivy.uix.floatlayout   import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.gridlayout import GridLayout
from todol import Todol
from kivy.uix.image import Image

class CreateApp(App):
	def build(self):
		b1 = Button
		mon = Todol("Monday")
		m = mon.createtodol()
		tues = Todol("Tuesday")
		t = tues.createtodol()
		return Image(source ='pic.png' )
		
	
if __name__== "__main__":
	CreateApp().run()
