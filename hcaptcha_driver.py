from lib2to3.pgen2 import driver
import shutil
import numpy as np
import tensorflow as tf
import os
import requests
import time
from undetected_chromedriver import Chrome as uc
from undetected_chromedriver.options import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow import keras
from os.path import join,dirname, isdir

class HCaptchaDriver:

      __class_names = ('airplane','airplane in the sky flying left','bicycle','boat','bus','motorbus','motorcycle','seaplane','train','truck','vertical river')
      __root_dir = dirname(__file__)
      __model = keras.models.load_model(join(__root_dir,'model'))
      def __init__(self, driver: uc, timeout:int = 30):
          self._driver = driver
          self._wait = WebDriverWait(driver=driver,timeout=timeout)
          self._timeout = timeout
          self._current_windows = driver.current_window_handle
          if not isdir(join(self.__root_dir,'database')):
                os.makedirs(join(self.__root_dir,'database'))
      
      def _handle_checkbox(self) -> bool:
            try:
                  self._driver.switch_to.frame(self._wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//iframe[contains(@title,"checkbox for hCaptcha")]'))))
                  if self._driver.find_element(By.ID,'anchor').get_attribute('aria-hidden') != 'true':
                        self._driver.find_element(By.ID,'anchor').click()
                  self._driver.switch_to.window(self._current_windows)
                  return True
            except TimeoutException:
                  self._driver.switch_to.window(self._current_windows)
                  return False

      def _no_captcha(self) -> bool:

            self._driver.switch_to.frame(self._driver.find_element(By.XPATH,'//iframe[contains(@title,"checkbox for hCaptcha")]'))
            if self._driver.find_element(By.ID,'checkbox').get_attribute('aria-checked') == 'true':
                  return True
            self._driver.switch_to.window(self._current_windows)
            return False
      
      def _download_challenge_images(self) -> str:
            folder_name = str(time.time()).split('.')[0]
            if not isdir(join(self.__root_dir,f'database\\{folder_name}')):
                os.makedirs(join(self.__root_dir,f'database\\{folder_name}'))
            elements = self._driver.find_elements(By.CLASS_NAME,'task-image')
            for element in elements:
                  task_image = element.find_element(By.CLASS_NAME,'image')
                  src_image = task_image.get_attribute('style').split('url("')[-1].split('")')[0]
                  content_image = requests.get(url=src_image).content
                  with open(join(self.__root_dir,f'database\\{folder_name}\\{element.get_attribute("aria-label")}.jpg'),'wb') as file:
                        file.write(content_image)
            return folder_name

      def _submit(self) -> bool:
            try:
                  self._driver.find_element(By.XPATH,'//div[@title="Submit Answers"]').click()
                  return True
            except:
                  return False
      
      def _next(self) -> bool:
            try:
                  self._driver.find_element(By.XPATH,'//div[@title="Next Challenge"]').click()
                  return True
            except:
                  return False
      
      def _check(self) -> bool:
            try:
                  self._driver.switch_to.window(self._current_windows)
                  if not self._driver.find_element(By.XPATH,'//iframe[contains(@title,"content of the hCaptcha")]').is_displayed():
                        self._driver.switch_to.frame(self._driver.find_element(By.XPATH,'//iframe[contains(@title,"content of the hCaptcha")]'))
                        return True
                  self._driver.switch_to.frame(self._driver.find_element(By.XPATH,'//iframe[contains(@title,"content of the hCaptcha")]'))
                  return False
            except NoSuchElementException:
                  try:
                        self._driver.switch_to.frame(self._driver.find_element(By.XPATH,'//iframe[contains(@title,"content of the hCaptcha")]'))
                  except:
                        pass
                  return True

      def solution(self) -> bool:

            if not self._handle_checkbox():
                  return False

            if self._no_captcha():
                  return True

            self._driver.switch_to.frame(self._wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//iframe[contains(@title,"content of the hCaptcha")]'))))
            self._wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//div[@class="image" and contains(@style,"background: url")]')))
            time.sleep(1)
            question = str(self._driver.find_element(By.CLASS_NAME,'prompt-text').text)
            if 'аirplane' in question:
                  question = question.split('аirplane')[0] + 'train'
            if 'mοtorbus' in question:
                  question = question.split('mοtorbus')[0] + 'train'
            if 'trаin' in question:
                  question = question.split('trаin')[0] + 'train'
            if 'bіcycle' in question:
                  question = question.split('bіcycle')[0] + 'bicycle'
            if 'ѕeaplane' in question:
                  question = question.split('ѕeaplane')[0] + 'seaplane'
            if 'mοtorcycle' in question:
                  question = question.split('mοtorcycle')[0] + 'motorcycle'
            if 'bοat' in question:
                  question = question.split('bοat')[0] + 'boat'
            if 'truсk' in question:
                  question = question.split('truсk')[0] + 'truck'
            print(question)
            for _ in range(2):
                  self._wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//div[@class="image" and contains(@style,"background: url")]')))
                  while True:
                        try:
                              folder_name = self._download_challenge_images()
                              if folder_name:
                                    break
                        except:
                              pass
                  data_dir = os.listdir(join(self.__root_dir,f'database\\{folder_name}'))
                  results = []
                  for j in range(len(data_dir)):
                        img = keras.preprocessing.image.load_img(join(self.__root_dir,f'database\\{folder_name}\\{data_dir[j]}'),target_size=(128,128))
                        img_array = keras.preprocessing.image.img_to_array(img)
                        img_array = tf.expand_dims(img_array, 0)
                        predictions = self.__model.predict(img_array)
                        score = tf.nn.softmax(predictions[0])
                        result = self.__class_names[np.argmax(score)]
                        if result in question and 100*np.max(score) > 98:
                              results.append(data_dir[j].replace('.jpg',''))

                  for k in range(len(results)):
                        while True:
                              try:
                                    ele = self._driver.find_element(By.XPATH,f'//div[@aria-label="{results[k]}"]')
                                    break
                              except:
                                    pass
                        if ele.get_attribute('aria-pressed') != 'true':
                              ele.click()
                  while True:
                        try:
                              shutil.rmtree(path=join(self.__root_dir,f'database\\{folder_name}'))
                              break
                        except:
                              pass
                  if self._next():
                        continue
                  self._submit()
            time.sleep(2)
            is_done = self._check()
            if not is_done:
                  self._driver.find_element(By.XPATH,'//div[@title="Refresh Challenge."]').click()

            self._driver.switch_to.window(self._current_windows)
            return is_done
