### OVAJ PROGRAM SE POKREĆE PRVI. IZ KORPUSA VADI IMENICE I SORTIRA IH PO FREKVENCI ###
recnik = dict()
with open("srWaC1.1.01.xml", "r", encoding="utf-8") as Korpus:
	for red in Korpus:
		if not red.startswith("<"):
			try:
				reci=red.split('\t')
				if (reci[3].startswith('N')) and (reci[1][0] == reci[2][0]):
					try:
						recnik[reci[2]] += 1
					except:
						recnik[reci[2]] = 1
			except:
				pass
sorted_by_value = sorted(recnik.items(), key=lambda kv: kv[1])
with open("sortedceo.txt", "w", encoding="utf-8") as Sortirano:
	for x in sorted_by_value:
		Sortirano.write(str(x) + "\n")
