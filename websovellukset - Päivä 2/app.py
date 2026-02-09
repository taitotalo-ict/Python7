from flask import Flask, request, render_template
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def home():
    # return "Hello world!"
    return '''
<!DOCTYPE html>
<head>
</head>
<body>
    <h1>Hello world!</h1>
    <p>This is a test</p>
</body>
'''

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    # json = request.args.get('json', None)
    if request.args.get('json') is not None:
        return {"Username": username}
    return f"Username: {username}"

@app.route('/users/<username>/json', methods=['GET'])
def get_user_json(username):
    return {"Username": username}

@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    print(type(user_id))
    return f"user_id is type: {Markup.escape(str(type(user_id)))}"


@app.get('/profile')
def profile():
    user = {'name': 'Christian'}
    title = 'Profiilisivu'
    return render_template('template.html', user=user, title=title)


if __name__ == '__main__':
    app.run(debug=True)