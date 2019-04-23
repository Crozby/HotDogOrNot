#Hot dog or not
Сайт для распознования хотдогов.
Сайт принимает ссылку на jpg картинку и выдаёт предсказание, 
есть ли на картинке хотдог или нет.
![23](https://puu.sh/DikGG/544fe01f51.gif)
###Стек технологий
Для предсказаний используется нейросеть (resnet18). 
Сайт реализован с использованием
* html
* css
* js
* python (Flask)
###Развёртывание
Необходимо установить [python 3.6.5 x86-64](https://www.python.org/downloads/release/python-365/)
и pip.  


Клонировать репозиторий  
`git clone https://github.com/Crozby/HotdogOrNot.git`     


Установить зависимости, выполнив в корне проекта    
`pip3 install -r requirements.txt`         


Выполнить   
`python -m flask run`  
для запуска сервера.