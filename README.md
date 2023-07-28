# Project 1: 

Your task is to build a RESTful API, using Python and Flask, that (partially) recreates some of
the GitHub API endpoints. The information provided by your API is to be scraped on-demand
from the GitHub website using Beautiful Soup.
The Flask API is to be created in a file named github_api.py and expose itself on the port
specified by the GITHUB_API_PORT environment variable. This environment variable should not
be set by your code. Your API will rely on web scraping functions that are to be defined in a file
named github_scraper.py. All python dependencies (as output by pip freeze) are to be
specified in requirements.txt. Projects which fail to adhere to these instructions will not be
marked. The following BASH script can be used to verify adherence.

The endpoints locations, query parameters, data types and response codes must match those of
the GitHub API, but only the endpoints and fields specified below need to be implemented. The
endpoints have been chosen such that you do not need to implement user authentication in your
API. You may wish to verify your solution by comparing your results with those consumed from
the GitHub API. The GitHub API and documentation will serve as ground truth for any
discrepancies or disputes. Your project may not use the GitHub Octokit library, GitHub CLI or
make requests to api.github.com.