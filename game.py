import electronicDie 
import csv
import os
import time
from time import sleep
debug=False
e=electronicDie.RollAndDisplay()
class Models:
	def __init__(self,):
		self.__player1_points=0	
		self.__player2_points=0	
		self.__max_points=30
	def get__player1_points(self):
		return self.__player1_points
	def get__player2_points(self):
		return self.__player2_points
	def get__max_points(self):
		return self.__max_points
	def set__max_points(self,num):
		self.__max_points=num
	def set__player1_points(self,num):
		self.__player1_points=num
	def set__player2_points(self,num):
		self.__player2_points=num
	player1_points=property(get__player1_points,set__player1_points)
	player2_points=property(get__player2_points,set__player2_points)
	max_points=property(get__max_points,set__max_points)
	def player1_game(self):
		e.set_accel()
		if (debug) :
			print("debug run1")
			
		e.print_random(e.get_accel())
		if (debug) :
			print("debug run2")			
		self.__player1_points=self.__player1_points+e.die_num
		if (debug) :
			print("debug run3")
		print("player1 points="+str(self.__player1_points))
		if(self.__player1_points>=30):
			return True
		else:
			return False
	def player2_game(self):
		e.set_accel()
		if (debug) :
			print("debug run1")
			
		e.print_random(e.get_accel())
		if (debug) :
			print("debug run2")			
		self.__player2_points=self.__player2_points+e.die_num
		if (debug) :
			print("debug run3")
		print("player2 points="+str(self.__player2_points))
		if(self.__player2_points>=30):
			return True
		else:
			return False
	def write_csv(self,player_name,time,player_points):
		with open("winner.csv",mode='a') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerow(["winner_name","time","points"])
			writer.writerow([player_name,time,player_points])
			csvfile.close();
	def read_csv(self):
		if(os.path.isfile("winner.csv")==True):
			with open("winner.csv",mode='r') as csvfile:
				reader=csv.reader(csvfile)
				for line in reader:
					print(line)
		else:
			print("file not exist")
		


class View:
	def greet(self):
		print("welcom to this game,The players willshake Pi several times one by one until one player gets above 30 points. The player who gets above 30 points first is the winner. Game start countdown:")
	#def view_update(self.strings):
		#print(strings)

class Controller:
	def countdown(self):
		count=0
		while (count < 5):
			count_now=5-count
			print(count_now)
			sleep(1)
			count += 1
		print('start')
	def start(self):
		view=View()
		view.greet()
		gameplay=Models()
		if (debug) :
			print("debug run3")
		while (gameplay.player1_points<gameplay.max_points and gameplay.player2_points<gameplay.max_points ):
			if(gameplay.player1_game()==True):
				gameplay.write_csv("player 1", str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),gameplay.player1_points)
				gameplay.read_csv()
				break
			else:
				print("player2 ready")
				self.countdown()
			if(gameplay.player2_game()==True):
				gameplay.write_csv("player 2", str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),gameplay.player2_points)
				gameplay.read_csv()
				break
			else:
				print("player1 ready")
				self.countdown()
			if (debug) :
				print("debug run4")
ui=View()
ui.greet()		
start=Controller()
start.countdown()
start.start()
		
