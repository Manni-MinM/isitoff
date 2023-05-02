import datetime
import jdatetime

from dotmap import DotMap

from .client import IsitoffClient


class Isitoff:
    def __init__(self, **kwargs):
        self.client = IsitoffClient()
        if "adapter" in kwargs:
            adapter = kwargs["adapter"]
            self.client = IsitoffClient(adapter=adapter)

    def get_jalali(self, date):
        date_string = date.strftime("%Y/%m/%d")
        resp_dict = self.client.response_dict(date_string)
        return DotMap(resp_dict)

    def get_gregorian(self, date):
        jalali_date = jdatetime.date.fromgregorian(date=date)
        resp_dotmap = self.get_jalali(jalali_date)
        return resp_dotmap
