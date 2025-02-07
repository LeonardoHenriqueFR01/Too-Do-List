from . import db  # Importa o SQLAlchemy do __init__.py

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id} - {self.title}>'

    # Método para transformar o objeto em um dicionário
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
