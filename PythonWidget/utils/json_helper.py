
import json
import datetime
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return super(DateEncoder, self).default(o)


class DecimalDateEncoder(DecimalEncoder, DateEncoder):
    """转换date, datetime, decimal为可json
    """


class JsonHelper(object):

    @classmethod
    def load_json(cls, path, **kwargs):
        with open(path, encoding="utf-8") as file:
            data = json.load(file, **kwargs)
            return data

    @classmethod
    def dump_json(cls, content, path, verbose=True, **kwargs):
        with open(path, "w", encoding="utf-8") as file:
            indent = kwargs.pop("indent", 1)
            json.dump(content, file,  
                      ensure_ascii=False, 
                      indent=indent,
                      cls=DecimalDateEncoder, 
                      **kwargs)
            if verbose:
                print("save success, save path: {}".format(path))
