from src import config, app

if __name__ == "__main__":
    app.config['HOST'] = config.HOST
    app.config['DEBUG'] = config.DEBUG
    app.config['PORT'] = config.PORT
    app.run()
