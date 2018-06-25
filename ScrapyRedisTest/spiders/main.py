from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy", "crawl", "kkex_kline", '-atimeframe=1m']) 传递参数
execute(["scrapy", "crawl", "jobbole"])
