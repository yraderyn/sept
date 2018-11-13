### OVAJ PROGRAM SKIDA FREKVENCU I INTERPUNKCIJU KOJU JE PRETHODNI PROGRAM DODAO ###
import re
with open("sorted.txt", "r", encoding="utf-8") as Ulaz:
	with open("reizlaz2.txt", "w", encoding="utf-8") as Izlaz:
		for red in Ulaz:
			dobrarec = re.match("\('[a-zšđčćž]+', [0-9]+\)", red)
			if dobrarec:
				red = re.sub("\d",'', red)
				red = re.sub("\(",'', red)
				red = re.sub("\s",'', red)
				red = re.sub("\)",'', red)
				red = re.sub(",",'', red)
				red = re.sub("'",'', red)
				Izlaz.write(red + "\n")