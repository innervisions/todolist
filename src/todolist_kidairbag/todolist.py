from todo import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def __str__(self):
        output_lines = [f"----- {self.title} -----"]
        output_lines += [str(todo) for todo in self._todos]
        return "\n".join(output_lines)

    def __len__(self):
        return len(self._todos)

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
        self._todos.append(todo)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def todo_at(self, index):
        return self._todos[index]

    def to_list(self):
        return self._todos.copy()

    def mark_done_at(self, index):
        self.todo_at(index).done = True

    def mark_undone_at(self, index):
        self.todo_at(index).done = False

    def mark_all_done(self):
        def mark(todo):
            todo.done = True
        self.each(mark)

    def mark_all_undone(self):
        def mark(todo):
            todo.done = False
        self.each(mark)

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, index):
        del self._todos[index]

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)

        def choose(todo):
            if callback(todo):
                new_list.add(todo)

        self.each(choose)
        return new_list

    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        todo = self.find_by_title(title)
        todo.done = True

