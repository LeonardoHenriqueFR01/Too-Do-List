from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Task

main = Blueprint('main', __name__)

# Rota principal que exibe as tarefas
@main.route('/')
def index():
    tasks = Task.query.all()  # Pega todas as tasks do banco
    return render_template('index.html', tasks=tasks)

# Rota para visualizar todas as tasks
@main.route('/tasks')
def view_tasks():
    tasks = Task.query.all()  # Obtém todas as tasks do banco
    return render_template('view_tasks.html', tasks=tasks)  # Renderiza a página com a lista de tasks

# Rota para adicionar uma nova task
@main.route('/submit', methods=['POST'])
def submit():
    task_name = request.form.get('task')

    # Verifica se o campo de tarefa não está vazio ou com apenas espaços
    if task_name and task_name.strip():  
        new_task = Task(title=task_name.strip())  # Remove espaços extras
        db.session.add(new_task)  # Adiciona a task à sessão
        db.session.commit()  # Salva no banco de dados

    return redirect(url_for('main.index'))  # Redireciona para a página principal

# Rota para deletar uma task (agora usando POST por segurança)
@main.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # Obtém a task pelo ID ou retorna 404 se não encontrada
    db.session.delete(task)  # Deleta a task
    db.session.commit()  # Salva as alterações no banco de dados

    return redirect(url_for('main.index'))  # Redireciona para a página principal após deletar a task

# Rota para renomear uma task
@main.route('/rename/<int:task_id>', methods=['GET', 'POST'])
def rename_task(task_id):
    task = Task.query.get_or_404(task_id)  # Obtém a task pelo ID ou retorna 404 se não encontrada
    
    if request.method == 'POST':
        new_title = request.form.get('title')  # Obtém o novo título da tarefa a partir do formulário
        
        if new_title and new_title.strip():
            task.title = new_title.strip()  # Atualiza o título da task, removendo espaços extras
            db.session.commit()  # Salva as alterações no banco de dados
        
        return redirect(url_for('main.index'))  # Redireciona para a página principal após renomear

    return render_template('rename_task.html', task=task)  # Exibe a página para editar o título da task
