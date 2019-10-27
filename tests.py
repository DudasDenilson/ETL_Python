import unittest
from json_class import *
from csv_class import *
import tests_data


class JSONTreatment(unittest.TestCase):
    def test_get_json_with_invalid_url(self):
        url = tests_data.URL_JSON_INVALID
        result = get_online_json(url)

        self.assertEqual(result, None)

    def test_get_json_with_valid_url(self):
        url = tests_data.URL_JSON_VALID
        result = get_online_json(url)

        self.assertNotEqual(result, None)

    def test_get_json_local(self):
        url = tests_data.LOCAL_VALID_JSON
        result = get_local_json(url)

        self.assertNotEqual(result, None)

    def test_get_json_local_invalid(self):
        url = tests_data.LOCAL_INVALID_JSON
        result = get_local_json(url)

        self.assertEqual(result, None)

    def test_treat_json_valid(self):
        list_json = tests_data.LISTA_JSON_FULL

        url = tests_data.URL_JSON_VALID
        result = treat_json(get_online_json(url))

        self.assertListEqual(result, list_json)

    def test_treat_json_invalid(self):
        list_json = tests_data.LISTA_JSON_FULL
        url = tests_data.LOCAL_VALID_JSON
        result = treat_json(get_local_json(url))

        self.assertNotEqual(result, list_json)


class CSVTreatment(unittest.TestCase):
    def test_get_csv_with_invalid_url(self):
        data = None
        local = tests_data.LOCAL_INVALID_CSV
        result = import_csv(local)

        self.assertIsNone(result, data)

    def test_get_csv_with_valid_url(self):
        data = None
        local = tests_data.LOCAL_VALID_PART_CSV
        result = import_csv(local)

        self.assertIsNotNone(result, data)






if __name__ == '__main__':
    unittest.main()
