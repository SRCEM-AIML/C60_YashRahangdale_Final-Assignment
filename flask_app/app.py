from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not name or not age or not age.isdigit():
            return "Invalid input! Please enter valid name and age.", 400
        return f"Hello {name}, you are {age} years old!"
    
    return render_template_string("""
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit">
        </form>
    """)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
