from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task



app = Flask(__name__)
app.secret_key= '981838467gui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/concluir/<int:task_id>')
def concluir(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    flash(f"Tarefa '{task.title}' concluída com sucesso!", "sucesso")
    return redirect(url_for('index'))

@app.route('/deletar/<int:task_id>')
def deletar(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f"Tarefa '{task.title}' deletada com sucesso!", "sucesso")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
