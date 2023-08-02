for admin login username and password are fixed to change the username and password you
can change it by creating superuser
username = user         password = P@ss123

To run the project follow the steps
Step 1:
    run a command ---> a :py manage.py makemigrations
                       b :py manage.py migrate


Step 2:
    now create a superuser by command --->  py manage.py createsuperuser

Step 3:
    run a command ---> a :py manage.py runserver
    add path ( admin ) in url 
    and provide username and password which we gave at the time of creating superuser
    now click on Host in django administration and add username and password for login 

Step 4:
    Now run command on terminal --->  py manage.py runserver
    here in Admin login we have to give username and password which we added in django administration
