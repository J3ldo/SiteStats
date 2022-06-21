# Site Stats
Site stats is a simple way to implement some insight about your site. Frameworks supported right now are: Flask. But django and react will hopefully soon come.  

## What it offers
* Amount of total requests made to the site.
* Amount of unique visitors.
* Amount of failed reqeusts.
* Amount of unique requests that failed.
* Amount of requests that got succesfully processed.
* Amount of unique requests that got succesfully processed.
* How much different urls got visited.
* How much different urls got visited by unique persons.
* Viewing the users trajectory.
* And way more to come!

## How to use
### Flask
If you want to use Site stats in flask. Just go to the flask directory and clone: SiteStats.py. Now just put the file in the same directory as the Flask app.  
Importing SiteStats.py:
```python
from flask import Flask
import SiteStats

app = Flask(__name__)

SiteStats.start(app) #To start listening.

try:
  app.run("0.0.0.0", 80)
finally:
  print(SiteStats.requests_made) #To access one of the variables.
  print(SiteStats.all) #To get a dictionary of all variables
```
