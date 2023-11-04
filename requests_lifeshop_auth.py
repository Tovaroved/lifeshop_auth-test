import requests
from requests import Session

# URL страницы авторизации
url = "https://app.lifeshop.kg/auth/login"

logins1,passwords1,names1 = [
    'sulaimanovuran@gmail.com',
    'macbookfrombro@gmail.com', 
    'brayanbekgriffin@gmail.com',

],[
    'murakami670',
    'macbro1v',
    'murakami670',

],[
    "Уран",
    "Влад",
    "Леша",
]

tokens =[
    "c5fGLAMdgl5cQHQ-n3gXCj4BeamZVRQIvYyepWlp9IlX4NdITG2hqK5nu0LdoR_A93ChE2Sj088NjX6YbNtWUQ",
    "H9KCkv3p2bLnqe65hUe_UsXCUQLS7FeLInZqwIKwWaacq9W8beGLogtwXuqlNQmWat9yOvbOCoAjlRvfAZ6arA",
    "qOfmad13GIqU0pkTFHsKqIsAxVeEK_M1og8oRafNyBa_jYFgePSd9bpSYqVwycRoxS1UBUtEW2_TOyo-tIaI_g"
]

# Параметры запроса (Headers и Payload) согласно данным, которые вы предоставили
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "_lifeshop_app_session=oHcmSWxbUcwRRjUXvlbaUYoF5VWwb5M%2BlOuc1uaA1QWVjHkgAUeYL%2BF7hgnt8Gb3OI8JDwH%2BsHPP6DVZeFgnG0Jh8VUzFOcnA63UqzMlmY4BddeGzkuqvTX19sG4PJ4ipLp8mHOoYLa5P6oQRXtYYh25S0VsXNCThrBpNB8hD0O0Tm1j6%2Fs8MP6Zf41tUE732WK015yyZlpZ0Bcxu0fGNDpo7s7K4GfmzxjqJ9ZHkKZa%2FrlMlkceFoau%2FORn2g7PGx0NKiLvRJBBdssyVOS%2F%2F%2Fqvw%2FoOS9ewVmA82W%2Btnz57%2F5wXOsOPMaTLvGi560SBlqX9F9qvAlBm--5l%2FsV2B0GtZdtlZe--i%2BqOV%2FOpFnRMOM4w2uLF%2BQ%3D%3D",
    "Host": "app.lifeshop.kg",
    "Origin": "https://app.lifeshop.kg",
    "Referer": "https://app.lifeshop.kg/auth/login",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}


data = {
    "authenticity_token": tokens[0],
    "user[email]": logins1[0],
    "user[password]": passwords1[0],
    "commit": "Войти"
}

# Выполняем POST-запрос для авторизации
response = requests.post(url, headers=headers, data=data)

# Проверяем статус код ответа
with open(f'{names1[0]}.html','w') as f:
    f.write(response.text)


logout_url = "https://app.lifeshop.kg/auth/logout"
response = requests.post(logout_url, headers=headers,data=data)

data = {
    "authenticity_token": tokens[1],
    "user[email]": logins1[1],
    "user[password]": passwords1[1],
    "commit": "Войти"
}

# Выполняем POST-запрос для авторизации
response = requests.post(url, headers=headers, data=data)

# Проверяем статус код ответа
with open(f'{names1[1]}.html','w') as f:
    f.write(response.text)
