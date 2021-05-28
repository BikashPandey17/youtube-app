from myapp.source import app


def default():
    app.logger.info("OK")
    return "Server Up!"
