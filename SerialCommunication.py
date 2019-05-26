import serial

class SerialCommunication:
	def __init__(self, port, baud):
		self._serial = serial.Serial(port, baud)

	def read_sample(self):
		line = self._serial.readline()
		if len(line) == 6:
			return line.decode()

if __name__ == "__main__":
	sc = SerialCommunication("COM8", 250000)
	while True:
		print(sc.read_sample())