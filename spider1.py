# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scrapy


class spider1(scrapy.Spider):
    name = "spider1"
    start_urls = [
        'https://www.goodreads.com/quotes?page=1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('div.quoteText::text').extract_first(),
                'author': quote.css('span.authorOrTitle::text').extract_first(),         
            }

        next_page = response.css('a.next_page::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)