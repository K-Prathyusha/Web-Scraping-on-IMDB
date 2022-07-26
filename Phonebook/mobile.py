from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/url")
def url():
    return redirect(url_for("index"))
    #return render_template("url.html")

@app.route("/new",methods=['GET','POST'])
def new():

    inp=request.form.get('inp')
    if inp=="google":
        return redirect ("https://www.google.co.in/")
    if inp=="innomatics":
        return redirect("https://online.innomatics.in/")
    if inp=="linkedin":
        return redirect("https://www.linkedin.com/feed/")
    return render_template("new.html")
database={}
@app.route("/add")
def add():
    return render_template("add.html")
    

@app.route("/search",methods=['GET','POST'])

def search():
    search=request.form.get('se')
    return render_template("search.html",database=database,search=search)

@app.route("/display")
def display():
    return render_template("display.html",database=database)

@app.route("/home",methods=['GET','POST'])
def home():
    #database={}
    name=request.form.get('Name')
    phone=request.form.get('phone')
    database[name]=phone

    return render_template("home.html",database=database)



if __name__ == '__main__':
    app.run(debug=True)
