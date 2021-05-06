# Test for developer (Django)

This repository contains the code for this test for a Python developer.
Objective: to design and develop an API for a user polling system.

## Getting Started

- [ ] [Python =>3.8](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [Redis](https://redis.io/download)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

## Documentation API

http://127.0.0.1:8000/swagger/ (if the application is running locally)

### Running the application locally

1. Clone the repository
```
$ git clone https://github.com/Shinobi3456/test_polls.git
```

2. Check into the cloned repository
```
$ cd testFunBox
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

5. Start the Django API
```
$ python manage.py runserver
```

6. Run tests
```
$ python manage.py test
```
