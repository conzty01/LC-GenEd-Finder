import scrapy

class CourseSpider(scrapy.Spider):
    name = "courseSpider"
    start_urls = ["https://www.luther.edu/catalog/curriculum/"]

    def parse(self, response):
        for href in response.css("ul.childrenList a::attr(href)"):
            yield response.follow(href, callback=self.parse_dept)

    def parse_dept(self, response):
        sub = response.css("h1.pageTitle span::text").extract_first()
        for cont in response.css("div.courseContainer"):
            yield {
                "number":cont.css("span.courseNumber::text").extract_first(),
                "title":cont.css("span.courseTitle::text").extract_first(),
                "subject":str(sub),
                "description":cont.css("span.courseDescription::text").extract_first(),
                "fulfills":cont.css("span.genEd::text").extract()
            }
