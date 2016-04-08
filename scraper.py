import argparse
from bs4 import BeautifulSoup
from datetime import date, time, datetime
import urllib2
import urllib
import os

BASE_URL = 'https://www.reddit.com/r/'
BASE_OUTPUT_DIRECTORY = 'downloads/'


def main():
	parser = argparse.ArgumentParser(description = 'Download pictures from the specified subreddit')
	parser.add_argument('subreddit', help='Name of the subreddit to scrape from')
	parser.add_argument('-n', dest='numPics', type=int, default=10,
		                help='Number of pictures to download. Default is 10.')
	parser.add_argument('-s', dest='sortedBy', default='top',
		                choices=['top', 'new', 'hot', 'rising','controversial'],
		                help='Method to choose pictures by. Default is \'top\'.')
	parser.add_argument('-p', dest='period', default='day',
		                choices=['hour', 'day', 'week', 'month', 'year', 'all'],
		                help='Time period to choose pictures by. Default is \'day\'.')
	parser.add_argument('-fn', dest='folderName', default='',
		                help='Name of the folder to output to. Wrap multi-word names with '
		                'quotations. Default is \'[SubredditName] (Date)\'.')
	args = parser.parse_args()
	scrapeSubreddit(subredditName=args.subreddit, numPics=args.numPics, sortedBy=args.sortedBy,
		            period=args.period, folderName=args.folderName)


def scrapeSubreddit(subredditName, numPics, sortedBy, period, folderName):
	url = BASE_URL + subredditName + '/' + sortedBy + '/?sort=' + sortedBy + '&t=' + period
	if folderName == '':
		dt = datetime.now()
		folderName = subredditName + " (" + dt.strftime("%Y-%m-%d %I.%M%p") + ")"
	directory = BASE_OUTPUT_DIRECTORY + folderName + "/" 
	os.makedirs(directory)

	picItems = []
	print "\nScraping from: " + url + "\n"
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/6.0')]
	html = opener.open(url).read()
	soup = BeautifulSoup(html, "lxml")
	picItems += soup.findAll("a", "title may-blank ")

	for i in range(min(numPics, len(picItems))):
		picUrl = picItems[i]['href']
		if picUrl[-5:] == '.gifv':
			picUrl = picUrl[:-1]
		elif picUrl[-4] != '.':
			picUrl += '.jpg'
		print "Downloading: " + picUrl
		title = picItems[i].text
		title += picUrl[-4:]
		urllib.urlretrieve(picUrl, directory + title)

if __name__ == '__main__':
	main()