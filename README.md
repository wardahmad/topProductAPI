## Top Product API
### How to run the Project

* Create a new folder:
`mkdir newFolder`
* Moving Into the Folder
`cd newFolder`
* git clone
`git clone https://github.com/wardahmad/topProductAPI.git`
* Moving Into the Folder
`cd topProductAPI`
* Create a virtual environment:
`python -m venv env`
* activate the virtual environment:
`source env/Scripts/activate`
* install the requirements:
`pip install -r requirements.txt`
* Install uvicorn:
`$ pip install uvicorn`
* Run the server:
`$ uvicorn main:app --reload`
* Open <a>http://127.0.0.1:8000/topProduct</a>  on chrome
* Press `CTRL+C` to quit
* Use `pytest` After install pytest `pip install pytest`
* deactivate the virtualenv:
`deactivate`
* <a href="https://pypi.org/project/autopep8/">automatically formats Python code to conform to the PEP 8 style guide:</a>
`pip install --upgrade autopep8`
`autopep8 --in-place --aggressive --aggressive main.py`
`autopep8 --in-place --aggressive --aggressive test_main.py`
