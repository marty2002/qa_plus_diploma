# Дипломный проект Яндекс Практикум. Инженер по тестированию расширенный

# Работа Коваленко Марии, 30я когорта

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Тест-кейс:
# 1. Клиент создает заказ
# 2. Проверяется, что по треку заказа можно получить данные о заказе.
def test_create_order_and_get_order_data():
    # создание нового заказа
    new_order_response = sender_stand_request.post_new_order(data.order_body_test)
    # сохранение номера заказа
    track = new_order_response.json()["track"]
    order_response = sender_stand_request.get_order_by_track(track)
    # проверка, что код ответа при получении данных заказа 200
    assert order_response.status_code == 200, "Ошибка! Код ответа сервера не равен 200."
