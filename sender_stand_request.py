import configuration
import requests
import data


def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,  # подставляем полный url
                         json=data.orders_body,  # тут тело
                         headers=data.headers) # а здесь заголовки


def get_orders_info (track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK + track)  # подставляем полный url




