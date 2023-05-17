"""Send greetings."""

import arrow
import sys
import requests



def runner(website: str):
    """Download website and return the content."""

    # Download website content
    response = requests.get(website)
    if response.status_code != 200:
        return "Error downloading website"
    
    # Save the website to a file
    with open("website.txt", "w") as f:
        f.write(response.text)

    return "Success"

# This is the main function that is called from the command line and parse arguments
def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]    
    tz = args[0]
    print(runner(tz))