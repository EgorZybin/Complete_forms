# Web-приложение для определения заполненных форм

Это простое Flask приложение, которое принимает POST-запросы для определения форм и типов полей.

## Установка

1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/get-started)
   и [Docker Compose](https://docs.docker.com/compose/install/).

2. Клонируйте проект:

```
   git clone https://github.com/EgorZybin/Complete_forms;
   cd Complete_forms
```

3. Установите зависимости:

```
   pip install -r requirements.txt
```

4. Запустите приложение:

```
   docker-compose up --build
```

5. Проверьте, что приложение работает:

```
   python tests/test_requests.py
```

### Заключение

Теперь у вас есть полное приложение, упакованное в Docker, с простым тестовым скриптом и детальным README для настройки
и развертывания. Вы можете расширять функционал по мере необходимости и добавлять больше форм, тестов и т.д.