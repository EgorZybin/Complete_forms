import requests


def test_post_request():
    url = 'http://localhost:5000/get_form'

    # Изменяем test_data на корректный формат
    test_data = {
        'email': 'test@example.com',
        'phone': '+7 123 456 78 90'
    }

    # Используем data вместо json
    response = requests.post(url, data=test_data)

    # Печатаем ответ сервера
    print('Response:', response.json())


def test_post_request_2():
    url = 'http://localhost:5000/get_form'

    test_data2 = {
        'date': '01.01.2000',
        'name': 'test'
    }

    # Используем data вместо json
    response = requests.post(url, data=test_data2)

    # Печатаем ответ сервера
    print('Response:', response.json())


if __name__ == "__main__":
    test_post_request()
    test_post_request_2()
