from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def serve_html():
    return render_template('index.html')


@app.route('/write_file', methods=['POST'])
def write_file():
    data = request.form.get('data')

    if data:
        try:
            with open('data.json', 'w') as file:
                file.write(data)
            return data
        except Exception as e:
            return f"Error writing to {'data.json'}: {str(e)}"
    else:
        return "Please provide both data and file_name in the request."


@app.route('/read_file', methods=['GET'])
def read_file():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return f"File {'data.json'} not found."
    except Exception as e:
        return f"Error reading {'data.json'}: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

