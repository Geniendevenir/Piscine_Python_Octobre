

import time
from random import randint
import os

first_time = True

def log(funct):
	def wrapper(*args, **kwargs):
		funct_name = funct.__name__.replace("_", " ").title()
		start_time = time.time()
		result = funct(*args, **kwargs)
		exec_time = time.time() - start_time
		
		LOG_FILE = "machine.log"
		global first_time
		mode = "w" if first_time else "a"
		first_time = False
		with open(LOG_FILE, mode) as out:
			if exec_time < 1:
				exec_time *= 1000
				out.write(f"({os.getlogin()})Running: {funct_name:<19}[ exec-time = {exec_time:.3f} ms ]\n")
			else:
				out.write(f"({os.getlogin()})Running: {funct_name:<19}[ exec-time = {exec_time:.3f} s ]\n")
		return result

	return wrapper

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
