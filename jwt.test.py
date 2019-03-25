import time
import jwt

service_account_id = "aje9ghlcdf6072u9377k"
key_id = "ajeoirkca0b0csbj0igb" # ID ресурса Key, который принадлежит сервисному аккаунту.

with open("private.pem", 'r') as private:
    private_key = private.read() # Чтение закрытого ключа из файла.
now = int(time.time())
payload = {
    'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
    'iss': service_account_id,
    'iat': now,
    'exp': now + 360}  # Формирование JWT.
encoded_token = jwt.encode(
    payload,
    private_key,
    algorithm='PS256',
    headers={'kid': key_id})
print(encoded_token)
