# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Esecuzione della pagina dei contenuti
@app.route('/')
def index():
    return render_template('index.html')


# Competenze dinamiche
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    button_html = request.form.get("button_html")
    button_db = request.form.get("button_db")
    return render_template('index.html', button_python=button_python , 
                            button_discord=button_discord,
                             button_html=button_html,
                            button_db=button_db
                              )
@app.route('/gigi', methods=['POST'])
def process_email():
    pippo = request.form.get("email")
    pluto = request.form.get("text")
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write(f"Email: {pippo}, Nome: {pluto}\n")
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
