def replace_new_lines(articles):
	titles = []
	for x in articles:
		titles.append(x.replace("\n", " "))
	return titles

def print_articles(articles):
	for x in articles:
		print x