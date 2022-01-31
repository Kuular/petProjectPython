import allure
import requests

data_post = {
    "id": 333333,
    "name": "Ellindos",
    "photoUrls": ["foto"],
    "tags": []
}

data_put = {
    "id": 333333,
    "name": "Ellizavr",
    "photoUrls": ["foto"],
    "tags": []
}

data_get = [
    {
        "id": 657774674,
        "username": "Elli one",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    },
    {
        "id": 657774675,
        "username": "Elli two",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
]


@allure.feature('Pet project')
@allure.story('Add new a pet to the store')
def test_pet_post():
    response = requests.post('https://petstore.swagger.io/v2/pet', json=data_post)
    print(response.text)
    assert response.json() == data_post


@allure.feature('Pet project')
@allure.story('Update an existing pet')
def test_pet_put():
    response = requests.put("https://petstore.swagger.io/v2/pet", json=data_put)
    print(response.text)
    assert response.json() == data_put


@allure.feature('Pet project')
@allure.story('Find pet by ID')
def test_pet_get():
    response = requests.get("https://petstore.swagger.io/v2/pet/" + str(data_post['id']))
    print(response.text)
    assert response.json() == data_post


@allure.feature('Pet project')
@allure.story('Creates list of users with given input array')
def test_pet_post_by_array():
    response = requests.post('https://petstore.swagger.io/v2/user/createWithArray', json=data_get)
    print(response.text)
    assert response.ok


@allure.feature('Pet project')
@allure.story('Get user by user name')
def test_pet_get_by_name():
    response = requests.get("https://petstore.swagger.io/v2/user/" + str(data_get[0].get('username')))
    print(response.text)
    assert response.json() == data_get[0]
