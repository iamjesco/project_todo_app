from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models.form import TodoForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '34twsfgd6t7ew45hgw4tgqwetg'
db = SQLAlchemy(app)

from models.TODO import Todos


@app.route('/', methods=["GET", "POST"])
def home():
	todo_list = Todos.query.all()
	form = TodoForm()
	if form.validate_on_submit():
		new_todo = Todos(
			todo=form.todo.data)
		db.session.add(new_todo)
		db.session.commit()
		flash('Todo created successfully', 'success')
		return redirect(url_for('home'))
	return render_template('todos.html', form=form, todo_list=todo_list)


@app.route('/delete/<int:pk>')
def delete(pk):
	todo = Todos.query.get_or_404(pk)
	db.session.delete(todo)
	db.session.commit()
	flash('Todo deleted successfully', 'danger')
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run()
