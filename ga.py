import lxml.html
from utils import *
from docs import g

def ga_main_titles():
	html = lxml.html.parse(g)
	main_titles = []

	top_element = html.xpath('//div[@class="MainArticle Xlarge"]')

	assert len(top_element) == 1
	top_element = top_element[0]

	title = top_element.xpath('.//div[@class="h1"]/a/text()')
	assert len(title) == 1
	subtitle = top_element.xpath('.//div[@class="head head-top"]/a/text()')
	assert len(subtitle) == 1

	main_titles.append("-".join((title[0], subtitle[0])))

	titles = html.xpath('//div[@class="wrapper main"]/div[@class="LeftContent"]/ul[@class="intros"]/li')
	for el in titles:
		title = el.xpath('.//div[@class="h2"]/a/text()')
		if len(title) > 0:
			assert len(title) == 1
			main_titles.append(title[0])

	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def main():
	ga_main_titles()
	print "#####"

if __name__ == "__main__":
    main()