from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig1314123"

@app.route('/hello')
def index():
    flash("What is your Name?")
    return render_template("base.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template('base.html')
    

if __name__ == '__main__':
    app.run()
    
