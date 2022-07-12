import requests
import json
from jsonpath_ng.ext import parse

class SwapiApi:

    def check_list_entity(self, path):
        response = requests.get(path)
        json_data = json.loads(response.text)
        result = list(json_data)
        assert result == ['people', 'planets', 'films', 'species', 'vehicles', 'starships'], "check list entity"


    def check_list_films(self, path):
        parse_result = self._read_json(path, "$.results..title")

        list_films = []
        for element_in_parser in parse_result:
            list_films.append(element_in_parser.value)
        assert list_films == ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace',
                              'Attack of the Clones', 'Revenge of the Sith'], "check list films"

    def check_film_info(self, path,
                        expected_title,
                        expected_director,
                        expected_release_date):
        parse_result = [match.value for match in self._read_json(path, "$.title")]
        assert parse_result == [expected_title], "check title"

        parse_result = [match.value for match in self._read_json(path, "$.director")]
        assert parse_result == [expected_director], "check director"

        parse_result = [match.value for match in self._read_json(path, "$.release_date")]
        assert parse_result == [expected_release_date], "check release_date"

    def check_list_planets(self, path):
        parse_result = self._read_json(path, "$.results..name")
        list_planets = []
        for element_in_parser in parse_result:
            list_planets.append(element_in_parser.value)
        # print(list_planets)
        assert list_planets == ['Tatooine', 'Alderaan', 'Yavin IV', 'Hoth', 'Dagobah', 'Bespin',
                              'Endor', 'Naboo', 'Coruscant', 'Kamino'], "check list planets"


    def get_list_planets_by_film(self, path):
        return [match.value for match in self._read_json(path, "$.planets")]

    def get_planet_name(self, path):
        return [match.value for match in self._read_json(path, "$.name")]

    def get_list_url_species_in_film(self, path):
        return [match.value for match in self._read_json(path, "$.species")]

    def get_list_url_people_in_film(self, path):
        return [match.value for match in self._read_json(path, "$.characters")]

    def get_species_name(self, path):
        return [match.value for match in self._read_json(path, "$.name")]

    def get_people_name(self, path):
        return [match.value for match in self._read_json(path, "$.name")]

    def _read_json(self, path, json_path):
        response = requests.get(path)
        json_data = json.loads(response.text)
        data = parse(json_path)
        return data.find(json_data)