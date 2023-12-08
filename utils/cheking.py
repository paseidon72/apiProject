"""Методи для проверки наших запросов"""
import json
from requests import Response


class Checking():
    """"Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("GOOD STATUS CODE :" + str(response.status_code))
        else:
            print("BAD STATUS CODE :" + str(response.status_code))

    """Метод проверки обязательних полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Any value In stock")

    """Метод проверки значений обязательних полей в ответе запроса"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ": Ensue True")

    """Метод проверки значений обязательних полей в ответе запроса по заданому слову"""

    @staticmethod
    def check_json_search_world_value(response: Response, field_name, search_world):
        check = response.json()
        check_info = check.get(field_name)
        if search_world in check_info:
            print("World" + search_world + ": Ensue True")
        else:
            print("World" + search_world + ": Ensue False")
