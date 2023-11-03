import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, no_of_balls_picked):
        no_of_balls_picked = min(no_of_balls_picked, len(self.contents))

        try_list = []

        for pick in range(no_of_balls_picked):
            try_list.append(self.contents.pop(random.randrange(len(self.contents))))

        return try_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum(
            [1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v]
        )
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments


hat = Hat(black=6, red=4, green=3)


probability = experiment(
    hat=hat,
    expected_balls={"red": 1, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
print(probability)
