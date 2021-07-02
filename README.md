
# A Sandox for Flask and Heroku

I am preparing for a new project, and am testing out the Flask framework.
Additionally, I am becoming more comfortable with hosting via Heroku.

First, I followed this tutorial: 
https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/.

As I go forward I am experimenting with Flask and Heroku some more.

## What I've Learned so Far

### Deploying the App

- To run locally, run `app/main.py`. In VSCode this can be done with `F5`.

- To push to the Heroku servers, simply push to the personal repository. On
  Heroku, I set it up to immediately run the version that is pushed to the main
  branch (if it passes CI, which is not yet set up).

- The site is https://eflask-app-067.herokuapp.com/, and it runs indefinitely.

### Files

- The file `.gitignore` instructs git to ignore certain files, such as 
  `__pycache__` folders which are generated by python to store some information.

- The files `Pipfile` and `Pipfile.lock` were generated through the `pipenv` 
  command, and appear to give information on dependencies and the environment.

- The file `Procfile` appears to tell the server what to run on startup; 
  specifically, it runs `gunicorn` and targets the app variable in 
  `app/main.py`.

- The file `runtime.txt` is used by Heroku. It contains info regarding which
  version of Python to use. Only some are available, and the one reccomended by
  the tutorial does not work.

- The file `wsgi.py` (alternatively, `app.py`) is the starting point for code 
  execution.

- The folder `app` will contain code for the server to use, and resources like 
  HTML, CSS, and images that are sent.

- The `.env` file (which is sensitive and not sent to github) contains 
  environment variables for running the site locally. I believe I needed to 
  install `python-dotenv` for the file to actually be loaded. Instead of a 
  `.env` file, Heroku uses config variables that can be configured through the 
  CLI or through the site in Settings. If a variable is not present, 
  `os.getenv()` will return `None`, so it is import to handle this if necessary.

### Flask

- Proper execution starts via a call to `app.run()` (where app is the Flask 
  instance created in `main.py`). However, we need not call this function itself
  anywhere. For production, the `Procfile` tells `gunicorn` to run this 
  variable, and VSCode (using flask) knows to run it as well.

- The `app` variable is set up in `main.py`. Setting it up entails defining 
  functions that are to be called at different times to generate the site's
  response. These functions are linked to `app` by the `@app.route()` decorator,
  which takes a string representing which url(s) should trigger that function.

- For debuging purposes, it is possible that an endpoint function can send raw
  HTML in the form of a string. The `\deprecated` endpoint does this, for 
  example.

- Alternatively, you can write HTML in seperate files (in fact, you can write 
  templates, but normal HTML also works). The `render_template()` function 
  generates the full response object to be sent. See `\sample` or the homepage.

- You can also send a redirect message via `redirect()`. Use `url_for()` to 
  create the right url (that function takes the name (string) of another 
  endpoint function). See `\redirect`
