from flask import Flask, render_template,  send_from_directory

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def corrector_page():
    return render_template('home.html', title="Angry Reviewer")


@app.route("/rules")
def rules_page():
    return render_template('rules.html', title='Rules')


@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route('/<filename>')
def download_file(filename):
 # The directory where the files are  located
 # Flask's send_from_directory to send the file to the client
 return send_from_directory('sources', filename, as_attachment=True)
