import pytest
import allure
import requests
from data_for_test.auth import *


@allure.feature("sign-up")
@allure.story("Обычная регистрация")
@allure.description("Позитивный кейс на проверку регистрации с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_sign_up(vpn_api):
    registration_data = {
        "email": 'qwerty@yandex.ru',
        "password": 'qweqweqwe',
        "password_confirmation": 'qweqweqwe'
    }
    response = requests.post("https://site.test.infra.gnuvpn.com/api/v1/sign-up", data = registration_data)
    # response = vpn_api.post("sign-up", data=registration_data, headers=auth_headers)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        assert response.text != '', f"Неверный ответ, получен  {response.text}"
    print(response.text)

# Можно добавить различное количество негативных проверок для входных данных
@allure.feature("sign-up")
@allure.story("Негативная регистрация")
@allure.description("Негативный кейс на проверку регистрации.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("account", [("Qa@qa.ru", "123123123"), ("qwe@qa.ru", "qweqweqwe")])
def test_sign_up_negative( vpn_api, account):
    registration_data = {"email": {account[0]},"password": {account[1]},"password_confirmation": {account[1]}}
    response = vpn_api.post(path="sign-up", data=registration_data)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        assert response.text != '', f"Неверный ответ, получен  {response.text}"
    print(response.text)

@allure.feature("sign-in")
@allure.story("Позитивная авторизация")
@allure.severity(allure.severity_level.BLOCKER)
def test_sign_in(vpn_api):
    auth_data = {}
    # response = vpn_api.post("sign-in/", auth_data)
    response = requests.post("https://site.test.infra.gnuvpn.com/api/v1/sign-in", auth_data)
    # response = requests.request("POST", url="https://site.test.infra.gnuvpn.com/api/v1/sign-in", data=auth_data )
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        assert response.text != '', f"Неверный ответ, получен  {response.text}"
    print(response.text)

def test_test(vpn_api):
    pass

# def test_get_random_dog(dog_api):
#     response = dog_api.get("breeds/image/random")
#
#     with allure.step("Запрос отправлен, посмотрим код ответа"):
#         assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
#
#     with allure.step("Запрос отправлен. Десериализируем ответ из json в словарь."):
#         response = response.json()
#         assert response["status"] == "success"
#
#     with allure.step(f"Посмотрим что получили {response}"):
#         with allure.step(f"Вложим шаги друг в друга по приколу"):
#             with allure.step(f"Наверняка получится что-то интересное"):
#                 pass
#
#
# @pytest.mark.parametrize("breed", [
#     "afghan",
#     "basset",
#     "blood",
#     "english",
#     "ibizan",
#     "plott",
#     "walker"
# ])
# def test_get_random_breed_image(dog_api, breed):
#     response = dog_api.get(f"breed/hound/{breed}/images/random")
#     response = response.json()
#     assert breed in response["message"], f"Нет ссылки на изображение с указанной породой, ответ {response}"
#
#
# @pytest.mark.parametrize("file", ['.md', '.MD', '.exe', '.txt'])
# def test_get_breed_images(dog_api, file):
#     response = dog_api.get("breed/hound/images")
#     response = response.json()
#     result = '\n'.join(response["message"])
#     assert file not in result, f"В сообщении есть файл с расширением {file}"
#
#
# @pytest.mark.parametrize("breed", [
#     "african",
#     "boxer",
#     "entlebucher",
#     "elkhound",
#     "shiba",
#     "whippet",
#     "spaniel",
#     "dvornyaga"
# ])
# def test_get_random_breed_images(dog_api, breed):
#     response = dog_api.get(f"breed/{breed}/images/")
#     response = response.json()
#     assert response["status"] == "success", f"Не удалось получить список изображений породы {breed}"
#
#
# @pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
# def test_get_few_sub_breed_random_images(dog_api, number_of_images):
#     response = dog_api.get(f"breed/hound/afghan/images/random/{number_of_images}")
#     response = response.json()
#     final_len = len(response["message"])
#     assert final_len == number_of_images, f"Количество фото не {number_of_images}, а {final_len}"
