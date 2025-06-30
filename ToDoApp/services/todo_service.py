from models.todo import Todo
from models import db

class TodoService:
    # def __init__(self):
    #     self._todos = [
    #         Todo(
    #             todo_id=1,
    #             title="Buy groceries",
    #             description="Milk, Bread, Eggs",
    #         ),
    #         Todo(
    #             todo_id=2,
    #             title="Clean the house",
    #             description="Living room, Kitchen, Bathroom",
    #         )
    #     ]

    @staticmethod
    def add(title, description):
        new_todo = Todo(
            title=title,
            description=description,
        )
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

        

    @staticmethod
    def get_all(sort_by=None, filter_by=None):
        query = Todo.query
        if sort_by == 'title':
            query = query.order_by(Todo.title)

        if filter_by:
            query = query.filter(Todo.title.ilike(f'%{filter_by}%'))
        return query.all()
    
    @staticmethod
    def get_by_id(todo_id):
        return Todo.query.get(todo_id)
    
    @staticmethod
    def update(todo_id, title, description):
        todo = TodoService.get_by_id(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete(todo_id):
        todo = TodoService.get_by_id(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return True
        return False
    




