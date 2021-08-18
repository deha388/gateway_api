import src.utils.providers.rasa_test.api.rasa_trigger as clients


class Client:
    api_client = None

    def __init__(self, alias):
        self.alias = alias

    def set_alias(self, alias):
        self.alias = alias

    def get_customers(self):
        self.api_client = clients.Client()
        return self.api_client.get_customers()
