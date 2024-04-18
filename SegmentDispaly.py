#BasiClock example
from module.display import SegmentDisplay
from os import system
from time import sleep

Display1 = SegmentDisplay()
Display2 = SegmentDisplay()

Display3 = SegmentDisplay()
Display4 = SegmentDisplay()

for i in range(0, 10**4):
	i2,i1 = bin(i%10)[2:], bin((i//10)%10)[2:]
	i4,i3 = bin((i//100)%10)[2:], bin((i//1000)%10)[2:]
	Display1.setData(i1)
	Display2.setData(i2)
	Display3.setData(i3)
	Display4.setData(i4)

	system('cls')
	Display3.renderDoubleDisplay(Display4.getMatrixDisplay())
	if i%2==0:
		print(' #	#	\n')
	else:
		print('  	 	\n')
	Display1.renderDoubleDisplay(Display2.getMatrixDisplay())
	sleep(1)

