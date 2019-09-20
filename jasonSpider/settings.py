# -*- coding: utf-8 -*-

# Scrapy settings for jasonSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jasonSpider'

SPIDER_MODULES = ['jasonSpider.spiders']
NEWSPIDER_MODULE = 'jasonSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jasonSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  #   'Referer': 'https://www.cnblogs.com/',
  #   'Accept-Encoding': 'gzip, deflate, br',
  #   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  #   'Method': 'GET',
  #   'Authority': 'www.cnblogs.com',
  #   'Cookie': '_ga=GA1.2.2102059732.1531759815; Qs_lvt_289801=1552891808%2C1554165719; Qs_pv_289801=1431315049922028800%2C125109502466263840; Hm_lvt_d8d668bc92ee885787caab7ba4aa77ec=1555816373; Hm_lvt_e7832a384d37994887357af186b47e63=1557969978; UM_distinctid=16b272104d02b3-08ddc8e881500d-37647e03-13c680-16b272104d1482; CNZZDATA1272990511=587500636-1560043096-https%253A%252F%252Fwww.baidu.com%252F%7C1560043096; CNZZDATA1254929547=2079358424-1559728158-https%253A%252F%252Fwww.baidu.com%252F%7C1563764734; Hm_lvt_444ece9ccd5b847838a56c93a0975a8b=1563765147; CNZZDATA1254128672=116913883-1567943776-https%253A%252F%252Fcn.bing.com%252F%7C1567943776; Hm_lvt_fa5cea7cd463480c76a420af9fa8973e=1567949567; _gid=GA1.2.450494227.1568875369',
  #   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jasonSpider.middlewares.JasonspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jasonSpider.middlewares.JasonspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'jasonSpider.pipelines.JasonspiderPipeline': 300,
    'jasonSpider.pipelines.CleanPipeline': 300,
    # 'jasonSpider.pipelines.JsonPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
