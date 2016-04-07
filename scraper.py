import argparse

def main():
	parser = argparse.ArgumentParser(description = 'Download pictures from the specified subreddit')
	parser.add_argument('subreddit', help='Name of the subreddit to scrape from')
	parser.add_argument('-n', dest='numPics', type=int, nargs=1, default=10,
		                help='Number of pictures to download. Default is 10.')
	parser.add_argument('-s', dest='sortedBy', nargs=1, default='top',
		                help='Method to choose pictures by. Options are: top, new, hot, rising,'
		                'controversial, gilded. Default is \'top\'.')
	parser.add_argument('-p', dest='period', nargs=1, default='today',
		                help='Time period to choose pictures by. Options are: hour, today, week, '
		                'month, year, alltime. Default is \'today\'.')
	parser.add_argument('-fn', dest='folderName', nargs=1, default='',
		                help='Name of the folcer to output to. Wrap multi-word names with '
		                'quotations. Default is \'[SubredditName] (Date)\'.')
	args = parser.parse_args()
	

if __name__ == '__main__':
	main()