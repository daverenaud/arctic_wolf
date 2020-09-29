from flask import Flask

from api.routes import set_routes

app = Flask(__name__)
set_routes(app)
app.run()
