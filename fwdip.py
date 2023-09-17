from pyrebase.pyrebase import Database
from pyrebase import initialize_app as initApp
import urllib.request as ur
from subprocess import check_output
from time import sleep

# Fill out the config with the information from your Firebase Real time database
CONFIG = {
        "apiKey": "your-dev-server-api-key",
        "authDomain": "your-dev-server.firebaseapp.com",
        "databaseURL": "https://your-dev-server-default-rtdb.firebaseio.com/",
        "storageBucket": "your-dev-server.appspot.com"
}

# Set the CHILD to whatever you want to name the ip address entry
CHILD: str = "RTDB-ID"

def check_internet_connection(host="http://google.com") -> bool:
	'''
	Checks for an internet connection by pinging Google.
	Returns true if a connection can be established,
	false otherwise
	'''
	try:
		print(f"Pinging {host}:")
		ur.urlopen(host)
		return True
	except:
		return False

def main():

	tries = 60
	while not check_internet_connection() and tries >= 0:
		tries -= 1
		sleep(3)

	if tries < 0:
		print("Could not connect to the internet :(")
		return

	print("Connected to the internet, updated the RTDB")
	
	# This command may not work as expected on some distros of Linux
	# It will also not work at all for MacOS
	ip_address = check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
	
	firebase = initApp(CONFIG)
	db: Database = firebase.database()
	db.child(CHILD).set(ip_address)


if __name__ == "__main__":
	main()
