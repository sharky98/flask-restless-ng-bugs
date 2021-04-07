This is a repository to illustrate bugs in http://www.github.com/mrevutskyi/flask-restless-ng

# How to run
1. Create the venv based on the requirements.txt file (there is a lot not used in there, I didn't strip down the venv from my template app).
2. Create the database by running `python manage.py init`
3. Import the fixtures from the file `SQLite Fixtures.sql`
4. Run the app by running `python run.py`
5. Go to `localhost:5000`

## Issues
### mrevutskyi/flask-restless-ng#12
After running, above table A, you have a button to add a new entry with a new Item A that has no linked Item B (valid per `nullable=True`).

When reloading the page, the Table A isn't able to load the data from the API with error `ValueError: Model <class 'NoneType'> is not known to any APIManager objects; maybe you have not called APIManager.create_api() for this model.`

### mrevutskyi/flask-restless-ng#13
A button is above table C. When launch, it create a new Item C and relationship to Item A id 1 and 2. However, it seems the relationship is not commited, but the API still return 204.
