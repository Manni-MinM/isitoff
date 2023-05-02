import json

import requests
from requests.adapters import HTTPAdapter, Retry

from urllib.parse import urljoin


DEFAULT_MAX_RETRIES=Retry(
    total=5,
    backoff_factor=1,
    allowed_methods=["GET"],
    raise_on_status=False,
    raise_on_redirect=False,
)

class IsitoffClient:
    base_url = "https://holidayapi.ir/jalali/"

    def __init__(self, **kwargs):
        adapter = HTTPAdapter(max_retries=DEFAULT_MAX_RETRIES)
        if "adapter" in kwargs:
            adapter = kwargs["adapter"]

        timeout = 15
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]

        self.http = requests.session()
        self.http.timeout = timeout

        self.http.mount("http://", adapter)
        self.http.mount("https://", adapter)

    def response_dict(self, path: str) -> dict:
        url = urljoin(self.base_url, path)

        try:
            resp = self.http.get(url)
            resp_dict = json.loads(resp.content)
            return resp_dict
        except Exception as err:
            raise(err)
