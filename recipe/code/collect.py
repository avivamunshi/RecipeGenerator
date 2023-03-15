"""
A set of functions that search through a url search page and
collects recipe links written into a csv file.
"""
from bs4 import BeautifulSoup as bs
import requests


def obtain_links(url_baselink):
    """
    The function collects a set of web links from a web site.
    The function takes url_baselink, a string url web link,
    as a parameter.
    The function returns a set of strings, that are url links.

    Raise Exception errors:
    Raises a value error if the parameter given is
    not a string data type.
    Raises a value error if the return value
    is not contained inside as a set.
    """
    bon_base_site = "https://www.bonappetit.com"
    epi_base_site = "https://www.epicurious.com"
    bon_site = "https://www.bonappetit.com/recipe/"
    header = {
    'User-Agent':('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/110.0.0.0 Safari/537.36')}

    with requests.Session() as session:
        req = session.get(url_baselink, headers=header)
    soup = bs(req.text, 'lxml')
    web_links = set()
    for item in soup.find_all("article",
        attrs={"class": "recipe-content-card"}):
        for link in item.find_all('a', href=True):
            url = link['href']
            if url not in link:
                if bon_base_site in url_baselink and bon_site in url:
                    web_links.add(url)
                elif bon_base_site in url_baselink and\
                    not 'htt' in url:
                    web_links.add(bon_base_site+url)
                else:
                    if epi_base_site in url_baselink:
                        web_links.add(epi_base_site+url)

    return web_links

# def link_store_file(set_links):
#     """
#     The function writes a set of strings in a csv file.
#     The function takes a set of strings,set_links, as a
#     parameter.
#     The function returns none and is void since the process
#     is writing a file in your file system.

#     Raise Exception errors:
#     Raises a value error if the parameter
#     set links is not a set.
#     """

#     path = Path('./code/web_links.csv')
#     mode = 'a' if path.is_file() else 'w'
#     with open('web_links.csv', mode, newline='', encoding="utf8") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows([[link] for link in set_links])

#     if path.is_file() is not True:
#         raise ValueError("File was not created into"
#         "the directory")

def main():
    """
    Main functon call the two functions from:

    obtain_links a function that takes a string
    that reperesents a link search page
    as a parameter and returns a set of
    web link recipe strings.

    The function link_store_file is called, which
    takes a set of string web links as a parameter
    and writes them into a csv file.
    """
    base_epicurious_search_page = ('https://www.epicurious.com/'
    'search/?content=recipe&search=recipe&page=')
    base_bon_search_page = ('https://www.bonappetit.com/'
    'search/recipe?content=recipe&q=recipe&page=')
    set_page_link = set()

    for page_num in range(1, 10):
        epi_search_page = base_epicurious_search_page + str(page_num)
        set_page_link.update(obtain_links(epi_search_page))

    for page_num in range (1, 10):
        bon_search_page = base_bon_search_page + str(page_num)
        set_page_link.update(obtain_links(bon_search_page))

    # link_store_file(set_page_link)

if __name__ == '__main__':
    main()
