import os
import colorama
import operator
from tkinter import N
from xdrlib import Error
from colorama import Fore
from colorama import Back
from colorama import Style
from time import sleep
from mailbox import NoSuchMailboxError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from prettytable import PrettyTable

myTable = PrettyTable(["Markė", "Modelis", "Kaina", "Metai", "Variklis", "Kuro tipas",
                      "Kėbulo tipas", "Pavarų dežė", "Rida", "Defektai", "Vairo padėtis", "URL adresas"])


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Vehicle(object):
    def __init__(self, brand=None, model=None, year=None, engine=None, fuel_type=None, body_type=None, gearbox=None, mileage=None, defects=None, wheel_position=None, price=None, url=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.engine = engine
        self.fuel_type = fuel_type
        self.body_type = body_type
        self.gearbox = gearbox
        self.mileage = mileage
        self.defects = defects
        self.wheel_position = wheel_position
        self.url = url

    def __repr__(self):
        return f"Object: {Fore.YELLOW} {self.brand} {self.model} {Fore.RED} {self.price} {Fore.WHITE} {self.year} {self.engine} {self.fuel_type} {self.mileage} {self.url}"


clear_console()
staring_url = input('Paste your URL address: ')

colorama.init(autoreset=True)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--window-size=1200,1200")

os.environ['PATH'] += r"C:/drivers"
driver = webdriver.Chrome(options=options)

driver.get(staring_url)
driver.implicitly_wait(2)
action = webdriver.ActionChains(driver)

car_object_list = []

try:
    clear_console()
    print(f"{Fore.GREEN}Opening chrome browser...")
    sleep(1)

    cookieAccept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookieAccept.click()

    car_articles = driver.find_elements(
        By.XPATH, "//a[@onclick='showWatchedBadge(this);'][@class='item-link ']")

    print(f"{Fore.GREEN}STARTED: getting data from - {Fore.BLUE} {staring_url}")
    i = 0
    for articles in car_articles:
        i += 1
        print(f"{Fore.GREEN}GATHERING: getting information from object number " +
              str(i) + "...", end="\r")
        action.move_to_element(articles).click().perform()
        driver.switch_to.window(driver.window_handles[1])
        try:
            new_car_object = Vehicle()
            car_price = driver.find_element(By.CSS_SELECTOR, "div.price")
            new_car_object.price = car_price.text.replace(" ", "")

            try:
                car_brand = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Markė')]/following-sibling::div")
                new_car_object.brand = car_brand.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Markė'. Value is set to 'None' by default")

            try:
                car_model = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Modelis')]/following-sibling::div")
                new_car_object.model = car_model.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Modelis'. Value is set to 'None' by default")

            try:
                car_year = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Metai')]/following-sibling::div")
                new_car_object.year = car_year.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Metai'. Value is set to 'None' by default")

            try:
                car_engine = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Variklis')]/following-sibling::div")
                new_car_object.engine = car_engine.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Variklis'. Value is set to 'None' by default")

            try:
                car_fuel_type = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Kuro tipas')]/following-sibling::div")
                new_car_object.fuel_type = car_fuel_type.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Kuro tipas'. Value is set to 'None' by default")

            try:
                car_body_type = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Kėbulo tipas')]/following-sibling::div")
                new_car_object.body_type = car_body_type.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Kėbulo tipas'. Value is set to 'None' by default")

            try:
                car_gearbox = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Pavarų dėžė')]/following-sibling::div")
                new_car_object.gearbox = car_gearbox.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Pavarų dėžė'. Value is set to 'None' by default")

            try:
                car_mileage = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Rida')]/following-sibling::div")
                new_car_object.mileage = car_mileage.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Rida'. Value is set to 'None' by default")

            try:
                car_defects = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Defektai')]/following-sibling::div")
                new_car_object.defects = car_defects.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Defektai'. Value is set to 'None' by default")

            try:
                car_wheel_position = driver.find_element(
                    By.XPATH, f"//div[contains(text(),'Vairo padėtis')]/following-sibling::div")
                new_car_object.wheel_position = car_wheel_position.text
            except NoSuchElementException:
                print(
                    f"{Fore.LIGHTYELLOW_EX}ATTENTION: object {i} does not contain 'Vairo padėtis'. Value is set to 'None' by default")

            car_url = driver.current_url
            new_car_object.url = car_url

            car_object_list.append(new_car_object)

        except NoSuchElementException:
            print(f"{Fore.RED}ERROR: No such element!")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    print(f"{Fore.GREEN}SUCCESFUL: collected information about objects. Collected data about " +
          str(i) + " objects.", end="\n")
    print(f"{Fore.GREEN}All information about collected data: ")
    for car in car_object_list:
        brand = vars(car).get("brand")
        model = vars(car).get("model")
        price = vars(car).get("price")
        year = vars(car).get("year")
        engine = vars(car).get("engine")
        fuel_type = vars(car).get("fuel_type")
        body_type = vars(car).get("body_type")
        gearbox = vars(car).get("gearbox")
        mileage = vars(car).get("mileage")
        defects = vars(car).get("defects")
        wheel_position = vars(car).get("wheel_position")
        url = vars(car).get("url")
        myTable.add_row([brand, model, price, year, engine, fuel_type,
                        body_type, gearbox, mileage, defects, wheel_position, url])
    print(myTable.get_string(sort_key=operator.itemgetter(1, 0), sortby="Kaina"))
    driver.quit()
except NoSuchElementException:
    print(f"{Fore.RED}ERROR: No such element!")
