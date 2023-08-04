from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained machine learning model
with open('regression.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    cylinders = int(request.form['cylinders'])
    horsepower = float(request.form['horsepower'])
    acceleration = float(request.form['acceleration'])
    origin = int(request.form['origin'])
    displacement = float(request.form['displacement'])
    weight = float(request.form['weight'])
    model_year = int(request.form['model_year'])
    
    # Prepare the input data for prediction
    input_data = [[cylinders, displacement, horsepower, weight, acceleration,model_year, origin]]
    # Make the prediction using the loaded model
    mpg_prediction = model.predict(input_data)
    
    result=round(mpg_prediction[0],2)
    label="The Miles Per Gallon (MPG) would be "+str(result)
    return render_template('index.html', prediction=label)

if __name__ == '__main__':
    app.run(debug=False,port=3005)
    
    
    
    
    
