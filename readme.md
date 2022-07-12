Тестовое задание по автоматизации тестирования.

В рамках тестового задания предлагается сделать тесты по REST API.

Сценарий теста REST API:
https://swapi.dev/

Действия:
1. Получить список сущностей;
2. Получить список фильмов (films) и информацию по одному фильму
3. Получить список планет (planets) и информацию по планете выбранного вам
фильма
4. Получить список рас (Species) народов одной из планет выбранного вами фильма
5. Получить список пилотов (peoples) космического корабля из выбранного вам
фильма



pip install jsonpath-ng
https://pypi.org/project/jsonpath-ng/

run with allure:
pytest main.py::TestSwapiApi::test_list_species_of_planet_in_film --alluredir="E:\python_scripts\code\neoflex\allure-results"
pytest main.py::TestSwapiApi::test_list_people_by_film --alluredir="E:\python_scripts\code\neoflex\allure-results"


allure serve E:\python_scripts\code\neoflex\allure-results