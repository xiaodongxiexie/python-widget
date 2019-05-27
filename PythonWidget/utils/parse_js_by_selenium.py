from lxml import etree
from pprint import pprint

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path=r"D:\DongData\backup\work_software\chromedriver.exe", options=options)

if __name__ == "__main__":

    url = "https://www.58.com/changecity.html"

    content = driver.get(url)
    content = driver.page_source
    html    = etree.HTML(content)

    provinces_cities_dict = {}
    provinces = html.xpath("//div[@class='content-province-title']/text()")
    for province in provinces:
        provinces_cities_dict[province] = html.xpath(f"//div[@class='content-province-title'][contains(text(), '{province}')]/following-sibling::div/a/text()")

    pprint(provinces_cities_dict)
