import sys
import os

# Adiciona o diretório raiz do seu projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from app import create_app, db
from app.models import Task

# Criação do app Flask (necessário para acessar o banco de dados)
app = create_app()

# Contexto de aplicação, necessário para interagir com o banco de dados
with app.app_context():
    # Consultando todas as tasks do banco de dados
    tasks = Task.query.all()

    # Convertendo os resultados para um DataFrame do Pandas
    tasks_data = pd.DataFrame([task.as_dict() for task in tasks])

    # Exibindo o DataFrame
    print(tasks_data)
