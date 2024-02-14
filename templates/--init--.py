from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_objecti(config)

from SINGLEPAGEAPPHW2 import routes 

