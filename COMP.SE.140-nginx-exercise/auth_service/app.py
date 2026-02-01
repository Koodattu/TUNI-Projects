from flask import Flask, request, redirect, make_response, render_template_string

app = Flask(__name__)

USERNAME = 'ex4user'
PASSWORD = 'ex4pass'

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    {% if error %}
    <script>alert("{{ error }}");</script>
    {% endif %}
    <form method="post" action="/login">
        Username: <input type="text" name="username"/><br><br>
        Password: <input type="password" name="password"/><br><br>
        <input type="submit" value="Login"/>
    </form>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        error = request.args.get('error')
        return render_template_string(LOGIN_PAGE, error=error)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            resp = make_response(redirect('/'))
            resp.set_cookie('auth', 'authenticated', max_age=3600)
            return resp
        else:
            return redirect('/login?error=Invalid credentials')

@app.route('/logout')
def logout():
    resp = make_response(redirect('/login'))
    resp.set_cookie('auth', '', expires=0)
    return resp

@app.route('/auth')
def auth():
    auth_cookie = request.cookies.get('auth')
    if auth_cookie == 'authenticated':
        return '', 200
    else:
        return '', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
