from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect("/")

@app.route("/show_dojo/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.dojo_with_ninjas(data)
    return render_template("dojo_show.html", dojo=dojo)

@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():    
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    Ninja.save(data)
    return redirect('/')






# @app.route("/delete/<int:id>")
# def delete_user(id):
#     data = {
#         "id":id
#     }
#     User.delete_user(data)
#     return redirect("/")


