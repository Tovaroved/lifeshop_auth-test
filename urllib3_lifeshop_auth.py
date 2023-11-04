import urllib3
import urllib.parse


http = urllib3.PoolManager(cert_reqs='CERT_NONE')


username = "sulaimanovuran@gmail.com"
password = "murakami670"
data = {
    'username': username,
    'password': password
}

# Кодируем данные
encoded_data = urllib.parse.urlencode(data).encode('utf-8')

url = "https://app.lifeshop.kg/auth/login"
response = http.request('POST', url, body=encoded_data)

# Проверить статус код ответа
if response.status == 200:
    print("Успешно авторизованы!")
else:
    print("Не удалось авторизоваться. Статус код:", response.status)
