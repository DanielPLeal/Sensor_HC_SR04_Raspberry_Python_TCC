import json
from flask import Flask, jsonify   
from flask import render_template
app = Flask(__name__)

#from SensorApp import sensor
# s = sensor.valor()

#teste de JSON
#@app.route("/")
#def index():
#    nome = "teste sensor"
#    posts = ["Flask basico","Flask intermadiario","Flask avancado"]
#    return render_template("index.html",nome=nome,posts=posts)
    #return jsonify({"message":"Hello Json"})


@app.route("/")
def sensor(name=None):
     return render_template('MedSensorRasp.html')
     

#@app.route("/sensor")
#def medidas():
#    import SensorApp
#    return render_template('MedSensorRasp.html')

@app.route('/sensor', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        val = int(request.form['MedSensorRasp.html'])
        current_states = states[:]
        current_states[val] = not current_states[val]
        return render_template('MedSensorRasp.html', states=current_states)
    else:
        return render_template('MedSensorRasp.html', states=states)

#@app.route('/hello/<name>')
#def hello(name):
#    return render_template('page.html', name=name)
        
   
if __name__=="__main__":
    #app.run(debug=True, port=6543)
    app.run(host='0.0.0.0',port=5000)



    
 
