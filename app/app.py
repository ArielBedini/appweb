from flask import Flask, request, render_template
<<<<<<< HEAD

app = Flask(__name__)
default_key = '1'
cache = {default_key: 'one'}
=======
import redis

app = Flask(__name__)
default_key = '1'
cache = redis.Redis(host='redis', port=6379, db=0)
cache.set(default_key, 'one')
>>>>>>> Clase022


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    key = default_key
    if 'key' in request.form:
        key = request.form['key']
    
    if  request.method == 'POST' and request.form['submit'] == 'save':
<<<<<<< HEAD
        cache[key] = request.form['cache_value']

    cache_value=None
    if key in  cache:
        cache_value = cache[key]
=======
        cache.set(key, request.form['cache_value'])

    cache_value=None
    if key in  cache:
        cache_value = cache.get(key).decode('utf-8')
>>>>>>> Clase022
    
    return render_template('inicio.html', key=key, cache_value=cache_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0')