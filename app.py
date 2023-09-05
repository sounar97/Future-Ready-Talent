import urllib.request
import json
import os
import ssl
from flask import Flask, render_template, request, jsonify

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
     data = request.json
     body = str.encode(json.dumps(data))
     url = 'http://426687ed-bb46-478e-b2cd-995453152ee8.centralindia.azurecontainer.io/score'
     api_key = 'EJOtLcGPg6EWWLUHCJpU3nsjhEMSSA3b'
     # Replace this with the primary/secondary key or AMLToken for the endpoint
     headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
     req = urllib.request.Request(url, body, headers)
     response = urllib.request.urlopen(req)
     result = response.read()
     result = json.loads(result.decode())
     response_data = {'prediction': result['Results'][0]}
     return jsonify(response_data)



    

            
            




if __name__ == '__main__':
    app.run(debug=True)

    
     
 
   

    
     




    



    



    
    
    