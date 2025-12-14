## [Описание]
- [Финальная работа по ручному тестированию](https://gorshenin.yonote.ru/doc/otchyot-o-testirovanii-internet-magazina-chitaj-gorod-DfIT9e06M7)
- Автотесты для сайта Читай-Город .

Сайт: https://www.chitai-gorod.ru/

Функционал:
Поиск книг

## [Структура]
-config
  - settings.py


- pages - классы

    pages/api_page.py
    pages/main_page.py

tests - тесты

    tests/test_api.py
    tests/test_ui.py


pytest.ini - маркеры для запуска pytest

README.md - отчет-инструкция к работе

config.py - конфигурации

requirements.txt - зависимости)

## [Инструкция по работе с тестами]
### Инструкция по работе с тестами
Устанавливаем зависимости из файла requirements.txt. Команда pip install -r requirements.txt
### Запуск API тестов:

Команда `pytest tests/test_api.py --alluredir=./allure_result_api`
После завершения тестирования вводим команду allure serve allure_result_api для просмотра отчета о тестировании
Запуск UI тестов:

Команда `pytest tests/test_ui.py --alluredir=./allure_result_ui`
После завершения тестирования вводим команду allure serve allure_result_ui для просмотра отчета о тестировании
Запуск всех тестов:

Команду `pytest --alluredir=./allure_result_all`
После завершения тестирования вводим команду allure serve allure_result_all для просмотра отчета о тестировании

## [Стек технологий]
- pytest - основная библиотека для написания и выполнения тестов.
- selenium - библиотека для автоматизации UI тестирования.
- requests - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- allure - библиотека для генерации отчетов о выполнении тестов.

  

  