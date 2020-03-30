import json
from sense_hat import SenseHat
import time
from time import sleep

debug=False
class Show_temp():
	def __init__(self):
	
		self.sense=SenseHat()
		self.blue=[0,0,255]
		self.red=[255,0,0]
		self.green=[0,255,0]
		self.white=[255,255,255]
		with open("config.json", 'r+') as f:
    			self.dic = json.loads(f.read())
    
    
		self.temp=self.sense.get_temperature()
		self.colour=self.white
	def run_project(self):
		while True:
			self.temp=round(self.temp,1)
			if(debug):
				print("debug"+str(dic['cold_max']))
			if (self.temp<self.dic['cold_max']):
				self.colour=self.blue		
			elif (self.temp>=self.dic['comfortable_min'] and self.temp<=self.dic['comfortable_max']):
				self.colour=self.green
			elif (self.temp>self.dic['hot_min']):
				self.colour=self.red
			if(debug):
				time_start=int(time.time())
	
			self.sense.show_message (str(self.temp),text_colour = self.colour,back_colour = self.white,scroll_speed=0.2)
			time_count=0
			if(debug):	
				time_end=int(time.time())
				time_count=time_end-time_start
			while(time_count<10):
				sleep(1)
				time_count=time_count+1
				print("time_count="+str(time_count)+"s")
			self.temp=self.sense.get_temperature()
			print("data update")
start=Show_temp()
start.run_project()
		
		
	
