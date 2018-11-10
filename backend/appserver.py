"""
appserver.py  
- creates an application instance and runs the dev server
"""


from flask_login import LoginManager

if __name__ == '__main__':  
    from give_me_eat.application import create_app
    app = create_app()
    login = LoginManager(app)
    #app.run()
    app.run(host="0.0.0.0", port=8080)
