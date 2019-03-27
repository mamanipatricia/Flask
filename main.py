from flask import Flask, request, make_response, redirect, render_template, session
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm


app = Flask(__name__)

# bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Cafe', 'Enviar Solicitud de compra', 'ENtregar video al']


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
