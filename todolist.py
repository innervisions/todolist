import todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title


# Code omitted for brevity.

empty_todo_list = TodoList("Nothing Doing")


def setup():
    todo1 = Todo("Buy milk")
    todo2 = Todo("Clean room")
    todo3 = Todo("Go to gym")

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list
