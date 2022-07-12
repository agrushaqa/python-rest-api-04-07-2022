import allure
import pytest
from neoflex_rest.SwapiApi import SwapiApi

class TestSwapiApi:
    @allure.story('swapi api')
    @allure.title('get common info')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    def test_common_info(self, path):
        allure.dynamic.description('''
        1. Получить список сущностей;
        2. Получить список фильмов (films) и информацию по одному фильму
        3. Получить список планет (planets) и информацию по планете выбранного вам
        фильма
        4. Получить список рас (Species) народов одной из планет выбранного вами фильма
        5. Получить список пилотов (peoples) космического корабля из выбранного вам
        фильма
        ''')
        api = SwapiApi()
        api.check_list_entity(f"{path}api")

    @allure.story('swapi api')
    @allure.title('get list films')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    def test_list_film(self, path):
        allure.dynamic.description('''
        2. Получить список фильмов (films)
        ''')
        api = SwapiApi()
        api.check_list_films(f"{path}api/films")

    @allure.story('swapi api')
    @allure.title('check film properties')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    @pytest.mark.parametrize("film_index, expected_title, expected_director, expected_release_date",
                             [("1", "A New Hope", "George Lucas", "1977-05-25"),
                              ("2", "The Empire Strikes Back", "Irvin Kershner", "1980-05-17")])
    def test_film_properties(self, path, film_index, expected_title, expected_director, expected_release_date):
        allure.dynamic.description('''
        2. Получить информацию по одному фильму
        ''')
        api = SwapiApi()
        api.check_film_info(f"{path}/api/films/{film_index}",
                                  expected_title,
                                  expected_director,
                                  expected_release_date)

    @allure.story('swapi api')
    @allure.title('get list planets')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    def test_list_planet(self, path):
        allure.dynamic.description('''
        3. Получить список планет (planets) 
        ''')
        api = SwapiApi()
        api.check_list_planets(f"{path}api/planets")

    @allure.story('swapi api')
    @allure.title('get planet info by film')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    @pytest.mark.parametrize("film_index, expected_titles",
                             [("1", ['Tatooine', 'Alderaan', 'Yavin IV']),
                              ("4", ['Tatooine', 'Naboo', 'Coruscant'])])
    def test_info_planel_by_film(self, path, film_index, expected_titles):
        allure.dynamic.description('''
        3. Получить информацию по планете выбранного вам фильма
        ''')
        api = SwapiApi()
        list_of_planet_urls = api.get_list_planets_by_film(f"{path}api/films/{film_index}")
        list_planets = []
        for i_planet in list_of_planet_urls[0]:
            list_planets.append(api.get_planet_name(i_planet)[0])
        assert list_planets == expected_titles

    @allure.story('swapi api')
    @allure.title('get list species of planet in film')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    @pytest.mark.parametrize("film_index, expected_species",
                             [("1", ['Human', 'Droid', 'Wookie', 'Rodian', 'Hutt']),
                              ("4", ['Human', 'Droid', "Yoda's species", 'Neimodian', 'Gungan', 'Toydarian',
                                     'Dug', "Twi'lek", 'Aleena', 'Vulptereen', 'Xexto', 'Toong', 'Cerean',
                                     'Nautolan', 'Zabrak', 'Tholothian', 'Iktotchi', 'Quermian', 'Kel Dor', 'Chagrian'])])
    def test_list_species_of_planet_in_film(self, path, film_index, expected_species):
        allure.dynamic.description('''
        Получить список рас (Species) народов одной из планет выбранного вами фильма
        ''') # TODO для планеты https://swapi.dev/api/planets/1/ не указан список рас.
        # поэтому здесь мы выводим список раc для фильма
        api = SwapiApi()
        # list_of_planet_urls = api.get_list_planets_by_film(f"{path}api/films/{film_index}")
        # first_planet_url = list_of_planet_urls[0][0]
        list_url_species = api.get_list_url_species_in_film(f"{path}api/films/{film_index}")
        list_species = []
        for i_url_species in list_url_species[0]:
            list_species.append(api.get_species_name(i_url_species)[0])
        assert list_species == expected_species

    @allure.story('swapi api')
    @allure.title('get planet info by film')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://swapi.dev/')
    @pytest.mark.parametrize("film_index, expected_people",
                             [("1", ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars',
                                     'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi',
                                     'Wilhuff Tarkin', 'Chewbacca', 'Han Solo', 'Greedo', 'Jabba Desilijic Tiure',
                                     'Wedge Antilles', 'Jek Tono Porkins', 'Raymus Antilles']),
                              ("4", ['C-3PO', 'R2-D2', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Jabba Desilijic Tiure',
                                     'Yoda', 'Palpatine', 'Qui-Gon Jinn', 'Nute Gunray', 'Finis Valorum',
                                     'Padmé Amidala', 'Jar Jar Binks', 'Roos Tarpals', 'Rugor Nass', 'Ric Olié',
                                     'Watto', 'Sebulba', 'Quarsh Panaka', 'Shmi Skywalker', 'Darth Maul',
                                     'Ayla Secura', 'Ratts Tyerel', 'Dud Bolt', 'Gasgano', 'Ben Quadinaros',
                                     'Mace Windu', 'Ki-Adi-Mundi', 'Kit Fisto', 'Eeth Koth', 'Adi Gallia',
                                     'Saesee Tiin', 'Yarael Poof', 'Plo Koon', 'Mas Amedda'])])
    def test_list_people_by_film(self, path, film_index, expected_people):
        allure.dynamic.description('''
        5. Получить список пилотов (peoples) космического корабля из выбранного вами фильма
        ''')
        api = SwapiApi()
        list_url_people = api.get_list_url_people_in_film(f"{path}api/films/{film_index}")
        list_people = []
        for i_url_people in list_url_people[0]:
            list_people.append(api.get_people_name(i_url_people)[0])
        assert list_people == expected_people