from lxml import etree
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

    print(html.xpath("//div[@class='content-province-title']/text()"))