# Git Wrapper

**Requirements**:
* Have Python 3.8 installed
* Have an activated virtual environment

**Steps**:
* Install requirements using pip (file is called requirements.txt)
* Edit settings.py inside git_wrapper before running migrations:
    * DJANGO_ADMIN_NAME: User name for admin
    * DJANGO_ADMIN_EMAIL: User email for admin
    * DJANGO_ADMIN_PASSWORD: User password for admin
    * ADMIN_GIT_TOKEN = User Personal Access Token for admin
* Run migrations (Admin user will be created with settings previous values)

**Adding new users:**
1. Go to http://127.0.0.1:8000 and click Login
2. Login with Admin user credentials, the page will redirect to home view
3. Click on Add user option
4. Populate all data


**Edit configurations**
1. Go to http://127.0.0.1:8000 and click Login
2. Login with Admin user credentials, the page will redirect to home view
3. Click on Edit configurations option
4. Update data needed for local repository path, API, Repository name and Main branch


**Create Pull Request**
1. Go to http://127.0.0.1:8000 and click Login
2. Login with Admin user credentials, the page will redirect to home view
3. Click on See branches option
4. If branches different from the main branch (specified in the configurations) exists, a Create pr link will be displayed
5. Click on create pr link
6. Populate Title and Description, for merge the PR, select Merge in the Save state, otherwise PR will only be saved and its state will remain open
7. Hit create


Notes: It has only been tested with GitHub API for create and merge Pull Request, the configuration for this API can be found in wrapper/config.json
