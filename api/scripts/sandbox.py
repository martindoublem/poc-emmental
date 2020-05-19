from flask import current_app as app

from repository.clean import clean_all_database
from repository.science_feedback import sync


@app.manager.command
def sandbox():
    clean_all_database()
    sync()
