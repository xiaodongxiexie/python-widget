class MapFlatten:

    def __init__(self):
        self.out = {}

    def map_flatten(self, adict, key=""):
        for k, v in adict.items():
            nk = key + "." + k if key else k
            if isinstance(v, dict):
                self.map_flatten(v, key=nk)
            else:
                self.out[nk] = v


if __name__ == '__main__':
    adict = {
              "country": {
                    "China": {
                        "city": {
                            "nj": "2010",
                            "bj": "2011",
                            "hz": "2012"
                            }
                            },
                    "USA": {
                        "home": "whitehouse"
                        }
              }
}
    r = MapFlatten()
    r.map_flatten(adict)
    print(r.out)

  
  """output:
   {'country.China.city.bj': '2011',
    'country.China.city.hz': '2012',
    'country.China.city.nj': '2010',
    'country.USA.home': 'whitehouse'}
   """
