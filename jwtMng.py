import config
from cryptography.fernet import Fernet


def get_encrypt_payload(user):
    config_obj = config.get()
    secret_key = config_obj.app.encrypt_key.encode()
    fernet_obj = Fernet(secret_key)
    enc_message = fernet_obj.encrypt(user.username.encode())
    return enc_message.decode()


def get_dencrypt_payload(payload_str):
    config_obj = config.get()
    secret_key = config_obj.app.encrypt_key.encode()
    fernet_obj = Fernet(secret_key)
    denc_message = fernet_obj.decrypt(payload_str)
    return denc_message
