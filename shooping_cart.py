print(1)

class ShoppingCart:
	def __init__(self, max_size: int) -> None:
		self.items = []
		self.max_size = max_size

	def add(self, item: str):
		if self.size() == self.max_size:
			raise OverflowError

		self.items.append(item)

	def size(self) -> int:
		return len(self.items) 

	def get_items(self):
		return self.items

	def get_total_price(self, price_map):
		pass

