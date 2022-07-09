# acceptancetest-robotframework
This is a basic acceptance test for Face Recognition with robot framework, this acceptance test use keyword-based approach

## Extra information
* [Getting started Robot Framework](https://robotframework.org/#getting-started)
* [Writing Keywords](https://dev.to/younup/write-your-keywords-for-robot-framework-with-python-31eg)
* [DEVOPEDIA info about Robot Framework](https://devopedia.org/robot-framework)
* [Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#rules-for-parsing-the-data)
* [Robot Framework Quick Start Guide](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst)
* [Robot Framework Demo (Calculator)](https://github.com/robotframework/RobotDemo)

## How to use
### 1. __Install python libraries__
On root folder use
```
python -m pip install -r requirements.txt
python -m pip install opencv-contrib-python --user
```
### 2. __Install node packages__
Go to TestLibrary > recognize and use
```
npm i
```
### 3. __Start node server__
Go to TestLibrary > recognize > src and use
```
npm run start
```
### 4. __Testing with Robot Framework__
Go to robot folder and use
```
robot acceptance_test_F3.2.robot
```