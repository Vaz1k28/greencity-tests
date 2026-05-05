
# GreenCity UI Automation Project 🧪

Даний проект присвячений автоматизації тестування користувацького інтерфейсу (UI) платформи **GreenCity**. В основі проекту лежить архітектурний підхід **Page Object Model (POM)** з використанням компонентної моделі для забезпечення гнучкості та підтримки коду.

**Тестуєма сторінка:** [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events)

## 🛠 Технологічний стек
*   **Мова:** Python
*   **Інструмент:** Selenium WebDriver
*   **Фреймворк:** Pytest
*   **Звітність:** Allure Report
*   **Логіка очікувань:** Explicit Waits (WebDriverWait)

---

## 🏗 Архітектура проекту
Проект побудований за принципом розділення відповідальності:

*   **`src/pages/`**: Містить класи сторінок. `BasePage` описує загальні методи, а `EventsPage` — специфічну логіку сторінки подій.
*   **`src/components/`**: Містить класи для незалежних UI-елементів (Header, FilterPanel, EventCard), які наслідуються від `BaseComponent`.
*   **`tests/`**: Набір тест-кейсів, що використовують об'єкти сторінок для перевірки бізнес-логіки.
*   **`conftest.py`**: Конфігурація фікстур (ініціалізація та закриття драйвера).

---

## 📑 Тестове покриття
В рамках проекту автоматизовано наступні сценарії:
1.  **TC-01:** Зміна вигляду відображення (Grid/List).
2.  **TC-02:** Взаємодія з кнопкою "Join event" для неавторизованого користувача.
3.  **TC-03:** Фільтрація подій за діапазоном дат та скидання фільтрів.

---

## 🚀 Налаштування та запуск

### 1. Підготовка середовища
Переконайтеся, що у вас встановлено Python 3.x та [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline).

1.  **Клонуйте репозиторій:**
    ```bash
    git clone [https://github.com/ваше-посилання/greencity-tests.git](https://github.com/ваше-посилання/greencity-tests.git)
    cd greencity-tests
    ```

2.  **Створіть та активуйте віртуальне середовище:**
    ```bash
    python -m venv venv
    # Для Windows:
    venv\Scripts\activate
    # Для macOS/Linux:
    source venv/bin/activate
    ```

3.  **Встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Запуск тестів
Щоб запустити всі тести та зібрати дані для звіту, виконайте:
```bash
pytest --alluredir=allure-results
 ```

###  Автор
Данік Едуард
