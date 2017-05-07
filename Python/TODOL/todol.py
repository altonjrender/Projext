##This is the class for the button
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label   import Label
from kivy.uix.floatlayout   import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
##Each Layout has a reminder(e.g. hourly,daily, weekly)
## Needs to save the layout onclose, onexit, orientation, 
##class Layout(GridLayout):
	##ef __init__(self)
	
##Application should not interrupt other applications, just add icon to the taskbar/todol
##Each todol(to do list) has a layout.. the button will check the times and place a reminder on the screen
class Todol:
	def __init__(self, day_of_week):
		self.weekday = day_of_week
	def getday():
		return self.weekday
	def createtodol(name):
		b = Button(text = name.weekday,background_color = (0,0,1,1), font_size = 150)
		return b
