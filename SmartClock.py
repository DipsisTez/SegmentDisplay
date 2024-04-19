#BasiClock example
from module.display import SegmentDisplay
from module.accumulator import Accumulator
from os import system
from time import sleep
from datetime import datetime


class SmartClock:
	def __init__(self):
		self.accumulator = Accumulator(6 * 10**5, 5,1, '100AKA_SMARTH')
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
		if self.accumulator.getEnergy() == 0 or self.accumulator.getV()<5 or self.accumulator.getV()>8:
			return None
		self.display1.renderDoubleDisplay(self.display2.getMatrixDisplay())
		if self._add==1:
			print(' #	#	\n')
		else:
			print('  	 	\n')
		self.display3.renderDoubleDisplay(self.display4.getMatrixDisplay())
		return 1



myClock = SmartClock()

prevHour = -1
prevMin = -1
power = 1

while power:
	currnet_time = datetime.now().time()
	
	if currnet_time.minute != prevHour:
		myClock.setData0(currnet_time.hour)
	if currnet_time.second != prevMin:
		myClock.setData1(currnet_time.minute)
	
	myClock.setAdd(myClock.accumulator.getInfoEnergy()%2==0)
	prevHour = currnet_time.hour
	prevMin = currnet_time.minute
	
	system('cls')
	power = myClock.renderDisplay()
	sleep(0.5)


