# test_software_center
<h1> Установка и запуск </h1>
<p>Создайте виртуальную среду</p>
<code> python -m venv env </code>
<p>Активируйте виртуальную среду</p>
<code> .\env\Scripts\activate </code>
<p> Клонируйте репозиторий </p>
<code> git clone https://github.com/cyberkitaec/test_software_center.git</code>
<p> Установка зависимостей</p>
<code>pip install -r requirements.txt</code>
<p> Запуск проекта</p>
<code>cd software_center</code>
<code>python manage.py runserver</code>
<p></p>
<h2> Импорт postman коллекции</h2>
<p> Коллекция представленая файликом .json в репозитории</p>
<p> Для импорта коллекции необходимо кликнуть по import</p>
![Screenshot_3](https://github.com/cyberkitaec/test_software_center/assets/87614770/cfe691df-4710-46c7-afa7-31aba3c34332)
<p> Затем в появившееся окно перетащить .json файл</p>


<h1>Стэк</h1>
<ul>
  <li> Python 3.9.13</li>
  <li> Django 4.2</li>
  <li> DRF<ul> <li> PyJWT (JSON Web Token) </li> </ul></li>
  <li> JQuery</li>
</ul>

<h1>Немного о важном</h1>
<p> Перед началом работы с API пользователю будет необходимо <strong>зарегестрироваться, т.к. в проекте используется аунтефикация по JWT </strong>.</p>
<code> Регистрация доступна по: /api/v1/registration</code>
<p> Далее, после регистрации, необходимо получить access токен <code>/api/v1/login</code></p>
<p> После чего, во время обращения к API приложения надо не забыть указать в headers: <code>Authorization: key</code> и не забыть указать ключевое слово <strong>Bearer</strong> перед key</p>
<h2>Теперь о веб...</h2>
<p>Шаблон index`a сделан по примеру, но <s> далек от идела</s>, хотя визиуально схожи.</p>
