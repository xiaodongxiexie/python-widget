# coding: utf-8
# Author: xiaodong
# Date  : 2019/11/2

import requests
from lxml.etree import HTML


def get_star_url(start_url):
    result = requests.get(start_url)
    html = HTML(result.content)
    skip_url_nodes = html.xpath("//h3/a/@href")
    skip_item_names = filter(lambda obj: obj.strip(), html.xpath("//h3/a/text()"))
    for skip_url, skip_item in zip(skip_url_nodes, skip_item_names):
        yield (skip_item, "htpps://github.com" + skip_url)

    skip_btn = html.xpath("//div[@class='BtnGroup']/a/@href")
    skip_content = html.xpath("//div[@class='BtnGroup']/a/text()")
    if "Next" in skip_content:
        next_url = skip_btn[skip_content.index("Next")]
        yield from get_star_url(next_url)


if __name__ == '__main__':

    url = "https://github.com/xiaodongxiexie?tab=stars"
    results = list(get_star_url(url))
    print(results)
