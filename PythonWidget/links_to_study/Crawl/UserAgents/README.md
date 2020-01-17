save some useful user-agent

```python

import json
import lxml

def get_agents(url):
    html = requests.get(url)
    html = lxml.etree.HTML(html.content)
    agents = html.xpath('//*[@id="liste"]/ul/li/a/text()')
    return agents
    
    
def dump_json(objs, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(objs, file, indent=1)
        
        
if __name__ == "__main__":

    home = "http://useragentstring.com/pages/useragentstring.php"
    root = "http://useragentstring.com"
    
    h = lxml.etree.HTML(requests.get(home).content)
    
    for postfix in h.xpath("//td/a/@href"):
        url = root + postfix
        name = url.split("name=")[-1]
        try:
            dump_json(get_agents(url), f"{name}.user.agents.list.json")
        except:pass
    
```
