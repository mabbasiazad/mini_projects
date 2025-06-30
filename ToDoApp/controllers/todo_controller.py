from flask import Blueprint, render_template
from services.todo_service import TodoService
from flask import request, redirect, url_for

todo_controller = Blueprint('todo', __name__)
todo_service = TodoService()

@todo_controller.route('/', methods=['GET'])
def todo_list():
    sort_by = request.args.get('sort_by')
    filter_by = request.args.get('filter_by')
    todos = todo_service.get_all(sort_by=sort_by, filter_by=filter_by)
    return render_template('todo_list.html', todos=todos)

@todo_controller.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    todo_service.add(title, description)
    return redirect(url_for('todo.todo_list'))

@todo_controller.route('/edit/<int:todo_id>', methods=['GET'])
def edit_todo(todo_id):
    todo_item = todo_service.get_by_id(todo_id)
    if todo_item:
        return render_template('todo_edit.html', todo=todo_item)
    else:
        return redirect(url_for('todo.todo_list'))
    
@todo_controller.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        todo_service.update(todo_id, title, description)
    return redirect(url_for('todo.todo_list'))

@todo_controller.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo_service.delete(todo_id)
    return redirect(url_for('todo.todo_list'))
    

