import argparse

def main():
	parser = argparse.ArgumentParser(description = 'Download pictures from the specified subreddit')
	parser.add_argument('subreddit', help='Name of the subreddit to scrape from')
	parser.add_argument('-n', dest='numPics', type=int, nargs=1, default=10,
		                help='Number of pictures to download. Default is 10.')
	parser.add_argument('-s', dest='sortedBy', nargs=1, default='top',
		                choices=['top', 'new', 'hot', 'rising','controversial', 'gilded'],
		                help='Method to choose pictures by. Default is \'top\'.')
	parser.add_argument('-p', dest='period', nargs=1, default='today',
		                choices=['hour', 'today', 'week', 'month', 'year', 'alltime'],
		                help='Time period to choose pictures by. Default is \'today\'.')
	parser.add_argument('-fn', dest='folderName', nargs=1, default='',
		                help='Name of the folder to output to. Wrap multi-word names with '
		                'quotations. Default is \'[SubredditName] (Date)\'.')
	args = parser.parse_args()
	scrapeSubreddit(subredditName=args.subreddit, sortedBy=args.sortedBy[0],
		            period=args.period[0], folderName=args.folderName[0])

def scrapeSubreddit(subredditName, sortedBy, period, folderName):
	print subredditName
	

if __name__ == '__main__':
	main()