from timeit import default_timer as timer

# input: target area: x=269..292, y=-68..-44
# deferring on writing an input reader because the input is so simple and parsing
# it would be incredibly annoying

# part 1 is solved as the sum of the series of -y_min

x_max = 292
x_min = 269
y_max = -44
y_min = -68

# x_max = 30
# x_min = 20
# y_max = -5
# y_min = -10

class Probe():
    def __init__(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.x = 0
        self.y = 0

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        # self.x_velocity = 0 if self.x_velocity == 0 else self.x_velocity - 1 if self.x_velocity > 0 else self.x_velocity + 1
        if self.x_velocity == 0:
            self.x_velocity = 0
        elif self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.x_velocity += 1
        self.y_velocity = self.y_velocity - 1
        # print(f"x: {self.x, self.x_velocity}, y: {self.y, self.y_velocity}")
        # return self.x, self.y

    def plot_trajectory(self, x_velocity, y_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        while self.x <= x_max and y_min <= self.y:
            # print(self.x <= x_max, y_min <= self.y)
            self.move()
            within_x = x_min <= self.x <= x_max
            within_y = y_min <= self.y <= y_max
            # print(within_x, within_y)
            if within_x and within_y:
                return True
        return False

    def reset(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.x = 0
        self.y = 0

if __name__ == "__main__":
    velocities = 0
    p = Probe()
    start = timer()
    for x in range(x_max + 1):
        for y in range(-2278, 2278):
            if p.plot_trajectory(x, y):
                velocities += 1
            p.reset()
    end = timer()
    print(f"Part 2: {velocities}")
    print(f"Ran in {end - start} seconds")
