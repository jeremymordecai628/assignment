#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from model import db, Student, Grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/student/<int:student_id>', methods=['GET', 'POST'])
def view_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        subject = request.form['subject']
        score = float(request.form['score'])
        grade = Grade(subject=subject, score=score, student_id=student_id)
        db.session.add(grade)
        db.session.commit()
    grades = Grade.query.filter_by(student_id=student_id).all()
    avg = sum(g.score for g in grades) / len(grades) if grades else 0
    return render_template('view_student.html', student=student, grades=grades, avg=avg)

if __name__ == '__main__':
    app.run(debug=True)

