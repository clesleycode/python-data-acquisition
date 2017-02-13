import scrapy 


class BrickSetSpider(scrapy.Spider):
	name = "bricket_spider"
	start_urls = ['http://brickset.com/sets/year-2016']
	
	def parse(self, response):
		SET_SELECTOR = '.set'
		for brickset in response.css(SET_SELECTOR):
			NAME_SELECTOR = 'h1 a ::text'
			yield {
				'name': brickset.css(NAME_SELECTOR).extract_first(),
				'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
			}
			NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
			next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
			if next_page:
				yield scrapy.Request(
					response.urljoin(next_page),
					callback=self.parse
				)
