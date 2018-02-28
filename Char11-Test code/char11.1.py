def get_country_name(city, country, population=''):
    if population:
        full_name = city + "," + country + " - " + population
        return full_name.title()
    else:
        full_name = city + "," + country
        return full_name.title()


import unittest


class CountryNameTestCase(unittest.TestCase):

    def test_name(self):
        country_name = get_country_name('guangzhou', 'china', '500')
        self.assertEqual(country_name, 'Guangzhou,China - 500')


unittest.main()