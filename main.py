from flask import Flask,request

app=Flask(__name__)

@app.route("/p1_input",methods=["POST"])
def p1_input ():
    if request =="POST":
        input= request.form["text"]
        process_text=input.upper()
        return  process_text

@app.route("/p2_input",methods=["POST"])
def p2_input ():
    if request =="POST":
        input= request.form["text"]
        process_text=input.upper()
        return  process_text

if __name__=="__main__":
    if player == 1:
        p1_input()
    else:
        p2_input()
    app.run()
