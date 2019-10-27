import unittest
from json_class import *
from csv_class import *
import tests_data


class JSONTreatment(unittest.TestCase):
    def test_get_json_with_invalid_url(self):
        result = get_online_json(tests_data.URL_JSON_INVALID)
        self.assertEqual(result, None)

    def test_get_json_with_valid_url(self):
        result = get_online_json(tests_data.URL_JSON_VALID)
        self.assertNotEqual(result, None)

    def test_get_json_local(self):
        result = get_local_json(tests_data.LOCAL_VALID_JSON)
        self.assertNotEqual(result, None)

    def test_get_json_local_invalid(self):
        result = get_local_json(tests_data.LOCAL_INVALID_JSON)
        self.assertEqual(result, None)

    def test_treat_json_valid(self):
        result = treat_json(get_online_json(tests_data.URL_JSON_VALID))
        self.assertListEqual(result, tests_data.LISTA_JSON_FULL)

    def test_treat_json_invalid(self):
        result = treat_json(get_local_json(tests_data.LOCAL_VALID_JSON))
        self.assertNotEqual(result, tests_data.LISTA_JSON_FULL)


class CSVTreatment(unittest.TestCase):
    def test_get_csv_with_invalid_url(self):
        result = import_csv(tests_data.LOCAL_INVALID_CSV)
        self.assertIsNone(result)

    def test_get_csv_with_valid_url(self):
        result = import_csv(tests_data.LOCAL_VALID_PART_CSV)
        self.assertIsNotNone(result)






if __name__ == '__main__':
    unittest.main()
