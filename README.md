# WeCare
## Requirements

- Ensure that your Python version is 3.8 or higher by running the following command:
```bash
python --version
```
or
```bash
python -V
```

- Verify that you have pip, the Python package management tool, installed by running:
```bash
pip --version
```

- Ensure that Git is installed on your system for version control. You can verify this by running:
```bash
git --version
```

### Cloning the Repository
You can clone this repository using the following command:
```bash
git clone https://github.com/Salome-Serna-R/WeCare.git
```
Or you can download the .zip package directly from the GitHub repository.

### Installing Dependencies
After cloning the repository, you need to install the required dependencies listed in the requirements.txt file. This file includes all the necessary packages for the project to function correctly. Run the following command in your terminal:
```bash
pip install -r requirements.txt
```
It also applies the following updates:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Applying Database Migrations
Next, you need to apply the initial migrations to set up the database. This is done using the following command in the terminal, while located in the root directory of the cloned project:
```bash
python manage.py migrate
```

### Running the Development Server
Finally, while ensuring you are in the correct project directory, you can start the Django development server by running:
```bash
python manage.py runserver
```
Once the server is running, open your web browser and go to http://127.0.0.1:8000 to see the application in action.


Note: If you want to use it you must ask for the client_secret file which can't be published in github, if you already have the file, you can try the app with an email that can be provided. In case of an error try deleting the file token.json. Use the email: wecareeafit@gmail.com
email: wecareeafit@gmail.com
password: WeCare2024

