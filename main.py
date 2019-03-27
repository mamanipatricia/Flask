# import requests
from flask import Flask, request, make_response, redirect, render_template, session, json
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm


app = Flask(__name__)

# bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Cafe', 'Enviar Solicitud de compra', 'ENtregar video al']

datas = [

        {
            "userId": 7,
            "id": 65,
            "title": "consequatur id enim sunt et et",
            "body": "voluptatibus ex esse s"
        },
        {
            "userId": 7,
            "id": 66,
            "title": "repudiandae ea animi iusto",
            "body": "officia veritatis teneto saepe"
        },
        {
            "userId": 7,
            "id": 67,
            "title": "aliquid eos sed fuga est maxime repellendus",
            "body": "reprehenderit id nostressitatibus molestiae"
        },
        {
            "userId": 7,
            "id": 68,
            "title": "odio quis facere architecto reiciendis optio",
            "body": "magnam molestiae perfeorro velit"
        },
        {
            "userId": 7,
            "id": 69,
            "title": "fugiat quod pariatur odit minima",
            "body": "officiisudiandae asperiores et saepe a"
        },
        {
            "userId": 7,
            "id": 70,
            "title": "voluptatem laborum magni",
            "body": "sunt repdolore"
        }
    ]

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello():
    # user_ip = request.remote_addr
    # user_ip = request.cookies.get('user_ip')
    # session, current_app, g = todos son dicccionarios
    user_ip = session.get('user_ip')

    # return 'Hello world FLASK, tu IP ES {}'.format(user_ip)
    context = {
        'user_ip': user_ip,
        'todos': todos,

    }
    return render_template('hello.html', **context)


@app.route('/api/v1/get-prices')
def getprices():
    # return requests.get('https://jsonplaceholder.typicode.com/posts').content
    data = [

        {
            "userId": 7,
            "id": 65,
            "title": "consequatur id enim sunt et et",
            "body": "voluptatibus ex esse s"
        },
        {
            "userId": 7,
            "id": 66,
            "title": "repudiandae ea animi iusto",
            "body": "officia veritatis teneto saepe"
        },
        {
            "userId": 7,
            "id": 67,
            "title": "aliquid eos sed fuga est maxime repellendus",
            "body": "reprehenderit id nostressitatibus molestiae"
        },
        {
            "userId": 7,
            "id": 68,
            "title": "odio quis facere architecto reiciendis optio",
            "body": "magnam molestiae perfeorro velit"
        },
        {
            "userId": 7,
            "id": 69,
            "title": "fugiat quod pariatur odit minima",
            "body": "officiisudiandae asperiores et saepe a"
        },
        {
            "userId": 7,
            "id": 70,
            "title": "voluptatem laborum magni",
            "body": "sunt repdolore"
        }
    ]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/v1/price', methods=['POST'])
def show_post():
    req = request.get_json()
    # return req
    res = ['default']
    for x in datas:
        if x['id'] == int(req['id']):
            res = x
            break
    response = app.response_class(
        response=json.dumps(res),
        # response=json.dumps(req),
        status=200,
        mimetype='application/json'
    )
    return response
