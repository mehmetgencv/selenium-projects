# selenium-projects

## Installing
You can download chrome driver from [here](https://chromedriver.chromium.org/downloads).

You should move driver file in to the ``driver/`` folder
```shell
$ cp .env-example .env
$ pip install -r requirements.txt
```

# Projects

### 1) Instagram Web Scraping
You can scrap instagram photos from search.
For example, you can download many photos about #cats

#### Usage
```shell
$ python instagram_web_scraping.py --keyword cats
```