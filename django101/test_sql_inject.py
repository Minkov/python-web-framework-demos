from django101.web.models import Todo

x = Todo()
todos = Todo.objects.all()
param = 'the; DROP DATABASE;'
todos = Todo.objects.raw('SELECT * FROM web_todo WHERE title LIKE %s',
                         (param,))

print(todos[0])
