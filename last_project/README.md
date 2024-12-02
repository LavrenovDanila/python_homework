### Описание итоговой работы
Проект: Веб-приложение для управления финансовым учетом
Описание проекта
Веб-приложение для управления персональными финансами позволяет пользователям отслеживать свои расходы и доходы, создавать бюджеты и анализировать финансовые данные. Приложение включает в себя функции для добавления транзакций, разделения расходов по категориям, генерации отчетов, а также возможность устанавливать финансовые цели. С помощью этого приложения пользователи могут лучше понимать свои финансовые привычки и принимать обоснованные решения.


Запуск
Установить python
Клонировать репозиторий проекта
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin/