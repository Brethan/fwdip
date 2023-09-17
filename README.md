# fwdip
Uploads the IP Address of a Raspberry Pi operating in headless mode to a Firebase Real Time Database.

# Setup
You will need a Firebase Real Time Database which can be created for free.
Keep note of the name of your Firebase project name.

Set up the authentication for your database (this scripts assumes you've selected anonymouse authentication)
to generate the Web API key for project.

After you've collected both the project name and the API key, paste the API key in the corresponding field in the
[fwdip.py](/fwdip.py) source file and replace all occurances of `your-dev-server` with the Firebase project name.

```python
CONFIG = {
        "apiKey": "your-dev-server-api-key",
        "authDomain": "your-dev-server.firebaseapp.com",
        "databaseURL": "https://your-dev-server-default-rtdb.firebaseio.com/",
        "storageBucket": "your-dev-server.appspot.com"
}
```

Feel free to change the CHILD constant in the script to whatever you feel is best.
The child does not need to exist in the database before you run the script, it will be generated automatically.
```python
CHILD: str = "RTDB ID"
```

# Dependencies
This script needs to be ran using a version of Python that is $\ge$ 3.7

This script uses Pyrebase, a Firebase wrapper library for Python.  
To install it, run `pip3 install Pyrebase` in your terminal of choice
