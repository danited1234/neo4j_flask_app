from flask import Flask
from queries.routes import queries

app = Flask(__name__)
app.register_blueprint(queries)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)