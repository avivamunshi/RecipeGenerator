"""
A unittest module for collecting weblinks
and writing them into a csv.
"""
import os
import sys
import unittest
from pathlib import Path
import requests

from collect import obtain_links #pylint: disable=import-error
from collect import link_store_file #pylint: disable=import-error

os.chdir("../")
sys.path.append(f"{os.getcwd()}/Code/")

class TestCollect(unittest.TestCase):
    """
    Unittest class for the recipe collect module
    testing two functions
    Obtain_links:
    The function collects a set of web links from a web site.
    The function takes url_baselink, a string url web link,
    as a parameter.
    The function returns a set of strings, that are url links.

    Link_store_file:
    The function writes a set of stings in a csv file.
    The function takes a set of strings,set_links, as a
    parameter.
    The function returns none and is void since the process
    is writing a file in your file system.

    """

    # Smoke test
    def test_obtain_links_smoke(self):
        """
        test smoke that asserts the function
        obtain links function is executing.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        obtain_links(url)
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(True)

    # One-shot test
    def test_obtain_links_return(self):
        """
        a onseshot test that asserts the function
        obtain links function is executing results
        as a set.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        self.assertIsInstance(result, set)

    def test_obtain_links_size(self):
        """
        a test that asserts the function
        obtain links function is executing results
        as a set that contains at least an element
        in a set.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        self.assertGreater(len(result), 0)

    # Pattern test
    def test_obtain_links_set_elements(self):
        """
        test that checks the patteren in obtain links
        function every elementis a string
        """
        # Test that each element in the set is a string
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        for element in result:
            self.assertIsInstance(element, str)

    # Edge cases test each recipe link is a valid url link
    def test_obtain_links_url_validity_epi(self):
        """
        test that the every string in the set is
        a vaild url link
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        for element in result:
            response = requests.get(element, timeout=5)
            self.assertEqual(response.status_code, 200)

    def test_link_store_file_smoke(self):
        """
        test smoke that asserts the function
        link store file function is executing.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        link_store_file(result)
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(True)

    def test_link_store_file_writable(self):
        """
        test that edge case checks links store
        file function has permission to write the
        csv file into the path system.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        link_store_file(result)
        filename = "web_links.csv"
        self.assertTrue(os.access(filename, os.W_OK))

    def test_link_store_file_readable(self):
        """
        test that edge case checks links store
        file function has permission to read the
        csv file into the path system.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        link_store_file(result)
        filename = "web_links.csv"
        self.assertTrue(os.access(filename, os.R_OK))

    def test_link_store_file_exists(self):
        """
        test that edge case checks links store
        file function that the csv file exists.
        """
        url = ('https://www.epicurious.com/'
        'search/?content=recipe&search=recipe&page=')
        result = obtain_links(url)
        link_store_file(result)
        file_path = Path('./web_links.csv')
        self.assertTrue(file_path.is_file())

if __name__ == '__main__':
    unittest.main()
