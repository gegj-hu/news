from  flask  import Flask

app = Flask(__name__)



@app.route('/')
def demo():
    return 'hello2'



if __name__ == '__main__':

    app.run()
