import sys
import time
from ortools.sat.python import cp_model

puzzle1 = """
.......1.
4........
.2.......
....5.4.7
..8...3..
..1.9....
3..4..2..
.5.1.....
...8.6...
"""

puzzle2 = """
...26.7.1
68..7..9.
19...45..
82.1...4.
..46.29..
.5...3.28
..93...74
.4..5..36
7.3.18...
"""

model = cp_model.CpModel()


class SudokuSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, values: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__values = values
        self.__solution_count = 0
        self.__start_time = time.time()

    @property
    def solution_count(self) -> int:
        return self.__solution_count

    def on_solution_callback(self):
        current_time = time.time()
        print(
            f"Solution {self.__solution_count}, "
            f"time = {current_time - self.__start_time} s"
        )
        self.__solution_count += 1

        solution = self.response_proto.solution
        for i in range(9):
            print("".join(str(solution[i * 9 + j]) for j in range(9)))
        print()


def read_board(puzzle: str) -> list[int]:
    out = []
    lines = puzzle.splitlines()

    for line in lines:
        for c in list(line.strip()):
            if c == ".":
                out.append(0)
            else:
                out.append(int(c))
    return out


board = read_board(puzzle2)
print(board)


values = []

# add 81 variables to the models corresponding to each cell
for j in range(9):
    for i in range(9):
        values.append(model.new_int_var(1, 9, f"x_{i, j}"))

# add 9 constraints for having different values in each column
for j in range(9):
    model.add_all_different(values[j * 9 : (j * 9 + 9)])

# add 9 constraints for having different values in each row
for i in range(9):
    model.add_all_different(values[i : (73 + i) : 9])

# add 9 box constraints
for top in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
    aux = []
    for j in range(3):
        for i in range(3):
            aux.append(values[top + i + j * 9])
    model.add_all_different(aux)

# impose constraints with known board elements
for i in range(81):
    if board[i] != 0:
        model.add_abs_equality(board[i], values[i])

solver = cp_model.CpSolver()
solution_printer = SudokuSolutionPrinter(values)
# solver.parameters.enumerate_all_solutions = True
solver.solve(model, solution_printer)

# Statistics.
print("\nStatistics")
print(f"  conflicts      : {solver.num_conflicts}")
print(f"  branches       : {solver.num_branches}")
print(f"  wall time      : {solver.wall_time} s")
print(f"  solutions found: {solution_printer.solution_count}")
