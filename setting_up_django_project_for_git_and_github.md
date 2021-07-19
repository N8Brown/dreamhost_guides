# DreamHost Guide: Setting Up a Django Project for Git & GitHub

In addition to the standard PHP, DreamHost allows users to host websites that are run on Python, Ruby, or Node.js. This guide will explain how to set up a Python-backed Django project locally for development in a way that is optimized for deploying to a DreamHost server from GitHub using the `git clone` command.

*(NOTE: This guide assumes that you have Git installed on your local machine and that you have a GitHub account)*

## Starting Local Django Project

There are two options for starting a Django project that will work well when it comes to cloning from GitHub to a DreamHost server. This guide will provide step-by-step for both.

*(NOTE: The steps and methods described below are by no means the only ways to structure a Django project for deployment on a DreamHost server. They do, however, make the process easier when the time for deployment comes)*

*(NOTE: In the steps listed below, any command that contains _name (i.e. - project_name, environment_name, etc.) represents a place-holder that should be changed to a name appropriate to your project)*

1. Open a terminal on your local machine and `cd` into the directory where you would like your Django project to reside.

2. Make a new directory with the name of your project. *(NOTE: For ease of configuration it is recommended to name this directory the same name you will be giving your Django project)*
```sh
mkdir project_name
```

3. Change into your new project directory
```sh
cd project_name
```

4. Create a virtual environment. *(NOTE: For the purposes of this guide, the* `venv` *virtual environment tool that comes with Python 3 is used. If you prefer a different tool for setting up virtual environments, please refer to the tools official documentation)*
```sh
python3 -m venv environment_name
```

5. Activate your new virtual environment.

Windows:
```sh
environment_name\Scripts\activate
```

Mac/Linux:
```sh
source environment_name/bin/activate
```

You should now see `(environment_name)` pre-fixed to the directory in the terminal *(NOTE: How this appears will differ based on the terminal being used)*:

Windows Example:
```sh
(environment_name)C:\Users\<path to your project directory>
```

6. Install Django
```sh
pip install django
```

7. Start a new Django project:

### OPTION 1

Start a Django project using the optional directory path argument *(NOTE: BE SURE TO INCLUDE THE PERIOD AT THE END AS THIS IS THE OPTIONAL ARGUMENT)*
```sh
django-admin startproject project_name .
```

*NOTE:* 
* *It is recommended to replace* `project_name` *with the same name used for the project directory* 
* *It is important to include the* `.` *after the project name as this will affect the project directory structure*  

If the above steps are executed properly, the project directory should look like this:
```bash
|---project_name
    |---environment_name
    |---project_name
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py

```

### OPTION 2

Start a Django project using the standard command *(NOTE: This does NOT use the optional directory path argument)*

```sh
django-admin startproject project_name
```

By excluding the optional directory path argument (In this case, the `.`) the project directory should look like this:

```bash
|---project_name
    |---environment_name
    |---project_name
        |---project_name
            |---__init__.py
            |---asgi.py
            |---settings.py
            |---urls.py
            |---wsgi.py
        |---manage.py
```

By excluding the `.` after `project_name` an extra layer is added to the directory tree (there are now three folders named `project_name`). The difference is subtle at first glance, but important nonetheless. 

8. Change directories if necessary and make sure you're in the directory containing the `manage.py` file. *(NOTE: You can use the* `ls` *command on Mac/Linux or the* `dir` *command on Window to display the current list of files/directories)*. If you see `project_name   manage.py`, then you are in the correct directory

9. Initialize Git and set the remote to a new GitHub repository.

10. Add a `.gitignore` file (should be in the same directory as the `manage.py` file) and be sure to add any files/directories to the `.gitignore` file that you don't wish to push to GitHub. These will typically include: 

- Virtual environment directory (if in the same directory location)
- All `__pycache__` directories
- Any other files/directories used only for development purposes
- `.env` file (used to hold SECRET_KEY and any other settings that should not be public)
- `settings.py` (if not using environmental variables)

11. Add and commit files and push changes/additions to GitHub like any other project

## Option 1 vs. Option 2

*What's the difference between the two options, and is one better than the other?*

The files being pushed to GitHub should be identical and in the same structural format regardless of which option is used. Both options will ensure that the project is properly structured for when the time comes to clone the GitHub repository to the DreamHost server. The only real difference comes on the local development side. 

The base GitHub file structure should look something like this:

```bash
|---GitHub_Repository
    |---project_name
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py
    |---.gitignore
```

*(NOTE: Adding one or more apps to a Django project will add additional directory folders and files. Additionally, users may wish to include a README.md file as well. These are perfectly fine and do not impact deployment to DreamHost servers)*

With regards to local development differences:

Option 1
- User is able to activate/deactivate their virtual environment and execute Git commands all from the same place without having to change into a different directory
- Less likely to initialize Git from the wrong location


Option 2
- User will have to activate their virtual environment and then change into the project directory in order to execute Git commands.
- More likely to initialize Git from the wrong location

The differences are ultimately minor and come down to user preference. The important part is making sure that the file structure pushed to GitHub is accurate. Doing so will help prevent the need to manually adjust settings files, static/template file links, etc.
