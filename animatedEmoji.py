from sense_hat import SenseHat
from time import sleep


class Show_emoji():
	def __init__(self):
		self.s=SenseHat()
		self.blue=[0,0,255]
		self.red=[255,0,0]
		self.white=[255,255,255]
		self.green=[0,255,0]
		self.black=[0,0,0]
		self.yellow=[255,255,0]
		
	
	#def get_pixels(self):
	#	return pixels
	#def set_pixels(self,pixels):
	#	self.pixels=pixels
	#pixels=property(get_pixels,set_pixels)
	#def update_sensehat(self,pixels):
	#	self.s.set_pixels(pixels)
	def emoji1(self):
		c1=self.blue
		c2=self.red
		c3=self.green
		first_emoji=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c1,c1,c1,c1,c1,c1,
c2,c2,c2,c1,c1,c2,c2,c2,
c1,c2,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c3,c3,c3,c3,c1,c1,
c1,c1,c1,c3,c3,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		self.s.set_pixels(first_emoji)
	def emoji2(self):
		c1=self.yellow
		c2=self.blue
		c3=self.red
		second_emoji=[c1,c1,c1,c1,c1,c1,c1,c1,
c2,c1,c2,c1,c1,c2,c1,c2,
c1,c2,c1,c1,c1,c1,c2,c1,
c2,c1,c2,c1,c1,c2,c1,c2,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c3,c3,c3,c3,c3,c3,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		self.s.set_pixels(second_emoji)
	def emoji3(self):
		c1=self.red
		c2=self.white
		c3=self.yellow
		third_emoji=[c1,c1,c1,c1,c1,c1,c1,c1,
c2,c2,c2,c1,c1,c2,c2,c2,
c2,c1,c2,c1,c1,c2,c1,c2,
c2,c2,c2,c1,c1,c2,c2,c2,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c3,c3,c3,c3,c1,c1,
c1,c1,c3,c1,c1,c3,c1,c1,
c1,c1,c3,c3,c3,c3,c1,c1]
		self.s.set_pixels(third_emoji)
	
show=Show_emoji()
while True:
	show.emoji1()
	sleep(3)
	show.emoji2()
	
	sleep(3)
	show.emoji3()
	sleep(3)





