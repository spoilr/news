import lxml.html
from utils import *
from docs import a

def ad_main_titles():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@class="main-items"]/article/hgroup/descendant::a[@itemprop="url"]/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def ad_events():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="npt subcategory eveniment"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def ad_eu():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="international subcategory europa"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)	

def ad_politics():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="politica subcategory politica"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)	

def ad_economy():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="economie subcategory stiri-economice"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)	

def ad_school():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="educatie subcategory scoala"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def ad_society():
	html = lxml.html.parse(a)
	main_titles = html.xpath('//div[@id="main-content"]/div[@class="wrap clearfix"]/div[@class="column-large mixed-news"]/article[@class="societate subcategory societate"]/h3[@class="defaultTitle"]/a/text()')
	
	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)	

def main():
	print "##### main"
	ad_main_titles()
	print "##### events"
	ad_events()
	print "##### eu"
	ad_eu()
	print "##### politics"
	ad_politics()
	print "##### economy"
	ad_economy()
	print "##### school"
	ad_school()
	print "##### society"
	ad_society()

if __name__ == "__main__":
    main()