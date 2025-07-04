from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert 'tea' in actual_text, f"Error. expected_text 'tea' not in {actual_text}"