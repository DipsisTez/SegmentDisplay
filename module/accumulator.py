#test class

class Accumulator:
	def __init__(self, powerEnergy, V, I, serial_key):
		self.powerEnergy = powerEnergy
		self.V = V
		self.I = I
		self.key = serial_key

	def getEnergy(self):
		if self.powerEnergy > 0:
			self.powerEnergy -= self.V*self.I
			return 1
		return 0

	def getInfoEnergy(self):
		return self.powerEnergy

	def getV(self):
		return self.V

	def getI(self):
		return self.I

	def getKey(self):
		return self.serial_key
