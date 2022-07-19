from flask import Flask,request,render_template
#import config

app = Flask(__name__,template_folder='../templates',static_folder="",static_url_path="")
#app.config.from_object(config)

@app.route('/')
def first():
    return render_template('index.html')#request.args.get('info')#'{\'return\':\'0\'}'

@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'

@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)


if __name__=='__main__':
    app.run(debug=True)