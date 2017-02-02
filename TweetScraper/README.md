# Twitter Scrape

Scrape tweets from twitter into a stopover DB.  Convert the DB to a CSV or JSON file.

## Setup
Try this to install the necessary libraries, let me know if something goes wrong. You make have to install pip first. 
https://pip.pypa.io/en/stable/installing/

* `pip install -r requirements.txt`

## Usage

* `python scrapesuperselect.py` to scrape.  Use `Ctrl + C` to stop. CSV and JSON files will be created upon exiting.
* to change the primary filter (list of shows and movies), go to settings.py.
* to change the secondary filters, find the if statement in scrapersuperselect.py.
