import lxml.html
from docs import a

def ad():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@class="main-items"]/article/hgroup/descendant::a[@itemprop="url"]/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def ad_events():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="npt subcategory eveniment"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)		

def replace_new_lines(articles):
	titles = []
	for x in articles:
		titles.append(x.replace("\n", " "))
	return titles

def print_articles(articles):
	for x in articles:
		print x

def main():
	ad()
	print "#####"
	ad_events()	

if __name__ == "__main__":
    main()