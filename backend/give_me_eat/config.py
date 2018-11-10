"""
config.py  
- settings for the flask application object
"""

class BaseConfig(object):  
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///survey.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    SECRET_KEY = '$2y$12$MICpKplYkfCPlGCeSXQwaOT.wI/J5Ake10o/k4kKQvrQllVRg2iQm'