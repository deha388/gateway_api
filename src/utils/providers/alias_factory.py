import sys
import src.utils.providers.test.client as test_client
import src.utils.providers.ocr_test.client as ocr_test_client
import src.utils.providers.rasa_test as rasa_test_client

module = sys.modules[__name__]


def get(alias):

    # registered_client = get_registered_client(alias=alias)
    # if registered_client:
    #     registered_client.set_alias(alias)
    #     return registered_client

    aliases = {
        "test": test_build,
        "ocr_test": ocr_test_build
        #"rasa_test":rasa_test_build
    }

    alias_build_fn = aliases.get(alias.service_name, "There is no matching provider for this alias -> " + str(alias))
    if isinstance(alias_build_fn, str):
        raise alias_build_fn

    client_obj = alias_build_fn(alias)
    register(alias, client_obj)
    return get_registered_client(alias=alias) # a=Client(alias="ocr_test with column")


def register(alias, client_obj):
    setattr(module, alias.name, client_obj)
def get_registered_client(alias):
    return getattr(module, alias.name, None)
def test_build(alias):
    return test_client.Client(alias=alias)
def ocr_test_build(alias):
    return ocr_test_client.Client(alias=alias) #object with attr alias
def rasa_test_build(alias):
    return rasa_test_client.Client(alias=alias)
