![image](https://github.com/bazonly/calendar/assets/134084102/3ec524ca-9d96-4213-9f25-ba13a0946ab2)запуск приложения
\calendar> flask --app ./server.py run   

для работы необходим Postman

1)создание события
создайте рабочюю среду с адрессом http://127.0.0.1:5000/api/v1/event/ и методом POST 
![image](https://github.com/bazonly/calendar/assets/134084102/f622d0ca-51ae-44b7-bb8c-b493433f26bf)
далее как на скриншоте создайте поля year, month, day, title, text. в эти поля неоходимо вводить интересующие данные. приложение не принимает не корректную дату.
после ввода всех данных нажмите кнопку Send.
при вводе корректных данных появится сообщение "new id: 'новый id'". id имеет примерно такой вид : e_236cc5a1-4c6a-4e0b-9b15-143b1f625207.
на одну дату может быть только одно событие

2)вывод всех событий
создайте рабочюю среду с адрессом http://127.0.0.1:5000/api/v1/event/ и методом GET
![image](https://github.com/bazonly/calendar/assets/134084102/7a1c7870-b34c-43b0-bb1b-1bbe8342b37c)
нажмите кнопку Send.

3)вывод конкретного события
создайте рабочюю среду с адрессом http://127.0.0.1:5000/api/v1/event/"id" и методом GET. Вместо "id" введите id интересующего события
![image](https://github.com/bazonly/calendar/assets/134084102/cb27a067-964f-4949-8211-11b380073d31)
нажмите кнопку Send

4)обновление события
создайте рабочюю среду с адрессом http://127.0.0.1:5000/api/v1/event/"id" и методом PUT. Вместо "id" введите id интересующего события
![image](https://github.com/bazonly/calendar/assets/134084102/7707858a-7649-4b16-9b8d-8b3731384322)
далее как на скриншоте создайте поля year, month, day, title, text. в эти поля неоходимо вводить интересующие данные. приложение не принимает не корректную дату.
после ввода всех данных нажмите кнопку Send.
при вводе корректных данных появится сообщение "updated".
если вы не поменяли дату и не поменяли описание события, то изменения не будут сохранены
при изменении даты и описания будет проверка, занята ли новая дата каким-либо событием
при изменении только описания изменения сразу будут внесены
при изменении даты  будет проверка, занята ли новая дата каким-либо событием

5)удаление события
создайте рабочюю среду с адрессом http://127.0.0.1:5000/api/v1/event/"id" и методом DELETE. Вместо "id" введите id интересующего события
![Uploading image.png…]()
нажмите кнопку Send
