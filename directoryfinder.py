import requests

def request(url):
	try:
		return requests.get("https://" + url)
	except requests.exceptions.ConnectionError:
		pass

foundUrls=[]
def findDirectories(url):
	with open("wordlist.txt","r") as listFile:
		for line in listFile:
			word = line.strip()
			testUrl = url + "/" + word
			response = request(testUrl)
			if response:
				print("Found URL --> " + testUrl)
				foundUrls.append(word)

url="atilsamancioglu.com"
findDirectories(url)

#for foundUrl in foundUrls:
#	findDirectories(url+"/"+ foundUrl)
