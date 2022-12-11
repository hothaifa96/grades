from flask import Flask

app = Flask(__name__)
grades = {
    'yali.soltz11@gmail.com': 10,
    'galsha2297@gmail.com': 10,
    'amitshurani@gmail.com': 10,
    'Aliav066@gmail.com': 10,
    'eladarditi1@gmail.com': 10,
    'pavlenkoleon@gmail.com': 10,
    'odedon123456@gmail.com': 10,
    'Tommy.rozenberg6@gmail.com': 10,
    'shon.barkan@gmail.com': 10,
    'goralishahar@gmail.com': 10,
    'hilooshefron25@gmail.com': 10,
    'Menachem.farkash1@gmail.com': 10,
    'danvolper2205@gmail.com': 10,
    'ilyglazer1617@gmail.com': 10,
    'Aharon589@gmail.com': 10,
    'tomernevo01@gmail.com': 10,
    'davidkvarts@gmail.com': 10,
    'yarden.yosefzon@gmail.com': 8,
    'adilevy156@gmail.com': 10,
    'nadavmor1342@gmail.com': 10,
    'Dor.shlush@gmail.com': 10,
    'Roieahal52@gmail.com': 10
};

@app.route('/<email>',methods=['GET'])
def home(email):
            return f' <h1 style="color:red;">{grades[email]}</h1> '

app.run()