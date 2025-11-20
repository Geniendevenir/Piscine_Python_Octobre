from pathlib import Path

""" 
with open(fileName) as f:

-> Try to open fileName

"""

class CsvReader:
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if not isinstance(filename, str):
			raise TypeError("Filename should be a string")
		elif not isinstance(sep, str) or len(sep) != 1:
			raise TypeError("Sep should be a character")
		elif not isinstance(header, bool):
			raise TypeError("Header should be a boolean")
		if not isinstance(skip_top, int):
			raise TypeError("Skip_top should be an int")
		if not isinstance(skip_bottom, int):
			raise TypeError("Skip_bottom should be a int")

		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		try:
			self.file = open(self.filename, "r")
			self.cleanLine = []
			for line in self.file:
				if line.strip() == "":
					continue
				self.cleanLine.append(line.rstrip("\n"))

			reccords = 0	
			for i, line in enumerate(self.cleanLine):
				splittedLine = line.split(self.sep)
				if i == 0:
					reccords = len(splittedLine)
				elif len(splittedLine) != reccords:
					raise ValueError("Inconsistent Reccords Lenght")

		except FileNotFoundError:
			raise FileNotFoundError("File does not Exists")
		except PermissionError:
			raise PermissionError("No Permission")
		return self	

	def __exit__(self, exc_type, exc_value, traceback):
		if hasattr(self, "file"):
			self.file.close()

	def getdata(self):
		"""
		Retrieves the data/records from skip_top to skip_bottom.

		Returns:
		    nested list (list(list, list, ...)) representing the data.
		"""
		if not hasattr(self, "cleanLine"):
			return None

		lines = self.cleanLine
		if self.header:
			lines = lines[1:]
		lines = lines[self.skip_top : len(lines) - self.skip_bottom]
		return [line.split(self.sep) for line in lines]

	def getheader(self):
		"""
		Retrieves the header from the csv file.

		Returns:
		    list: representing the header (when self.header is True).
		    None: when self.header is False.
		"""
		if self.header is True and self.cleanLine:
			return self.cleanLine[0].split(self.sep)
		return None
