output = open("gmapvar.js","w")

with open("pacoords.js", "r") as textfile:
	for l in textfile:
		
		if (l.startswith("var")):
			
			jsvar = (l.split(" ")[1])
			
			output.write("var "+jsvar+"Polygon = new google.maps.Polygon({\npaths: "+jsvar+",\nstrokeColor: '#FF0000',\nstrokeOpacity: 0.8,\nstrokeWeight: 2,\nfillColor: '#FF0000',\nfillOpacity: aliveState});\n"+jsvar+"Polygon.setMap(map);")
			
output.close()