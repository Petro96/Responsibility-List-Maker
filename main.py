from website import create_app

app = create_app()

app.config.from_object("config")

if __name__ == '__main__':# you only want to run this server from this file 
    app.run(host=app.config.get('APP_HOST'),
            port=app.config.get('FLASK_DEVELOPMENT_PORT'),
            debug=app.config.get('FLASK_DEBUG'))
