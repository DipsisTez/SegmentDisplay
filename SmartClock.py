#BasiClock example
from module.display import SegmentDisplay
from os import system
from time import sleep
from datetime import datetime

class SmartClock:
	def __init__(self):
		self.display1 = SegmentDisplay()
		self.display2 = SegmentDisplay()
		self.display3 = SegmentDisplay()
		self.display4 = SegmentDisplay()
		self.data0 = 0
		self.data1 = 0
		self._add = False


	def setData(self, screens, number):
		screen0, screen1 = screens
		screen0.setData(bin((number//10)%10)[2:])
		screen1.setData(bin(number%10)[2:])


	def setData0(self,number):
		self.setData([self.display1, self.display2], number)

	def setData1(self, number):
		self.setData([self.display3, self.display4], number)

	def setAdd(self,flag):
		self._add = flag

	def renderDisplay(self):
		self.display1.renderDoubleDisplay(self.display2.getMatrixDisplay())
		if self._add==1:
			print(' #	#	\n')
		else:
			print('  	 	\n')
		self.display3.renderDoubleDisplay(self.display4.getMatrixDisplay())



myClock = SmartClock()

prevMin = -1
prevSec = -1

for i in range(0, 10**4):
	currnet_time = datetime.now().time()
	
	if currnet_time.hour != prevMin:
		myClock.setData0(currnet_time.hour)
	if currnet_time.minute != prevSec:
		myClock.setData1(currnet_time.minute)
	
	myClock.setAdd(i%2==0)
	prevMin = currnet_time.hour
	prevSec = currnet_time.minute
	
	system('cls')
	myClock.renderDisplay()
	sleep(0.5)


