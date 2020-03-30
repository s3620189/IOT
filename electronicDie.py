from sense_hat import SenseHat
import random
sense=SenseHat()
class Die_matter:
	def __init__(self):		
		
		self.red=[255,0,0]
		self.white=[255,255,255]
		
		
	def die_1(self):
		c1=self.white
		c2=self.red
		
		die_1=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		return die_1
	def die_2(self):
		c1=self.white
		c2=self.red
		
		die_2=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		return die_2
	def die_3(self):
		c1=self.white
		c2=self.red
		
		die_3=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		return die_3
	def die_4(self):
		c1=self.white
		c2=self.red
		
		die_4=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		return die_4
	def die_5(self):
		c1=self.white
		c2=self.red
		
		die_5=[c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c1,c1,c2,c2,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1]
		return die_5
	def die_6(self):
		c1=self.white
		c2=self.red
		
		die_6=[c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c1,c1,c1,c1,c1,c1,c1,
c1,c2,c2,c1,c1,c2,c2,c1,
c1,c2,c2,c1,c1,c2,c2,c1]
		return die_6
		

class RollAndDisplay:
	
	def __init__(self):
		self.__die_num=0
		
	def set_accel(self):
		sense.set_imu_config(False,False,True)
	def get_accel(self):
		accel=sense.get_accelerometer_raw()
		
		return accel
	
	def get_random_num(self):
		return self.__die_num
	def set_random_num(self,num):
		self.__die_num=num
	die_num=property(get_random_num,set_random_num)
	def print_random(self,accel):
		matter=Die_matter()
		die_all=[matter.die_1(),matter.die_2(),matter.die_3(),matter.die_4(),matter.die_5(),matter.die_6()]
		while (True):
			if(abs(accel['x'])>=1.5 or abs(accel['y'])>=1.5 or abs(accel['z'])>=1.5):
				self.__die_num=random.randint(1,6)
				print("die result="+str(self.__die_num))
				sense.set_pixels(die_all[(self.__die_num-1)])
				break
			else:
				print("please shake the pi")
				while(True):
					accel=self.get_accel()
					if(abs(accel['x'])>=1.5 or abs(accel['y'])>=1.5 or abs(accel['z'])>=1.5):
						break
				
