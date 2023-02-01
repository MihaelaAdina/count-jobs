import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookiescript_accept")))

        accept_cookies = driver.find_element(By.ID, 'cookiescript_accept')
        time.sleep(5)
        accept_cookies.click()

        department_dropdown = driver.find_element(By.XPATH, '//*[@id="sl"]')
        department_dropdown.click()

        select_department = driver.find_element(By.XPATH, "//a[text()='Research & Development']")
        select_department.click()

        language_dropdown = driver.find_element(By.XPATH, "//button[text()='All languages']")
        language_dropdown.click()

        select_language = driver.find_element(By.XPATH, "//label[text()='English']")
        select_language.click()
        time.sleep(5)

        count_job_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/div/a")
        print(len(count_job_list))

        actual_count = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/h3/span')
        print(actual_count.text)
        self.assertNotEqual(count_job_list, actual_count)

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()







