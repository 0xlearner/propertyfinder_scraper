# propertyfinder_scraper

- [Virtual enviornment] - Create a virtual environment

`mkdir property-finder`
`cd property-finder`
`python3.9 -m venv venv`
`source venv/bin/activate`

- [Git clone] - Download the source code from github

`git clone https://github.com/0xlearner/propertyfinder_scraper`
`cd propertyfinder_eg`

- [Running spiders] - Each scraper is run by it's own name e.g for sale category `scrapy crawl propertyfinder-sale-spider`

for rent `scrapy crawl propertyfinder-rent-spider`

for commercial `scrapy crawl propertyfinder-commercial-spider`

for new-projects `scrapy crawl propertyfinder-new-projects-spider`

Before running the spiders make sure to export the environment variables.

`# Heroku db creds
export DRIVER_NAME=postgresql
export HOST=ec2-44-197-128-108.compute-1.amazonaws.com
export PORT=5432
export USER_NAME=rkfdeysyblfosa
export PASSWORD=7d232a6dd02fc0878b6c2a07a697eaa0dc715c8ff65612a1a4e38d095d57bfb9
export DATABASE_NAME=d3u8gg7r0rqq4
export DATABASE_URL=postgresql://rkfdeysyblfosa:7d232a6dd02fc0878b6c2a07a697eaa0dc715c8ff65612a1a4e38d095d57bfb9@ec2-44-197-128-108.compute-export 1.amazonaws.com:5432/d3u8gg7r0rqq4

# Scrapeops API
export SCRAPEOPS_API_KEY=f02c8b09-19aa-4814-bf9b-a54abd833fe9`
