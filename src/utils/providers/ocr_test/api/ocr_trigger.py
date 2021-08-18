import requests


class Ocr:
    def __init__(self, service_url):
        self.service_url = service_url

    def trigger_process(self):
        endpoint = "api/trigger"
        trigger_url = self.service_url + endpoint
        trigger_res = requests.get(trigger_url)
        return trigger_res.json(), trigger_res.status_code
