from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///cakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class Cake(db.Model):
   title=db.Column(db.String(50), nullable=False, primary_key=True)
   price=db.Column(db.Integer,nullable=False)
   image=db.Column(db.String(100),nullable=False)
   category=db.Column(db.String(20),nullable=False)

   def __repr__(self) -> str:
      return f"{self.title} - {self.price} - {self.image} - {self.category}"


@app.route('/')
def indexPage():
   allCakes = Cake.query.all()
   return render_template("index.html",allCakes=allCakes)



@app.route('/delete')
def deletePage():
   allCakes = Cake.query.all()
   return render_template("index.html",allCakes=allCakes)



@app.route('/signin')
def signInPage():
   return render_template("signin.html")   



@app.route('/addcake',methods=['GET','POST'])
def addCakePage():
   if(request.method=="POST"):
      title=request.form['title']
      price=request.form['price']
      image=request.form['imageLink'] 
      category=request.form['category']
      cake=Cake(title=title , price=price , image=image, category=category)
      db.session.add(cake)
      db.session.commit()
   return render_template("addCake.html")   


if __name__ == "__main__":
    app.run(debug=True)    