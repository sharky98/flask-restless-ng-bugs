# Translation
First, create the *.pot files. Then merge the new *.pot file into the existing *.po files. Then compile thoses *.po files into the *.mo files.
1. Enter into the venv and stay at the project root.
2. Run `pybabel extract -F babel.cfg -o .\project\translations\messages.pot .`
3. Run `pybabel update -i .\project\translations\messages.pot -d .\project\translations\`
4. Create the translations.
5. Run `pybabel compile -d .\project\translations`