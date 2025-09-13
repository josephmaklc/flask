from flask import Flask, render_template
app = Flask(__name__)

@app.get("/")
def index():
    return "Hello Flask World. Try /page1 and /page2"

@app.get("/page1")
def page1():
   return "<h1>hello</h1><br/>This is like a <i>servlet</i>"
   
@app.get("/page2")
def page2():
    return render_template("mypage.html",name="Johnny")

if __name__=="__main__":
    app.run()
