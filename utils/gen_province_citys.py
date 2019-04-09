import requests

from lxml import etree
from pprint import pprint


# 从贝壳网来获取全国省-城市hash表
url = "https://www.ke.com/city/"


if __name__ == "__main__":
    response = requests.get(url)
    html     = etree.HTML(response.content)
    provinces = list(filter(lambda obj: obj, list(map(lambda obj: obj.strip(), html.xpath("//div[@class='city_province']/div/text()")))))
    province_citys_dict = {}
    for province in provinces:
        citys = html.xpath("//div[@class='city_province']/div[contains(text(), '{}')]/following-sibling::ul/li/a/text()".format(province))
        province_citys_dict[province] = citys
    pprint(province_citys_dict)
