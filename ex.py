from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return "SQLAlchemy"


##rendering pages



if __name__ == "__main__":
    app.run()