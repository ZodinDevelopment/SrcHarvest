# SrcHarvest
A simple yet functional and convenient tool that reads a .txt file containing urls and retrieves their source code and scrapes img objects from the html.

[Dependencies]
  + Python 3.7 
  + Python3-pip 
  
  
[Installation]

1. Clone the repository:
	
	$ git clone https://github.com/ZodinDevelopment/SrcHarvest.git

2. Install Python3.7 (if you don't have it) and Python3-pip:
	
	$ sudo apt update && sudo apt install python3 python3-pip 

3. Enter SrcHarvest directory and install the necessary dependencies:
	
	$ cd SrcHarvest
	
	$ python3 -m pip install -r requirements.txt

[Usage]
Note: As of right now, the tool is going to save it's output files in the directory you're executing the script from. Keep this in mind and make sure to move your documents into another directory if you are afraid of losing them due to samefilename errors. (I'll fix it shortly!)

$ python3 srcharvest.py

# The terminal will ask you to enter a path to a .txt file, it will attempt to read urls from it and perform its functions on them. 

# Your .txt file with your urls should simply be url strings, each seperated by a newline. 


[TODO]

	+ Implement directory system for output files and better filenaming convention
	+ Restructure the code in its entirety. It was a quick script I came up with and alot of the code can be compartmentalized into smaller functions. 
	+ Implement a support for command line arguments 


[Developer]
GitHub: https://github.com/ZodinDevelopment
Original Developer: Michael Landon / Zodin Development

Please report bugs, issues, comments, or questions to:
	
	michael.landon@zodin.dev



