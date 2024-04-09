import os
from flask import Flask, request, jsonify, render_template
#from flask_cors import CORS
from subprocess import run, PIPE

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/compile', methods=['POST'])
def compile_code():
    # Create the 'uploads' directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Check if the POST request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded file to the server
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Compile the source code
    compile_command = f"python main.py {file_path}"
    os.system(compile_command)

    # Generate the object file
    llc_command = f"clang -c output.ll -o output.o"
    os.system(llc_command)

    # Generate the executable
    gcc_command = f"gcc output.o -o output"
    os.system(gcc_command)

    # Execute the executable
    execution_output = os.popen("./output").read()

    # Respond with the output from executing the executable
    return jsonify({'output': execution_output})



if __name__ == '__main__':
    app.run(debug=True)
