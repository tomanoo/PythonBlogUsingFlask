from flask import Flask
from bs4 import BeautifulSoup as soup
import requests

# margonem = 'https://new.margonem.pl/'
#
# get_page = requests.get(margonem)
#
# page = soup(get_page.text, "html.parser")
#
# print(page.find_all('div')[3])

appr = Flask(__name__)

@appr.route('/check')
def homer():
    return """
    <h1>ELO</h1>
    <iframe src="https://www.youtube.com/embed/YQHsXMglC9A" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == '__main__':
    appr.run(debug=True, use_reloader=True)