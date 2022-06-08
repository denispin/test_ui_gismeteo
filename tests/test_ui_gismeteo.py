import allure


@allure.epic('Тестовое задание UI')
@allure.title('Проверка популярного города')
def test_popular_cities(app, asserts):
    app.session.open_home_page()
    with allure.step("Проверяю, что предпоследний город в списке популярных городов - Владивосток"):
        with allure.step(f"Получаю список популярных городов"):
            asserts.accumulate(app.start_page.get_popular_cities_list()[-2] == "Владивосток",
                               f"Список популярних городов - {app.start_page.get_popular_cities_list()}, "
                               f"предпоследний город - {app.start_page.get_popular_cities_list()[-2]}")
            app.get_screenshot()
            asserts.release()


@allure.epic('Тестовое задание UI')
@allure.title('Проверка поиска')
def test_search(app, asserts):
    city_name = 'Волгоград'
    app.session.open_home_page()
    with allure.step(f'В строку поиска ввожу название города - {city_name}'):
        app.start_page.city_search(city_name)
    with allure.step('Проверяю, что  отображается погода для указанного города'):
        asserts.accumulate(app.start_page.get_page_title() == f'Погода в {city_name}е сегодня',
                           f"Ожидаю - Погода в {city_name}е сегодня - получил - {app.start_page.get_page_title()}")
    app.get_screenshot()
    asserts.release()


@allure.epic('Тестовое задание UI')
@allure.title(' Переход на страницу погодного приложения для телевизоров')
def test_tv_site(app, asserts):
    app.session.open_home_page()
    with allure.step('Открываю станицу приложений'):
        app.start_page.open_soft_page()
    with allure.step('Открываю станицу Погода для телевизоров'):
        app.start_page.open_soft_tv_page()
    waiting_text = app.start_page.get_soft_header_text().split('\n')[0]
    asserts.accumulate(waiting_text == 'Погода для телевизоров',
                       f"Ожидаю - 'Погода для телевизоров' - получил - {waiting_text}")
    app.get_screenshot()
    asserts.release()


@allure.epic('Тестовое задание UI')
@allure.title('Проверка погоды на 10 дней')
def test_10_days(app, asserts):
    app.session.open_home_page()
    city_id, city_code = app.start_page.get_city_link()
    with allure.step(f'Получаю название текущего города'):
        app.start_page.open_10days_weather(city_code)

    with allure.step('Перехожу на страницу Погода на 10 дней для текущего города'):
        asserts.accumulate(app.start_page.get_page_url() == city_id + '10-days/',
                           f'Ожидаю - {city_id + "10-days/"}, получил - {app.start_page.get_page_url()}')
    with allure.step('Проверяю, соответствие интервала отображаемым датам'):
        asserts.accumulate(app.count.count_of_days() == 10,
                           f'Ожидаю - 10, получил - {app.count.count_of_days()}')
    app.get_screenshot()
    asserts.release()
