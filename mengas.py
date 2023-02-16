from flask import Flask

app=  Flask(__name__)

@app.route("/")
def ola():
    return "<b>E O Mengas!!</b>"

app.run()