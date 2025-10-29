from flask import Flask, render_template, request, redirect, url_for, flash #flask é a biblioteca e Flask é a classe principal dentro da biblioteca
from models import db, Task #db é o tradutor do SQLAlchemy. Gerencia a conexao com o banco de dados

#render template lê os arquivos em html e substitui por variaveis logicas do python
#main.py cuida das rotas(logica web)
#models.py cuida da logica do banco de dados

app = Flask(__name__)
app.secret_key= '981838467gui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

with app.app_context():
    db.create_all() #cria o banco de dados

@app.route('/') #@ decorador (embrulhador) embrulha a função que está abaixo dele -> conecta uma URL do navegador a um pedaço do codigo python
def index():
    tasks = Task.query.all() #Consultar a tabela do banco de dados e pegar todas as tarefas que estão dentro e salvar em uma lista chamada task
    return render_template('index.html', tasks=tasks) #envio dos dados python para o html

@app.route('/add', methods=['POST']) # Postando informaçoes para o servidor, aceitar dados enviados por um formulário
def add():
    title = request.form.get('title') #basicamente um input()
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
    flash (f"Tarefa '{task.title}' concluída com sucesso!", "sucesso")
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
