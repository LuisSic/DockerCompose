from flask import Flask
import redis
import os
app = Flask(__name__)

def get_env_variable(name):
    try:
        print(os.environ.get(name))
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

r = redis.Redis(host=get_env_variable("REDIS"), port=6379, db=0)
result = r.ping()
print("Ping returned : " + str(result))



@app.route("/get")
def home():
    name=r.get('name') or'World'
    return "Hello %s!" % name


@app.route("/set/<name>") 
def setname(name): 
    r.set('name',name) 
    return 'Nombre actualizado'

@app.route("/")
def hello():
    return "Hello Flask"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')