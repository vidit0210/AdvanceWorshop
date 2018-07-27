class Car():


	def __init__(self, model, color, company, speed_limit):
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
		self.model = model

	def start(self):
		print("started")

	def stop(self):
		print("stopped")

	def accelarate(self):
		print("accelarating...")

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

print(audi.start())