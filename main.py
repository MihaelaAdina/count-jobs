import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class CountJobs(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1370, 900)

    # Test case method. It should always start with test_
    def test_count_jobs(self):
        # get driver
        driver = self.driver
        driver.get("https://cz.careers.veeam.com/vacancies")
        department = driver.find_element(By.XPATH, '//*[@id="sl"]')
        department.click()
        time.sleep(5)

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()







