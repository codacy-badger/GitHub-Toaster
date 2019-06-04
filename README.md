# GitHub Toaster
<a href="https://snyk.io/test/github/jieggii/GitHub-Toaster?targetFile=requirements.txt"><img src="https://snyk.io/test/github/jieggii/GitHub-Toaster/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/jieggii/GitHub-Toaster?targetFile=requirements.txt" style="max-width:100%;"></a>
Get toast notifications from GitHub directly on your desktop
<img src="https://imgur.com/3ekMkWy.jpg">

## About
<b>GitHub Toaster</b> allows you to receive notifications from GitHub directly on your desktop via toast notifications


## Supported platforms
<b>Only</b> Windows 10

## Requirements
* Python 3
* requests
* win10toast

## Installation
### Downloading program & installing requirements
```bash
git clone https://github.com/jieggii/GitHub-Toaster.git
cd GitHub-Toaster/
pip install -r requirements.txt
```

### Setting up
```json
{  
  "username": "your username",  
  "access_token": "your GitHub access token here",  
  "notification_duration": 5,  
  "delay": 5  
}
```
* ```username``` - your GitHub username
* ```access_token``` - your GitHub access token
* ```notification_duration``` - duration (sec) of toast notifications
* ```delay``` - delay (sec) before getting updates from GitHub

1. Get your GitHub access token. Go <a href="https://github.com/settings/tokens">here</a>, press <b>Generate new token</b> and turn on checkbox in the scope <b>Notifications</b>
2. Set variables in <b>config.json</b>

### Running
#### Run ```notifier.py``` to see terminal:
```python notifier.py```

#### OR

#### Run ```notifier.pyw``` not to see terminal:
```python notifier.pyw```

In both cases you will see this message:
<br>
<img src="https://imgur.com/SouzUJf.jpg">

### Adding to startup
When you set everything up and checked perfomance, you are ready to add the program to startup
1. Place program into comfortable place (e.g. ```C:\Program Files\```)
2. Open explorer
3. Locate to program folder
4. <b>Right click</b> on ```notifier.pyw``` 
5. ```Send ``` ```>``` ``` Desktop (create shourtcut)```
6. Go to desktop
7. Copy ```notifier.pyw (shortcut)``` to ```C:\Users\<your_username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```
8. Done! Now program will be started with the system

## License
Project is placed under MIT License

## Thanklist
There are no contributors yet

## Todo
 - [x] Notifications from <b>GitHub news feed</b>
 - [ ] Notifications from <b>watched repositories</b>


## Contribution
You can add any updates & fixes via  <b>pull requests</b>. Your nickname will be added into <a href="#thanklist"><b>thanklist</b></a>
