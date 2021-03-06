>A virtual environment is a copy of the Python interpreter into which you can install pacakages privately, 
>without affecting the global Python interpreter installed in system
>it prevent package clutter and version conflicts 

##Install pip first

> pip is a Python package manager
```
$ sudo apt-get install python3-pip
```
>Verify it 
```
$ pip -V 
```

>Ubuntu
>Install python3-venv package that provides venv module
```
$ sudo apt install python3-venv
or
$ sudo apt-get install python3-venv
```

>Go to the Dir you want to create virtual environment and execute this cmd
```
$ python3 -m venv venv
$ python3 -m venv virtual-environment-name -> example
```
>you can change last venv to your required environmental name

##Activate the venv
```
$ source venv/bin/activate
(venv) $
```
>once activated you will find venv as prefix 

##To deactivate
```
(venv) $ deactivate
```

>what ever the install packages will be available and isolated only to this venv


>If you have requirement.txt file, after activating venv use this cmd to install all dependencies
```
$ pip install -r requirements.txt
```

##list packages that installed
```
$ pip list
```

##To automatically insert into requirement.txt file
```
$ pip3 freeze > requirements.txt 
```

>direct pip installation of dependencies has a vunarability with request package.
>So pipenv carries hash where it installs only specified package version

>Another way we can use pipenv or poetry
```
$ pip install pipenv
```

>create virtual env for project use follow cmd
```
$ pipenv shell
$ pipenv install flask
$ pipenv install requests
```
>to uninstall 
```
$ pipenv uninstall flask
```
>to deactivate virtual env
```
$ exit
```

>To check pip package installed successfully or not use Python interpreter 
```
(venv) $ python
>> import flask
>>
```
if no error then flask installed successfully 


##Routes:
The association between URL and python function that handles it is called a Route



