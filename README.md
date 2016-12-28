flask-boilerplate
=================

Setup
-----

* Clone the repository:

```
git clone git@github.com:wilspi/flask-boilerplate.git
```

* Install Dependencies in virtual environment    
Read more [here](docs.python-guide.org/en/latest/dev/virtualenvs/)

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

* Configure parameters

Edit configurations in ```myapp/config.py```


* Change app name
Rename myapp to ```<your_app_name>```
and run
```sh
find . -type f -name '*.py' -exec sed -i '' s/myapp/<your_app_name>/ {} +
```