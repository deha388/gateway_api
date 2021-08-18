import json
import src.utils.providers.ocr_test.api.ocr_trigger as trigger


class Client:
    api_ocr = None

    def __init__(self, alias):
        self.alias = alias

    def set_alias(self, alias):
        self.alias = alias

    def trigger_process(self):
        credentials = json.loads(self.alias.credentials)
        service_url = credentials["url"]
        self.api_ocr = trigger.Ocr(service_url)
        return self.api_ocr.trigger_process()
