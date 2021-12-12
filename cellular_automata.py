from enum import Enum

import numpy as np
from PIL import Image

# Example - Rule 110
# 111	110	    101	    100	    011	    010	    001	    000
# 0	    0	    0	    1	    1	    1	    1	    0


class CellularAutomata:
    rule: int

    width: int
    height: int

    ca_matrix = None
    ca_matrix_rgb = None

    class StartState(Enum):
        CLASSIC = "cls"
        RANDOM = "rnd"

    start_state: StartState = StartState.CLASSIC

    def __init__(
        self,
        rule: int,
        height: int,
        width: int,
        start_state: StartState = StartState.CLASSIC,
    ):
        self.rule = rule
        self.height = height
        self.width = width
        self.start_state = start_state

    def create(self):
        self.ca_matrix = self._get_initial_state()

        for j in range(self.height - 1):
            self.ca_matrix.append(
                np.array(
                    [
                        self._next_by_rule(
                            self._prev_as_str(i, self.ca_matrix[j]), self.rule
                        )
                        for i in range(self.width)
                    ]
                )
            )

        self.ca_matrix_rgb = [
            [(self._to_rgb(p)) for p in row] for row in self.ca_matrix
        ]
        self.ca_matrix_rgb = np.array(self.ca_matrix_rgb, dtype=np.uint8)

    def _get_initial_state(self):
        if self.start_state == self.StartState.CLASSIC:
            initial_state = np.zeros(self.width, dtype=int)
            initial_state[int(self.width / 2)] = 1
            return [initial_state]
        if self.start_state == self.StartState.RANDOM:
            return [np.random.randint(0, 2, self.width)]

    def save(self, name=None):
        if not name:
            name = (
                f"rule{self.rule}_{self.start_state.value}_{self.height}x{self.width}"
            )
        img = Image.fromarray(self.ca_matrix_rgb)
        img.save(f"{name}.png")

    def _prev_as_str(self, index, array):
        indices = [index - 1, index, (index + 1) % len(array)]
        return "".join(map(str, array[indices]))

    def _next_by_rule(self, prev: str, rule: int):
        rule_conf = "{0:08b}".format(rule)
        index = 7 - int(prev, 2)
        return int(rule_conf[index])

    def _to_rgb(self, val):
        if val == 0:
            return (255, 255, 255)
        return (0, 0, 0)
