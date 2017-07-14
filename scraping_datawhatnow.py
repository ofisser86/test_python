import requests
from lxml import html

url = 'https://www.datawhatnow.com'


def get_parsed_page(url):
    """Return the content of the website on the given url in
    a parsed lxml format that is easy to query."""

    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page


parsed_page = get_parsed_page(url)
# Print the website's title
x = parsed_page.xpath('//h2/a/text()')  # ['Data, what now?']
print x
print(type(1 / 2))