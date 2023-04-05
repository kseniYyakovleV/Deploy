from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    "Тест нового пользователя"

    def setUp(self):
        "setup"
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_test_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)
        self.fail("Закончить тест")

if __name__ == "__main__":
    unittest.main(warnings="ignore")
    