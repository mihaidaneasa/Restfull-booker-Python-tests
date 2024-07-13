## Restfull-Booker

### Exploration: 
Testing is more than just finding bugs. With Restful-booker-platform you can use it to hone your exploratory testing skills by diving into the application to find out more about how it works. There are many features for you to explore, with more being continuously added. So there will always be something new to explore!

### Automation: 
Restful-booker-platform is an open source application and it offers a range of different technologies that you can automate against, either online or via a locally deployed instance.

Check out the restful-booker-platform source code to learn more about the various APIs and JavaScript features to practise your Automation in Testing skills.

### Infrastructure:
Restful-booker-platform is a continuously deployed application using CircleCi and Docker. All the deployment assets can be found in the restful-booker-platform source repository for you to create your own pipeline. You can also learn more about the build process in this public build pipeline.

### Get Started: 
How you use this application is up to you, but here are a few things to get you started:
- Explore the home page
- Access the admin panel with the credentials admin/password
- You can read more about the features here
- If you find a particularly bad bug, feel free to raise it here
  
Please note: for security reasons the database resets every 10 minutes.


### Python API framework tests Project
In this project I tested a few features of Restfull Booker Rest API by sending GET, POST, PUT, PATCH and DELETE requests to "https://restful-booker.herokuapp.com" URL using API framework in Python with Pycharm IDE.

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