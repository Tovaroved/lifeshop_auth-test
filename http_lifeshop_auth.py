import http.client
import ssl

# URL страницы авторизации
url = "app.lifeshop.kg"

# Отключаем проверку SSL
context = ssl._create_unverified_context()

# Параметры запроса (Headers и Payload)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "_lifeshop_app_session=oHcmSWxbUcwRRjUXvlbaUYoF5VWwb5M%2BlOuc1uaA1QWVjHkgAUeYL%2BF7hgnt8Gb3OI8JDwH%2BsHPP6DVZeFgnG0Jh8VUzFOcnA63UqzMlmY4BddeGzkuqvTX19sG4PJ4ipLp8mHOoYLa5P6oQRXtYYh25S0VsXNCThrBpNB8hD0O0Tm1j6%2Fs8MP6Zf41tUE732WK015yyZlpZ0Bcxu0fGNDpo7s7K4GfmzxjqJ9ZHkKZa%2FrlMlkceFoau%2FORn2g7PGx0NKiLvRJBBdssyVOS%2F%2F%2Fqvw%2FoOS9ewVmA82W%2Btnz57%2F5wXOsOPMaTLvGi560SBlqX9F9qvAlBm--5l%2FsV2B0GtZdtlZe--i%2BqOV%2FOpFnRMOM4w2uLF%2BQ%3D%3D",
    "Host": "app.lifeshop.kg",
    "Origin": "https://app.lifeshop.kg",
    "Referer": "https://app.lifeshop.kg/auth/login",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

data = "authenticity_token=your_authenticity_token&user%5Bemail%5D=your_email&user%5Bpassword%5D=your_password&commit=%D0%92%D0%BE%D0%B9%D1%82%D0%B8"

# Выполняем POST-запрос для авторизации
conn = http.client.HTTPSConnection(url, context=context)
conn.request("POST", "/auth/login", body=data, headers=headers)

# Получаем ответ
response = conn.getresponse()

# Читаем и обрабатываем ответ
response_data = response.read()
print(response_data)


    # Записываем запрос и ответ в файлы

with open(f'name_response.html', 'wb') as f:
    f.write(response_data)

conn.close()
