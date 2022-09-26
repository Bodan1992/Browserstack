import allure
from components import *


@allure.tag('Browserstack mobile')
@allure.title('Search on Wikipedia')
def test_search_in_wikipedia():

    search_in_wikipedia('Selenium (software)')

    verify_content_found()

