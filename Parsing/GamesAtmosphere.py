import undetected_chromedriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np

class Driver:
    CLASS_NAME = "class name"
    ID = 'id'
    Name = 'name'
    XPATH = "xpath"

    def __init__(self, driver):
        self.__driver = driver

    def get(self, link):
        return self.__driver.get(link)

    def preset(self):
        self.__driver.maximize_window()
        self.__driver.implicitly_wait(1000)

    def find_class_name(self, class_name):
        return self.__driver.find_element(By.CLASS_NAME, class_name)

    def find_id(self, id):
        return self.__driver.find_element(By.ID, id)

    def find_name(self, name):
        return self.__driver.find_element(By.NAME, name)

    def find_xpath(self, xpath):
        return self.__driver.find_element(By.XPATH, xpath)

def set_up(driver):
    input_field = driver.find_xpath(
        '// *[ @ id = "__next"] / div[1] / div[1] / main / div[2] / form / div / div[2] / textarea')
    input_field.send_keys(
        "You are GameAtmosphereDescriptor,an AI who is skilled in emotion and atmosphere description of videogames.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys(
        "Your task is to describe atmosphere of videogame that will be provided to you and to give appropriate plot tags. Also you should recommend books or films in the same atmosphere.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("Silently do the following:")
    input_field.send_keys(
        "1) Start with '/start/Atmosphere:' word. In this section you are describing atmosphere of the game. What was an inspiration of an author of the game if you know. If the game is part of franchise do not mention that the game's inspiration was in the franchise.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("End the section with '/end/Atmosphere'.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys(
        "2) Start with '/start/Tags:' In this section you are describing plot tags of the game. Tags should be separate metadata key words of the games.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("End the section with '/end/Tags'.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys(
        "3)Start with '/start/RecommensationsMovie:' In this section you are giving a movie recommendation as many as possible. Movies should be in the same atmosphere as the game. If you can't give a recommendation type 'None'")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("End the section with '/end/RecommensationsMovie'.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys(
        "4)Start with '/start/RecommensationsBook:' In this section you are giving a book recommendation as many as possible. Books should be in the same atmosphere as the game. If you can't give a recommendation type 'None'")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("End the section with '/end/RecommensationsBook'.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("Restrictions:")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("You can not describe plot of the game.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("You can not mention developers, names, and publishers of the games.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys(
        "If the game is part of a franchise recommendation in each of the category should containe at least 3 titles that is not a part of the franchise.")
    input_field.send_keys(Keys.SHIFT, Keys.ENTER)
    input_field.send_keys("Start when I send you next title of a video game.")
    time.sleep(5)
    input_field = driver.find_xpath(
        '// *[ @ id = "__next"] / div[1] / div[1] / main / div[2] / form / div / div[2] / textarea')  # //*[@id="__next"]/div[1]/div[1]/main/div[2]/form/div/div[2]/textarea
    input_field.send_keys(Keys.ENTER)

def enter_open_ai():
    driver = Driver(undetected_chromedriver.Chrome())
    driver.get(r'https://chat.openai.com/chat')
    driver.preset()
    time.sleep(2)
    log_in = driver.find_class_name('btn.flex.justify-center.gap-2.btn-primary')
    time.sleep(3)
    log_in.click()
    email = driver.find_id('username')
    email.send_keys('mishanet1997@gmail.com')
    continue_button = driver.find_name('action')
    continue_button.click()
    password = driver.find_name('password')
    password.send_keys('Blade007@')
    continue_button = driver.find_name('action')
    continue_button.click()
    time.sleep(1)
    next = driver.find_class_name('btn.flex.justify-center.gap-2.btn-neutral.ml-auto')
    time.sleep(1)
    next.click()
    time.sleep(5)
    next = driver.find_class_name('btn.flex.justify-center.gap-2.btn-neutral.ml-auto')
    time.sleep(1)
    next.click()
    done = driver.find_class_name('btn.flex.justify-center.gap-2.btn-primary.ml-auto')
    done.click()
    time.sleep(5)
    return driver


# def df_cleaning(df):
#     df = df.replace('\r', np.nan)
#     df = df.rename(columns={"GPT_answer\r": "GPT_answer"})
#     return df
# def insert_info():
#     driver = enter_open_ai()
#     set_up(driver)
#     return driver

def df_update():
    driver = enter_open_ai()
    set_up(driver)
    time.sleep(5)
    input_field = driver.find_xpath(
        '// *[ @ id = "__next"] / div[1] / div[1] / main / div[2] / form / div / div[2] / textarea')
    input_field.send_keys(Keys.ENTER)
    df_games = pd.read_csv(r'C:\Users\misha\Pet-project\Parsing\games_dataset.csv', lineterminator='\n')
    df_games['GPT_answer'] = None
    time.sleep(5)
    titles_dict = {}
    row = 0
    NoAnswer = 4
    for i in df_games['title']:
        if i in titles_dict:
            #df_games = df_games.append({'ChatGPT': titles_dict.get(i)}, ignore_index=True)
            df_games.at[row, 'GPT_answer'] = titles_dict.get(i)
            row += 1
        else:
            input_field.send_keys(i)
            time.sleep(1)
            input_field.send_keys(Keys.ENTER)
            time.sleep(60)
            if NoAnswer == 4:
                print(f'//*[@id="__next"]/div[1]/div/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
                chat_gpd_answer = driver.find_xpath(
                    f'//*[@id="__next"]/div[1]/div/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
            else:
                chat_gpd_answer = driver.find_xpath(
                    f'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
            NoAnswer +=2
            print(chat_gpd_answer)
            titles_dict.update({i:chat_gpd_answer.text})
            df_games.at[row, 'GPT_answer'] = chat_gpd_answer.text
            row += 1
        df_games.to_csv(r'C:\Users\misha\Downloads\games_dataset_gpt.csv', index=False)

def continue_parsing():
    driver = enter_open_ai()
    set_up(driver)
    time.sleep(5)
    input_field = driver.find_xpath(
        '// *[ @ id = "__next"] / div[1] / div[1] / main / div[2] / form / div / div[2] / textarea')
    time.sleep(5)
    input_field.send_keys(Keys.ENTER)
    df_games = pd.read_csv(r'C:\Users\misha\Downloads\games_dataset_gpt.csv', lineterminator='\n')
    time.sleep(5)
    row = df_games[df_games.isna().any(axis=1)].first_valid_index()
    titles_dict = dict(zip(df_games.loc[df_games['GPT_answer'] != np.nan]['title'][:row],
                           df_games.loc[df_games['GPT_answer'] != np.nan]['GPT_answer'][:row]))
    NoAnswer = 4
    for i in df_games['title'][row:]:
        if row % 40 == 0 and row != 80:
            set_up(driver)
            time.sleep(5)
            NoAnswer += 2
        if i in titles_dict:
            #df_games = df_games.append({'ChatGPT': titles_dict.get(i)}, ignore_index=True)
            df_games.at[row, 'GPT_answer'] = titles_dict.get(i)
            row += 1
        else:
            input_field.send_keys(i)
            time.sleep(1)
            input_field.send_keys(Keys.ENTER)
            time.sleep(60)
            if NoAnswer == 4:
                print(f'//*[@id="__next"]/div[1]/div/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
                chat_gpd_answer = driver.find_xpath(
                    f'//*[@id="__next"]/div[1]/div/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
            else:
                chat_gpd_answer = driver.find_xpath(
                    f'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[{NoAnswer}]/div/div[2]/div[1]/div/div')
            NoAnswer +=2
            print(chat_gpd_answer)
            titles_dict.update({i:chat_gpd_answer.text})
            df_games.at[row, 'GPT_answer'] = chat_gpd_answer.text
            row += 1
        df_games.to_csv(r'C:\Users\misha\Downloads\games_dataset_gpt.csv', index=False,line_terminator='\n',encoding='utf-8')
continue_parsing()