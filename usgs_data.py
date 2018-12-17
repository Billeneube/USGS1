import urllib.request
import json

def printResults(data):
	
	theJSON = json.loads(data)
	if "title" in theJSON["metadata"]:
		print (theJSON["metadata"]["title"])
	count = theJSON["metadata"]["count"];
	print(str(count) + " Events Recorded")
	print("-------\n")
	for i in theJSON["features"]:
		if i["properties"]["mag"] >3.5:
			print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
	print("-------\n")
	
	
def main():
	urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	webUrl = urllib.request.urlopen(urlData)
	print("result code :" + str(webUrl.getcode()))
	if(webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)
	else:
		print("received an error from server" + srt(webUrl.getcode()))

if __name__ == "__main__":
	main()
