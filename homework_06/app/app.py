from flask import Flask, render_template, request, redirect, url_for
from models import db, Record

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'  # настроим под свои параметры
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    records = Record.query.all()
    return render_template('index.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_record = Record(name=name, description=description)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_record.html')

if __name__ == '__main__':
    app.run()