#Importing the liabraries
import pickle
import numpy as np
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('Model.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    category = request.form['category']
    reviews = request.form['reviews']
    size = request.form['size']
    installs = request.form['installs']
    price = request.form['price']
    rating = request.form['rating']

    print("Category:", category)
    
    prediction=loadedModel.predict([[category, reviews, size, installs, price, rating]])[0]

    if prediction < 0:
        prediction = 0
    
    if prediction > 5:
        prediction = 5
    
    prediction = str(np.round(prediction,1)) + " / 5"
    
    return render_template('index.html', output=prediction)

       
#Main function
if __name__ == '__main__':
    app.run(debug=True)
