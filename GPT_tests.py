import requests

# URL страницы авторизации
url = "https://app.lifeshop.kg/auth/login"
logout_url = "https://app.lifeshop.kg/auth/logout"

logins1, passwords1, names1 = [
    'sulaimanovuran@gmail.com',
    'macbookfrombro@gmail.com',
    'brayanbekgriffin@gmail',
], [
    'murakami670',
    'macbro1v',
    'murakami670',
], [
    "Уран",
    "Влад",
    "Леша",
]

tokens = [
    "c5fGLAMdgl5cQHQ-n3gXCj4BeamZVRQIvYyepWlp9IlX4NdITG2hqK5nu0LdoR_A93ChE2Sj088NjX6YbNtWUQ",
    "H9KCkv3p2bLnqe65hUe_UsXCUQLS7FeLInZqwIKwWaacq9W8beGLogtwXuqlNQmWat9yOvbOCoAjlRvfAZ6arA",
    "qOfmad13GIqU0pkTFHsKqIsAxVeEK_M1og8oRafNyBa_jYFgePSd9bpSYqVwycRoxS1UBUtEW2_TOyo-tIaI_g"
]

logout_tokens = [
    "hLBc8fcKsBzXH5O--NiYyZJ7gs7VqkMktlxGRtFoBeW37-SQ7-RJjtJwZwcZ0CXYIICenxD4bbPwrWpsc6A2WA",
    "bP-omybBihMjvlLoEz4d-g5Lx73FERagq_Ao5y29K1hicx5SvSJ2rO-1kn6wcezrwkTMuArNP4dB9rln6UsA5A",
    "l8883HvkyIem28tlpCFfJWVTzc9guxPahRUDCmS-r5F8nP238CnXZKMBpPzqAznv5rIKa3t653gXaXxtfFNyGQ"
]

# Создаем объект Session
session = requests.Session()

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

for l, p, n, t, lt in zip(logins1, passwords1, names1, tokens, logout_tokens):
    data = {
        "authenticity_token": t,
        "user[email]": l,
        "user[password]": p,
        "commit": "Войти"
    }

    logout_data = {
        "_method": "delete",
        "authenticity_token": lt
    }

    # Выполняем POST-запрос для авторизации
    response = session.post(url, headers=headers, data=data)

    # Проверяем статус код ответа
    with open(f'{n}.html', 'w') as f:
        f.write(response.text)

    # Завершаем сессию перед переходом ко второму аккаунту
    response = session.post(logout_url, headers=headers, data=logout_data)
