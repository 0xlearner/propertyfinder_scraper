import scrapy
import json
from bs4 import BeautifulSoup
import requests


class PropertyFinderCommercial(scrapy.Spider):
    name = "propertyfinder-commercial-spider"

    custom_settings = {
        "FEED_FORMAT": "csv",
        "FEED_URI": "propertyfinder-commercial.csv",
        "LOG_FILE": "propertyfinder-commercial-spider.log",
        # "ITEM_PIPELINES": {
        #     "propertyfinder_eg.pipelines.PropertyFinderCommercialPipeline": 300
        # },
    }

    cookies = {
        "audience": "new-user",
        "_gcl_au": "1.1.1448230514.1655083322",
        "__rtbh.lid": "%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22MiQoGGBwjLGWicMon6z6%22%7D",
        "_fbp": "fb.1.1655083326502.713391606",
        "visitor_id709273": "438507614",
        "visitor_id709273-hash": "b7504e7ee56e5d4491f186dcd78d6c9cf84f884622602ceedb01d25462dfbdf562ba211672b78ff9a6d8e21d5b91281a7ca67a37",
        "_hjSessionUser_385772": "eyJpZCI6ImRkNDI1ZDdiLTE0OTYtNWFlZi1iZDA0LTY5MzI4ZTE2NDg5MiIsImNyZWF0ZWQiOjE2NTUwODMzMjY3MjAsImV4aXN0aW5nIjp0cnVlfQ==",
        "pf-notification": "true",
        "g_state": '{"i_p":1656087797914,"i_l":3}',
        "_gid": "GA1.2.1194255553.1655636881",
        "__gpi": "UID=000008b53ee73303:T=1655083326:RT=1655713283:S=ALNI_MbpBKmWG69yvlMwBl5xywQpBh4j1g",
        "_sp_ses.32cc": "*",
        "_hjSession_385772": "eyJpZCI6IjFlYWVmM2U3LTBkZGYtNDUwNi04YjY4LWE3ZThmZjU3ZDNiMyIsImNyZWF0ZWQiOjE2NTU3MjQ3ODUzMTMsImluU2FtcGxlIjpmYWxzZX0=",
        "_hjAbsoluteSessionInProgress": "0",
        "cto_bundle": "LAG0CF9GY1MlMkZhSkJWaDBHM0NPRUhVOHlqWGtNaTdIZjI3Q0xJWUJtajQ3MTRPeEJPRFZqbThESjhzU29xRGZjVVB2dk0lMkYyMlpZc2MlMkJkdTd6TVFrMzV2akFzQ1M3Y3V5SmdHYTNSRSUyRkt4RE5teHp2QnZleE55aXBYZ2tIWk1BNUM0cmYyUkRFZlBQNWphS254eXYlMkJ0cVc5cFoyVjhJWGVLVHgzY2h1RkVTaVZoVVYwJTNE",
        "website_ab_tests": "test87%3Doriginal%2Ctest92%3Doriginal%2Ctest64%3DvariantA",
        "AKA_A2": "A",
        "_dd_l": "1",
        "_dd": "9b2e0ec3-c81d-449c-af7b-64a94cf89e9c",
        "bm_mi": "5982F61A0205D7DCACCC95DD23D01BE1~YAAQnig0F0e/Um+BAQAA2mtMgRA/QwA2ven8NQxNUqqahaUGeC2N2XVg6BSxtGB/7AEFVjDum8zfKywve2S68L9Lfq7BAVfe2a3cTXRSaeT1oCGfE37ZlHc7xrqNzYR2TR/4S+yT9fzz2bvug/HMdr5qSajq+Pvg1IP/ImrLrpdSR9LsPFg51yUl8tpjNNFW0ne3MwL+00sGR1VYT8VTpGOrSDKk2AM7bTFQ3jbdZX4SBZclIRXDIIJZ3QRoIDtivHMTQhtNEmkACTUr4fgo0nfhK9GU48iaUHV55d8VHPoJtTWEDD6YOlYqOHvy+tKh4TFkIrqIVhNAVNzh~1",
        "_sp_id.32cc": "ce2927e1-1c9b-4580-8671-18a309bd3813.1655083322.16.1655731679.1655713527.edeca332-13f1-4c09-93a7-c71bfe400e7e",
        "_dc_gtm_UA-2867119-13": "1",
        "_dc_gtm_UA-2867119-3": "1",
        "_ga_17NF7T4FBV": "GS1.1.1655724784.24.1.1655731679.57",
        "_ga": "GA1.1.1811748855.1655083325",
        "_hjIncludedInSessionSample": "0",
        "ak_bmsc": "4DD6AE90869364B6FF101974005A0006~000000000000000000000000000000~YAAQnig0F1e/Um+BAQAASopMgRBCZN8IKzKBYSGDqwwiVhLydsrUoK6f40dT60qqwoZ2ObNYxjjmwPUoYsYcqxNXyIBWbJMSfA8ft3Tayy4A1meln9Hc+7i5o3XgI/hRgyIbCoatlOytKEsU8MCztcZiGtuzEUKt6PBlI93B/NPmLHJ0dvZSkxhUcTCpfvXjYo1sH9FL8zDzRDZMEhRyf0v8Ca31QI4rV7wEGJCc/LIqtcMwk+N2EndmCM1kZZumyqicK6lRct3PLwbuHVuBmMiavyh40cWxGehNILtOEpirWWhy+39EAl1zEDh3bRrJe8JUNLxkd4eaz9zYdEHBKPtdkfZcQbsMSFFvmDNwtAJTwAObNyVB6GwnIubOGmCtIljew+4rlDzF9YtTFOKHAbPJrw8xl7VCt4vstwmJsb4sYWeO4zQ16eUi+UjrifWyM7OJyDbdswpXmb9s32Az1bm1VLmKycicwgkF8gImEoqPAmcahdD5PkZdGvmrnq+RvSl6DXDA6ScVUVo98kL7cToWdy0ZdKBvGsWcoe+XqDE=",
        "bm_sv": "E1C41F38738A577C31EF46A693AC8A60~YAAQnig0F1i/Um+BAQAASopMgRCp/O+4DzokcjMQp32JQqHPTMZ9Wm8/Y/ewu6zYJy28CvB0uwpsstYBX5KKKbAk4OlT/osYh7LD0RMnRGjVJCFVLTDnLK6BL4uyi/90Qzp6ulWsxUua11QivfFKIzXxT8r7Ot2UmM2dItwuYfPCsotMa3WciBFrZK1gVsZ5PD7OjpE2NA6b9ca4V0asdggWSG9932v7oGgn9N4hwzkCMOMKcxvutjGi0NmvKzmLgvjNh7BCEQ==~1",
        "__gads": "ID=c0ddfd769ae5fa6d:T=1655083326:RT=1655731686:S=ALNI_MapWF53QMIZAVjKyDA0Ji0ihXCMtQ",
    }

    headers = {
        "authority": "www.propertyfinder.eg",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en,ru;q=0.9",
        "cache-control": "max-age=0",
        "if-none-match": '"8acc9-8niBB0klGFkZoUL0NMR1kiS6xcg"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }

    base_url = (
        "https://www.propertyfinder.eg/en/commercial-rent/properties-for-rent.html"
    )

    def start_requests(self):
        yield scrapy.Request(
            url=self.base_url,
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse_property_listings,
        )

    def parse_property_listings(self, response):
        listing_urls = []
        listings = response.css('div[itemprop="itemListElement"] ::attr(href)').getall()
        for listing in listings:
            if listing.startswith("https://www.propertyfinder.eg"):
                listing_urls.append(listing)

        for idx, url in enumerate(listing_urls):
            if "?ref=listing" in url:
                listing_urls.remove(listing_urls[idx])

        for clean_url in listing_urls:
            yield scrapy.Request(
                url=clean_url,
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse_property_details,
            )

        next_page = response.css('link[rel="next"]::attr(href)').get()
        if next_page:
            yield scrapy.Request(
                url=next_page,
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse_property_listings,
            )

    def parse_property_details(self, response):
        item = {}
        data = (
            response.css('script[type="application/ld+json"]')[1]
            .get()
            .replace('<script type="application/ld+json">', "")
            .replace("</script>", "")
            .replace("\n", "")
            .replace(" ", "")
        )
        json_data = json.loads(data)

        item["URL"] = json_data[0]["mainEntity"]["url"]
        try:
            item["Breadcrumb"] = (
                response.css("div.breadcrumb a::text").get()
                + " "
                + ">"
                + " "
                + response.css("div.breadcrumb a::text")[1].get()
                + " "
                + ">"
                + " "
                + response.css("div.breadcrumb a::text")[2].get()
            )
        except:
            item["Breadcrumb"] = (
                response.css("div.breadcrumb a::text").getall()[0]
                + " "
                + ">"
                + " "
                + response.css("div.breadcrumb a::text").getall()[1]
            )
        item["Price"] = response.css("div.property-price__price::text").get().strip()
        item["Title"] = response.css("h1.property-page__title ::text").get().strip()
        item["Type"] = response.css("div.property-facts__content::text").get().strip()
        try:
            item["Bedrooms"] = (
                response.css("div.property-facts__content::text")
                .getall()[2]
                .replace("\t", "")
                .replace("\n", "")
            )
        except:
            item["Bedrooms"] = ""
        bathrooms_1 = response.css(
                "div.property-facts__content::text"
            ).getall()[3]
        bathrooms_2 = response.css(
                "div.property-facts__content::text"
            ).getall()[2]
        try:
            if bathrooms_1:
                item["Bathrooms"] = response.css(
                    "div.property-facts__content::text"
                ).getall()[3]
            else:
                item["Bathrooms"] = ''
        except:
            if bathrooms_2:
                item["Bathrooms"] = response.css(
                    "div.property-facts__content::text"
                ).getall()[2]
            else:
                item["Bathrooms"] = ''

        item["Area"] = str(json_data[1]["floorSize"]["value"]) + " " + "sqm"
        try:
            item["Location"] = (
                response.css("div.property-project-details__location-name::text").get()
                + ", "
                + response.css(
                    "div.property-project-details__location-path::text"
                ).get()
            )
        except:
            item["Location"] = (
                response.css("div.property-location__tower-name::text").get()
                + ", "
                + response.css("div.text--size1::text").get()
            )
        item["Agent_company"] = (
            response.css("div.property-agent ::text").extract()[2].strip()
        )
        item["Agent_name"] = (
            response.css("div.property-agent ::text").extract()[1].strip()
        )
        item["Description"] = " ".join(
            desc.strip()
            for desc in response.css('div[data-qs="text-trimmer"]::text').getall()
        )
        item["Amenities"] = ",".join(
            am.strip()
            for am in response.css("div.property-amenities__list::text").getall()
        )
        item["Reference"] = response.css(
            "div.property-page__legal-list-content ::text"
        ).getall()[0]
        item["Listed_date"] = response.css(
            "div.property-page__legal-list-content ::text"
        ).getall()[1]
        try:
            item["Image_url"] = json_data[0]["mainEntity"]["image"]
        except:
            item["Image_url"] = ""
        item["Phone_number"] = json_data[1]["telephone"]
        item["Map_location"] = ""
        # lat = json_data[1]["geo"]["latitude"]
        # long = json_data[1]["geo"]["longitude"]
        # google_search = f"https://www.google.com/search?q={lat}+{long}&sxsrf=ALiCzsY-43H18PCGXic0y8e-cQseF9da5w%3A1655665940280&ei=FHWvYp7WELaRxc8P1sm5mAI&ved=0ahUKEwiesPKhnLr4AhW2SPEDHdZkDiMQ4dUDCA4&uact=5&oq={lat}+{long}&gs_lcp=Cgdnd3Mtd2l6EAM6BwgjELADECc6BwgjEOoCECdKBQg8EgExSgQIQRgBSgQIRhgAUMgcWI-SAmCDmAJoAnAAeACAAfkBiAGjBZIBAzItM5gBAKABAaABArABCsgBAcABAQ&sclient=gws-wiz"
        # res = requests.get(google_search, headers=self.headers)
        # soup = BeautifulSoup(res.text, "lxml")
        # try:
        #     item["Map_location"] = (
        #         "https://www.google.com"
        #         + soup.find("div", {"class": "lu_map_section"}).next_element["data-url"]
        #     )
        # except:
        #     item["Map_location"] = ""

        yield item
