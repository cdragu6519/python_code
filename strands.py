height = 8
width = 6

puzzle = {
    "input": """
FESOBR
EDIMUE
BADRNV
CKADRE
EGNCUE
SABHLM
SCEVOL
KTREBE
""",
    "soulution_words": [
        "SOUNDCHECK",
        "REVERB",
        "FEEDBACK",
        "MIDRANGE",
        "BASS",
        "VOLUME",
        "TREBLE",
    ],
}


def make_grid(puzzle: dict[str, object]) -> dict[(int, int), str]:
    out = {}
    lines = puzzle["input"].splitlines()
    lines = [x for x in lines if len(x) > 0]
    for i, line in enumerate(lines):
        for j, value in enumerate(list(line)):
            out[(i, j)] = value

    return out


def get_neighbors(cell: tuple[int, int]) -> list[(int, int)]:
    out = []
    (i, j) = cell
    for ix in [i - 1, i, i + 1]:
        for jy in [j - 1, j, j + 1]:
            if ix >= 0 and ix < height and jy >= 0 and jy < width:
                if (ix, jy) != (i, j):
                    out.append((ix, jy))
    return out


grid = make_grid(puzzle)
# print(grid)

cell = (0, 5)
print(get_neighbors(cell))
