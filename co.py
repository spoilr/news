import lxml.html
from utils import *
from docs import c

def co_main_titles():
	html = lxml.html.parse(c)
	main_titles = []

	top_element = html.xpath('//div[@class="middle"]/div[@class="articleblock"]/div[@class="articletextbig"]')

	assert len(top_element) == 1
	top_element = top_element[0]

	titles = top_element.xpath('.//div[@class="subtitle"]/text()')
	subtitles = top_element.xpath('.//div[@class="title"]/a/text()')

	assert len(titles) == len(subtitles)

	for i in range(len(titles)):
		main_titles.append("-".join((titles[i], subtitles[i])))

	# ----------

	main_elements = html.xpath('//div[@class="middle"]/div[@class="articleblock"]/div[contains(@class, "articlehalfblock")]/div[@class="articletextbig"]')
	
	for el in main_elements:
		title = el.xpath('.//div[@class="subtitle"]/text()')
		subtitle = el.xpath('.//div[@class="title"]/a/text()')

		assert len(titles) == len(subtitles) == 1
		main_titles.append("-".join((title[0], subtitle[0])))

	main_titles = replace_new_lines(main_titles)
	print_articles(main_titles)

def main():
	co_main_titles()
	print "#####"

if __name__ == "__main__":
    main()