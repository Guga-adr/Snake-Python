class Snake:
    def __init__(self, cell_size, width, height):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (1, 0)  # Initial direction: right
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.grow_pending = 0

    def move(self):
        head = (
            self.body[0][0] + self.direction[0] * self.cell_size,
            self.body[0][1] + self.direction[1] * self.cell_size,
        )
        self.body.insert(0, head)

        if self.grow_pending > 0:
            self.grow()
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        self.body.append((0, 0))  # You can set the position to (0, 0) for now

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (
            -self.direction[0],
            -self.direction[1],
        ):
            self.direction = new_direction

    def check_collision(self):
        # Check if the snake collides with itself or the screen boundaries
        head = self.body[0]
        if (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
            or head in self.body[1:]
        ):
            return True
        return False
