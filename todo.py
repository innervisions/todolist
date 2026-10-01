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
