import scrapy
import json
from bs4 import BeautifulSoup
import requests


class PropertyFinderSale(scrapy.Spider):
    name = "propertyfinder-new-projects-spider"

    custom_settings = {
        "FEED_FORMAT": "csv",
        "FEED_URI": "propertyfinder-new-projects.csv",
        "LOG_FILE": "propertyfinder-new-projects-spider.log",
        # "ITEM_PIPELINES": {
        #     "propertyfinder_eg.pipelines.PropertyFinderNewProjectsPipeline": 300
        # },
    }

    cookies = {
    'audience': 'new-user',
    '_gcl_au': '1.1.1448230514.1655083322',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22MiQoGGBwjLGWicMon6z6%22%7D',
    '_fbp': 'fb.1.1655083326502.713391606',
    'visitor_id709273': '438507614',
    'visitor_id709273-hash': 'b7504e7ee56e5d4491f186dcd78d6c9cf84f884622602ceedb01d25462dfbdf562ba211672b78ff9a6d8e21d5b91281a7ca67a37',
    '_hjSessionUser_385772': 'eyJpZCI6ImRkNDI1ZDdiLTE0OTYtNWFlZi1iZDA0LTY5MzI4ZTE2NDg5MiIsImNyZWF0ZWQiOjE2NTUwODMzMjY3MjAsImV4aXN0aW5nIjp0cnVlfQ==',
    'pf-notification': 'true',
    'g_state': '{"i_p":1656087797914,"i_l":3}',
    '_gid': 'GA1.2.1194255553.1655636881',
    '__gads': 'ID=c0ddfd769ae5fa6d:T=1655083326:S=ALNI_MapWF53QMIZAVjKyDA0Ji0ihXCMtQ',
    '__gpi': 'UID=000008b53ee73303:T=1655083326:RT=1655740626:S=ALNI_MbpBKmWG69yvlMwBl5xywQpBh4j1g',
    'website_ab_tests': 'test87%3Doriginal%2Ctest92%3Doriginal%2Ctest64%3DvariantA',
    'cto_bundle': 'yfGRrl9GY1MlMkZhSkJWaDBHM0NPRUhVOHlqWG1pYzR3NzZzVTR6WXFHdDVodENUOFd3S29FeW5KOWxPaTFpaE9DeE5KU0l5anZ0eUExaVZabndjSWpjZUElMkJOa1kzTjR0WFQlMkZSOWhGTkVwUE1sODJyY3U1SjI5eGxBYXJYTyUyRllQMUdaRmNY',
    'AKA_A2': 'A',
    '_sp_ses.32cc': '*',
    '_dd_s': 'logs=1&id=f9b79fca-464f-439b-a17e-563a9a60c56a&created=1655751801148&expire=1655752702152',
    '_dd_l': '1',
    '_dd': '69a9b2b9-6312-49ab-bfe0-dc08168ec1b8',
    '_hjSession_385772': 'eyJpZCI6IjRhY2ViOTk4LTNhZjEtNGE1OS04NDQ3LWRmOTUwODQwODA1OCIsImNyZWF0ZWQiOjE2NTU3NTE4MDU3OTcsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga': 'GA1.2.1811748855.1655083325',
    '_ga_17NF7T4FBV': 'GS1.1.1655751711.27.1.1655751815.48',
    'ak_bmsc': '8BBB433D23A12A626F26A02AC8744EE8~000000000000000000000000000000~YAAQ1V8yuBfZFzqBAQAAjTSAghC4wFq36jDSPk88HMOVh83yfFeiJ8Qib3XhWBLH3wBKnwYjozAbJiZ3H1xYt4qck8P66NYSHL0unpoHtIjYFkuaGoGsBmW9JWs/M2AwjOp8QeE9LjvhpBOe1vqOjwwDE3J5rvmh6HCUo0wNP6qD5f2sALIaLWDbF20O9/AHvMehnB3tA5apBAvF4KuiXcHGNrXORnpYZp34c4/Dyg84hp4ghw04OJpAT46bP58FfDvlKMg5CvsGhIlSkamPsoGp4e0Ef5or53/rlqW7KhI/jPRKNJX2jQGKeF8/CHpylLkVACSz09oCFjYnFpEdvvOuO0yXt/BmpTsmtlQvaAs4yhRfDKu+uCpUzgTmP8ome/1M7zL0m7KZMik8J+u/47Un3AzQ4h2Iu9uguEegf7TRpOP69JsOSe7Gh4k0YT+OUJz7fDAEbXrBLb8ZVm03BHwFsYXlGhCDQQiWOWKwEoCLjl4o6GHPeMYROzVhXc0sPae0xJuWagqb0ScwINLyZvrZ',
    '_sp_id.32cc': 'ce2927e1-1c9b-4580-8671-18a309bd3813.1655083322.19.1655752207.1655749509.e49bc75d-0619-496a-9732-a4e444850c20',
    'bm_sv': 'FC7C90E3FBCB17A74FB09240CAE7821A~YAAQBNYsFxge8YCBAQAAi2eIghB0cRyNfHeqxAZvJWU4xSIPomCxnF+lXIzfI1kqkWYfJ40U2aMSKUYgTaJKGTv7m1MYvvvcgwGEsndQH6taDN259URYmACqHAE1lgme7UexsW43c+6UXPg5oSJTQBIQSjvuz2GhqN/FVhF72fC8Ls+9aWPrbk5LrdR4Pri2ZrCCuUMnbbYhRXvcvsUjzy512so4ps2zzaNs5CgC2stKTUsrj4fgr/yKwj3kl5TRm+CsjMkm3w==~1',
}

    headers = {
        "authority": "www.propertyfinder.eg",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en,ru;q=0.9",
        "cache-control": "max-age=0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }

    base_url = "https://www.propertyfinder.eg/en/new-projects"

    def start_requests(self):
        yield scrapy.Request(
            url=self.base_url,
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse_property_listings,
        )

    def parse_property_listings(self, response):
        urls = [
            "https://www.propertyfinder.eg" + url.css("::attr(href)").get()
            for url in response.css("li._1Aeoj1wO")
        ]

        for url in urls:
            yield scrapy.Request(
                url=url,
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse_property_details,
                meta={"listing_url": url},
            )

    def parse_property_details(self, response):
        item = {}

        item["URL"] = response.meta.get("listing_url")
        item["Breadcrumb"] = ""
        item["Price"] = response.css("span._1-htALWL::text").get()
        item["Title"] = response.css("h1._3ckSaLGM::text").get()
        item["Type"] = ""
        item["Bedrooms"] = response.css("span._1-htALWL::text").getall()[5]
        item["Bathrooms"] = ""

        item["Area"] = ""
        item["Location"] = response.css("div._3XeJbDEl").css("span::text").get()
        item["Agent_company"] = ""
        item["Agent_name"] = ""
        item["Description"] = response.css("div._3RInl69y ::text").get()
        try:
            item["Amenities"] = ", ".join(
                response.css("div._3RInl69y ::text").getall()[1:]
            )
        except:
            item["Amenities"] = ""
        item["Reference"] = ""
        item["Listed_date"] = ""
        item["Delivery_date"] = response.css("span._1-htALWL::text").getall()[3]
        item["Image_url"] = response.css("div._1rJE5wS3").css("img::attr(src)").get()
        item["Phone_number"] = (
            response.css("a._3s36E1-J._2kown_jA::attr(href)").get().replace("tel:", "")
        )
        item["Map_location"] = ""

        yield item
