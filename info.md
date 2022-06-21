smart_ads = response.css('div.smart-ad__list')
ads_url = []
if smart_ads:
    ads = smart_ads.css('::attr(href)').getall()
    for ad in ads:
        ads_url.append(ad)
listing = response.css('div[data-qs="property-list"] ::attr(href)').getall()
for li_url in listing:
    ads_url.append(li_url)

listings = response.css('div[itemprop="itemListElement"] ::attr(href)').getall()
listing_url = []
for listing in listings:
    if listing.startswith('https://www.propertyfinder.eg'):
            listing_url.append(listing)


data = response.text[283772:308724].replace('\n', '').replace(' ', '').replace('window.propertyfinder.settings.property={payload:', '')
json_data = json.loads(data)

URL = data_json['data']['attributes']['share_url']
Breadcrumb = response.css('div.breadcrumb a::text').get() + ' ' + '>' + ' ' + response.css('div.breadcrumb a::text')[1].get() + ' ' + '>' + ' ' +  response.css('div.breadcrumb a::text')[2].get()
Price = response.css('div.property-price__price::text').get().strip()
Title = response.css('h1.property-page__title ::text').get().strip()
Type = response.css('div.property-facts__content::text').get().strip()
Bedrooms = response.css('div.property-facts__content::text').getall()[2].replace('\t', '').replace('\n', '')
Bathrooms = response.css('div.property-facts__content::text').getall()[3]


Area = json_data['data']['attributes']['area']
Location = json_data['data']['attributes']['location_tree_path']
Agent_company = json_data['included'][0]['attributes']['name']
Agent_name = json_data['included'][3]['attributes']['name']
Description = ' '.join(desc.strip() for desc in response.css('div.text-trim.property-description__text-trim::text').getall())
Amenities = [am.strip() for am in response.css('div.property-amenities__list::text').getall()]
Reference = response.css('div.property-page__legal-list-content ::text').getall()[0]
Listed_date = response.css('div.property-page__legal-list-content ::text').getall()[1]
Image_URL = json_data['data']['links']['image_property']
Phone_number = json_data['included'][3]['attributes']['phone']
lat = json_data['data']['attributes']['coordinates']['lat']
long = json_data['data']['attributes']['coordinates']['long']
google_search = f'https://www.google.com/search?q={lat}+{long}&sxsrf=ALiCzsY-43H18PCGXic0y8e-cQseF9da5w%3A1655665940280&ei=FHWvYp7WELaRxc8P1sm5mAI&ved=0ahUKEwiesPKhnLr4AhW2SPEDHdZkDiMQ4dUDCA4&uact=5&oq={lat}+{long}&gs_lcp=Cgdnd3Mtd2l6EAM6BwgjELADECc6BwgjEOoCECdKBQg8EgExSgQIQRgBSgQIRhgAUMgcWI-SAmCDmAJoAnAAeACAAfkBiAGjBZIBAzItM5gBAKABAaABArABCsgBAcABAQ&sclient=gws-wiz'
res = requests.get('https://www.google.com/search?q=30.964159+28.753507&sxsrf=ALiCzsY-43H18PCGXic0y8e-cQseF9da5w%3A1655665940280&ei=FHWvYp7WELaRxc8P1sm5mAI&ved=0ahUKEwiesPKhnLr4AhW2SPEDHdZkDiMQ4dUDCA4&uact=5&oq=30.964159+28.753507&gs_lcp=Cgdnd3Mtd2l6EAM6BwgjELADECc6BwgjEOoCECdKBQg8EgExSgQIQRgBSgQIRhgAUMgcWI-SAmCDmAJoAnAAeACAAfkBiAGjBZIBAzItM5gBAKABAaABArABCsgBAcABAQ&sclient=gws-wiz', headers=google_headers)
soup = BeautifulSoup(res.text, 'lxml')
Map_location = 'https://www.google.com' + soup.find('div', {'class': 'lu_map_section'}).next_element['data-url']


next_page = response.css('a.pagination__link--next::attr(href)').get()
next_url = 'https://www.propertyfinder.eg' + next_page

urls = ['https://www.propertyfinder.eg' + url.css('::attr(href)').get() for url in response.css('li._1Aeoj1wO')]

phone = response.css('a._3s36E1-J._2kown_jA::attr(href)').get().replace('tel:', '')
price = response.css('span._1-htALWL::text').get()
title = response.css('h1._3ckSaLGM::text').get()
bedrooms = response.css('span._1-htALWL::text').getall()[5]
location = response.css('div._3XeJbDEl').css('span::text').get()
delivery_date = response.css('span._1-htALWL::text').getall()[3]
description = response.css('div._3RInl69y ::text').get()
amenities = ', '.join(response.css('div._3RInl69y ::text').getall()[1:])
image_url = response.css('div._1rJE5wS3').css('img::attr(src)').get()