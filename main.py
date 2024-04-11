from website import create_app

from flask_login import LoginManager

app = create_app()

if __name__ == '__main__':# you only want to run this server from this file 
    app.run(host="0.0.0.0", debug=False)
