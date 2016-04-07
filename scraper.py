import argparse
from bs4 import BeautifulSoup
import urllib2

BASE_URL = 'https://www.reddit.com/r/'


def main():
	parser = argparse.ArgumentParser(description = 'Download pictures from the specified subreddit')
	parser.add_argument('subreddit', help='Name of the subreddit to scrape from')
	parser.add_argument('-n', dest='numPics', type=int, nargs=1, default=10,
		                help='Number of pictures to download. Default is 10.')
	parser.add_argument('-s', dest='sortedBy', nargs=1, default='top',
		                choices=['top', 'new', 'hot', 'rising','controversial'],
		                help='Method to choose pictures by. Default is \'top\'.')
	parser.add_argument('-p', dest='period', nargs=1, default='day',
		                choices=['hour', 'day', 'week', 'month', 'year', 'all'],
		                help='Time period to choose pictures by. Default is \'day\'.')
	parser.add_argument('-fn', dest='folderName', nargs=1, default='',
		                help='Name of the folder to output to. Wrap multi-word names with '
		                'quotations. Default is \'[SubredditName] (Date)\'.')
	args = parser.parse_args()
	scrapeSubreddit(subredditName=args.subreddit, numPics=args.numPics, sortedBy=args.sortedBy,
		            period=args.period, folderName=args.folderName[0])

def scrapeSubreddit(subredditName, numPics, sortedBy, period, folderName):
	url = BASE_URL + subredditName + '/' + sortedBy + '/?sort=' + sortedBy + '&t=' + period
	print url
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	html = opener.open(url).read()
	soup = BeautifulSoup(html, "lxml")
	titles = soup.findAll("a", "title may-blank ")
	print titles[0].text

if __name__ == '__main__':
	main()