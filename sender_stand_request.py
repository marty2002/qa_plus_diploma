# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Функция отправки POST-запроса на создание нового пользователя
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Функция получения заказа по треку заказа
def get_order_by_track(track):
    params = {
       't': track
   }

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + "?",
                        params=params)