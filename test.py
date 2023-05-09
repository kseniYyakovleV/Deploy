from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class NewVisitorTest(unittest.TestCase):
    "Тест нового пользователя"

    def setUp(self):
        "setup"
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_test_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")


        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn("To-Do", self.browser.title)
        self.assertIn("To-Do", self.browser.find_element(By.TAG_NAME,"h1").text)


        # Ей сразу же предлагается ввести элемент списка
        

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")



        
        #Она набирает в текстовом поле "Купить павлиньи перья"
        # (ее хобби – вязание рыболовных мушек)
        inputbox.send_keys("Купить павлиные перья")
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == '1' for row in rows))

        # Текствое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        self.fail("Закончить тест")
if __name__ == "__main__":
    unittest.main(warnings="ignore")
    