output = open("outputformat","w")

coords = ""
flag = 0

with open("needformat.txt", "r") as textfile:
	for firstline in textfile:
		
		if (firstline.startswith("1.")):
			
			coords = "[{lat: " + firstline.replace("]\\n]\\n","}").replace("[[","{").replace("[","").replace("]","").replace("}}}","}").replace("{","{lat: ").replace(",10",",lng: 10").replace("}}","") + "];"
			coords = coords.replace("\n","")
			
		elif firstline and firstline[0].isalpha():
			if (flag == 0): 
				output.write("var " + firstline.lower().replace(" ","").replace("\u0027","").replace("-","").strip() + "PA = " + coords + "\n\n")
			else: 
				output.write("var " + firstline.lower().replace(" ","").replace("\u0027","").replace("-","").strip() + "SZ = " + coords + "\n\n")

			if (firstline.replace(" ","").strip() == "STRAITSVIEW"):
				flag = 1
			
			
output.close()
