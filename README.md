- sudo apt-get update
- git clone https://github.com/AbhiiVops/CVs-info-Extractor.git
- cd CVs-info-Extractor/
- sudo apt install python3-pip -y
- pip install django
- python3 manage.py makemigrations
- git pull origin master
- pip install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser
- python3 manage.py runserver 0.0.0.0:8000
- la
- clear
- ls
- cd cv_extractor/
- ls
- vim settings.py 
- python3 manage.py runserver 0.0.0.0:8000
- cd ..
- python3 manage.py runserver 0.0.0.0:8000
- cd cv_extractor/
- ls
- vim settings.py 
- cd ..
- python3 manage.py runserver 0.0.0.0:8000
- *nohup python3 manage.py runserver 0.0.0.0:8000 &*
