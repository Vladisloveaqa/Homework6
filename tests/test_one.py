from datetime import time
from pprint import pprint


def test_dark_theme_by_time():
    start=22
    end=6
    current_time=time(hour=23)
    is_dark_theme=False
    if current_time.hour >= start or current_time.hour <= end:
      is_dark_theme=True
      print('is_dark_theme=black')
    current_time = time(hour=23)
    assert is_dark_theme is True

from datetime import time

def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = None
    is_dark_theme = None

    if dark_theme_enabled_by_user is True:
        print('Пользователь включил темную тему')
        is_dark_theme = True

    elif dark_theme_enabled_by_user is False:
        print('Пользователь включил светлую тему')
        is_dark_theme = False

    else:
        print('Включена автоматически темная тема по времени')
        is_dark_theme = True

    assert is_dark_theme is True

def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suitable_users = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user
            break
    assert suitable_users == {"name": "Olga", "age": 45}


    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

def print_readable(func, *args, **kwargs):
    name = func.__name__.replace('_', ' ').title()
    values = list(args) + [f"{v}" for v in kwargs.values()]
    result = f"{name} [{', '.join(values)}]"
    print(result)
    return result


def test_readable_function():
    assert open_browser(browser_name="Chrome") == "Open Browser [Chrome]"
    assert go_to_companyname_homepage(page_url="https://companyname.com") == \
           "Go To Companyname Homepage [https://companyname.com]"
    assert find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register") == \
           "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def open_browser(browser_name):
    actual_result = print_readable(open_browser, browser_name)
    return actual_result


def go_to_companyname_homepage(page_url):
    actual_result = print_readable(go_to_companyname_homepage, page_url)
    return actual_result


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_readable(find_registration_button_on_login_page, page_url, button_text)
    return actual_result










