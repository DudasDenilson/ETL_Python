import unittest
from json_class import *
from json_csv_class import *
from csv_class import *
import tests_data


class JSONTreatment(unittest.TestCase):
    def test_get_json_with_invalid_url(self):
        result = get_online_json(tests_data.URL_JSON_INVALID)
        self.assertIsNone(result)

    def test_get_json_with_valid_url(self):
        result = get_online_json(tests_data.URL_JSON_VALID)
        self.assertIsNotNone(result)

    def test_get_json_local(self):
        result = get_local_json(tests_data.LOCAL_VALID_JSON)
        self.assertIsNotNone(result)

    def test_get_json_local_invalid(self):
        result = get_local_json(tests_data.LOCAL_INVALID_JSON)
        self.assertIsNone(result)

    def test_treat_json_valid(self):
        empty_list = []
        result = treat_json(get_online_json(tests_data.URL_JSON_VALID))
        self.assertListEqual(result, tests_data.LISTA_JSON_FULL) or self.assertNotEqual(result, empty_list)

    def test_treat_json_invalid(self):
        empty_list = []
        result = treat_json(get_local_json(tests_data.LOCAL_INVALID_JSON))
        self.assertEqual(result, empty_list)


class CSVTreatment(unittest.TestCase):
    def test_get_csv_with_invalid_url(self):
        result = import_csv(tests_data.LOCAL_INVALID_CSV)
        self.assertIsNone(result)

    def test_get_csv_with_valid_url(self):
        result = import_csv(tests_data.LOCAL_VALID_PART_CSV)
        self.assertIsNotNone(result)

    def test_treat_url_with_valid_url(self):
        result = treat_url_google_drive_file(tests_data.URL_VALID_GOOGLE_DRIVE)
        self.assertIsNotNone(result)

    def test_treat_data_with_valid_csv(self):
        empty_list = []
        result = data_treatment(import_csv(treat_url_google_drive_file(tests_data.URL_VALID_GOOGLE_DRIVE)))
        self.assertNotEqual(result, empty_list)

    def test_write_csv_with_valid_local(self):
        result = write_csv(data_treatment(import_csv(tests_data.LOCAL_VALID_FULL_CSV)),
                           tests_data.LOCAL_DESTINO_CSV_VALID)
        self.assertTrue(result)

    def test_write_csv_with_invalid_local(self):
        result = write_csv(data_treatment(import_csv(tests_data.LOCAL_VALID_FULL_CSV)),
                           tests_data.LOCAL_DESTINO_CSV_INVALID)
        self.assertNotEqual(result, True)


class StageTreatment(unittest.TestCase):
    def test_treat_stage_with_valid_data(self):
        empty_list = []
        result = gera_csv_stage(treat_json(get_online_json(tests_data.URL_JSON_VALID)),
                                data_treatment(import_csv(tests_data.LOCAL_VALID_FULL_CSV)))
        self.assertNotEqual(result, empty_list)


if __name__ == '__main__':
    unittest.main()
