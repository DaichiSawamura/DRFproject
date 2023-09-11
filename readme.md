устанавливаем виртуальное окружение python3 -m venv venv
включаем виртуальное окружение source venv/bin/activate
устанавливаем нужные для проекта библиотеки из файла pip install -r requirements.txt
отправляем данные в БД python manage.py migrate
запускаем сервер python manage.py runserver
запускаем  Docker docker-compose up -d --build
