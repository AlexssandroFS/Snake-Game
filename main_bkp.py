from flask import Flask, render_template, request
app = Flask(__name__)
#bd=("usuario":"alexssandro.ferreira300@gmail.com","senha":"123")

def converte_romano(numero):

#coloque o seu codigo aqui

@app.route("/")
def romano():
        if request.method == "POST"
                request = request.format
                print("response")
                print(response)
                return render_template("snake.html")
	
                numero = reponse["valor:"]

                romano = converte_romano(romano)

                return romano

        elif request.method == "GET":
                return render_template("JS_Snake.html")

if __name__== "__main__":
	app.run(host="0.0.0.0",debug=True)
