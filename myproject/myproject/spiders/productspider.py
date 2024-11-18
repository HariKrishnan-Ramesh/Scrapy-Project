import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    def parse(self, response):
        for products in response.css('article.fbc619bc._058bd30f'):
            yield{

                property_id : "",
                purpose : "",
                type : "",
                added_on : "22 April 2021",
                furnishing: "Unfurnished",
                price: {
                    currency : "",
                    amount: ""
                },
                location: "",
                bed_bath_size : {
                bedrooms : "" ,
                bathrooms : "",
                size : ""
                },
            }
