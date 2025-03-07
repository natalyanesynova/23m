# Проект 23.2.1 (HW)
## Задача - построить парсер, принимающий уникальный идентификатор рецензента сервиса livelib.ru, возвращающий информацию об оценках книг этим рецензентом. 
Также реализована возможность сохранения результатов парсинга в таблицу excel

## Обоснование.
LiveLib - сервис, который подбирает книги, ориентируясь на предпочтения пользователя. Рецензии могут оставлять и читатели, и книжные клубы.
Помимо этого сервиса есть еще несколько похожих: Goodreads (крупнейшая в мире книжная соцсеть, где есть и русскоязычное сообщество), Книгогид и др.
Данный парсер нужен для построения рекомендательных систем, так как можно горизонтально расширить его: распарсить всех пользователей всех таких сервисов. Это позволит в перспективе построить улучшенную версию рекомендательной системы книг, которая будет основываться не только на основе понравившихся самому читателю книг, но и на оценках множества других пользователей разных сервисов с оценками книг. Можно также добавить "уровни" рецензентов, чтобы можно было выбирать рекомендации "профессионалов" или "любителей", например.

## Инструкция по сборке и запуску кода
1. Поместить код (файл 23.2.1.HW.py) в интерпретатор PyCharm
2. Установить необходимые библиотеки (в терминале PyCharm командой pip install): requests; beautifulsoup4; lxml; pandas; openpyxl
3. Выбрать конкретного рецензента на сайте livelib.ru
   > Сделать это можно следующим образом:
   >  - открыть любую книгу на главной странице livelib.ru,
   >  - пролистать страницу вниз до пункта "Рецензии",
   >  - нажать на автора рецензии,
   >  - на открывшейся странице рецензента нажать на вкладку "Рецензии".
5. Вставить никнейм резенцента в кавычках (можно из адресной строки, со страницы рецензента, из пункта "Рецензии выбранной книги") в 39 строку кода на место "user_login" (вот искомая строка: user_rates = collect_user_rates(user_login))
6. Результат парсинга будет сохранен в текущей папке в формате excel

## Пример работы парсера прикреплен в виде таблицы excel, использован никнейм "Lika_Veresk"


