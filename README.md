This assumes you have django installed on your system, if you don't then install it with

```
$ pip install Django==1.8.5
```
This example does't use virtualenv, to see how to setup virtualenv visit [Marina Mele's tutorial](http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html)

To use the template with startproject , you can use the --template argument.

```
$ django.admin.py startproject foo --template=project_name
```
To start the server navigate to foo folde and run 

```
$ python foo.py runserver
```

To use functional tests first install selenium

```
$ pip install --upgrade selenium
```

Copy the functional_tests folder to your new project folder

eg.

```
$ cp functional_tests/ foo/
```

Start server, open another terminal window and run

```
$ python functional_tests/all_users.py
```




