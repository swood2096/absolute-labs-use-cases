from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_details = {
            'name': request.form['company_name']
            # Add other fields as needed
        }
        use_cases = backend.generate_use_cases(company_details)
        return render_template('index.html', use_cases=use_cases)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

