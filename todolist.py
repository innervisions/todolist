class Todo:
    IS_DONE = "X"
    NOT_DONE = " "

    def __init__(self, title):
        self.title = title
        self.done = False

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    def __str__(self):
        status = self.IS_DONE if self.done else self.NOT_DONE
        return f"[{status}] {self.title}"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return self.title == other.title and self.done == other.done


class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
        self._todos.append(todo)


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

# Code omitted


def step_1():
    print("--------------------------------- Step 1")
    todo_list = setup()

    # setup() uses `todo_list.add` to add 3 todos

    try:
        todo_list.add(1)
    except TypeError:
        print("TypeError detected")  # TypeError detected

    for todo in todo_list._todos:
        print(todo)


step_1()
