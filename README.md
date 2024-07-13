### Python Backend tests Project
In this project I tested a few features of Restfull Booker Rest API by sending GET, POST, PUT, PATCH and DELETE requests to "https://restful-booker.herokuapp.com" URL

### Features
All tests may be run from terminal commands: 
- python -m pytest --html=./Positive_tsts.html tests/positive_tests.py 
- python -m pytest --html=./Negative_tsts.html tests/negative_tests.py

This commands will generate tests reports.

### Project structure
1. requests_api folder
- restfull_booker_api file
2. tests folder
- negative_tests file
- positive_tests file

### Tests results
![Imagine 1](https://github.com/mihaidaneasa/Restfull-booker-Python-tests/blob/main/Positive%20tests.jpg)
![Imagine 2](https://github.com/mihaidaneasa/Restfull-booker-Python-tests/blob/main/Negative%20tests.jpg)