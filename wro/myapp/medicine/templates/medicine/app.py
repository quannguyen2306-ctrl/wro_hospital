import json
from unittest import result
from flask import request
from flask import Flask, render_template
from nbformat import write
from numpy import result_type
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('./home.html')
@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output) #this converts the json output to a python dictionary
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary
    with open("data.json",'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["prescription"].append(result)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
    return result


if __name__ == "__main__":
    app.run(debug=True)

