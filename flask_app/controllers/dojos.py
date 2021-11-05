from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_dojos()
    return render_template("dojo.html", dojos = dojos)



@app.route("/new_ninja")
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():    
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    Dojo.save_ninja(data)
    return redirect('/show_dojo/{{ dojo.id }}')

@app.route("/show_dojo/<int:dojo_id>")
def show_dojo(dojo_id):
    data = {
        "id":dojo_id
    }
    dojo = Dojo.get_one(data)
    return render_template("dojo_show.html", dojo=dojo)




@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save_dojo(data)
    return redirect("/")


# @app.route("/delete/<int:id>")
# def delete_user(id):
#     data = {
#         "id":id
#     }
#     User.delete_user(data)
#     return redirect("/")


