How to run tests for this project:

1. Create virtual environment with the command: python -m venv (venv_name)
2. Install the requirements with the command from the src folder: pip install -r requirements.txt
3. Download chromedriver (latest version) for your appropriate operating system: https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
4. Unextract the folder and put the chromedriver file in the functional_tests folder.
5. Run the python manage.py test functional_tests command which runs the dummy test.