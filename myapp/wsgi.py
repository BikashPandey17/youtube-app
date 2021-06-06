from myapp.source import create_app
from myapp.config import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run()