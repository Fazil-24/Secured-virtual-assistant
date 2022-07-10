from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
    
@app.route("/task")
def task():
    return render_template("tasks.html")

@app.route("/generalassistant")
def GAM():
    return render_template("GA.html")

@app.route("/call_action")
def action():
    import call_action
    return render_template("index.html")





@app.route('/exec2')
def parse1():
	import tasks
	print("done")
	return render_template("tasks.html")

@app.route('/exec3')
def parse2():
    import face_test
    print("done")
    return render_template("signup.html")

@app.route('/exec4')
def parse3():
    import voice_auth
    print("done")
    return render_template("signup.html") 

@app.route('/exec5')
def parse4():
    import Gen
    print("done")
    return render_template("GA.html")    


@app.route("/admin")
def admin():
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(port=5000, debug=True)
