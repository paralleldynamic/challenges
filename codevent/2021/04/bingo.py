from itertools import chain

class Board():
    def __init__(self, tiles, draws):
        self.tiles = tiles
        self.all_tiles = set(chain.from_iterable(tiles))
        self.tile_sets = self.get_all_tile_sets()
        self.wins_at_draw = self.evaluate(draws)

    def get_all_tile_sets(self):
        rotated = map(set, zip(*self.tiles))
        tile_sets = list(map(set, self.tiles))
        tile_sets.extend(rotated)
        return tile_sets

    def evaluate(self, draws):
        wins_at_draw = min(map(lambda x: max(i for i, v in enumerate(draws) if v in x), self.tile_sets))
        return wins_at_draw + 1

    def score(self, draws):
        drawn_tiles = set(draws[:self.wins_at_draw])
        undrawn_tiles = self.all_tiles - drawn_tiles
        score = sum(undrawn_tiles) * draws[self.wins_at_draw - 1]
        self.score = score
        return score

    def __repr__(self):
        return f"Board(<Wins at draw {self.wins_at_draw} with {self.tiles}>)"

class InputReader():
    INPUT_PATH = "input.txt"

    def __init__(self, input_path = INPUT_PATH):
        self.read_input_file(input_path)

    def read_input_file(self, input_path):
        boards = []
        board_collector = []

        with open(input_path, "r") as input:
            draws = input.readline()
            draws = list(map(int, draws.split(",")))
            for row in input:
                r = row.strip()
                if r and len(board_collector) <= 5:
                    r = r.split()
                    r = list(map(int, r))
                    board_collector.append(r)
                elif len(board_collector) == 5:
                    boards.append(Board(board_collector, draws))
                    board_collector = []
                elif not r:
                    continue
            if len(board_collector) == 5:
                boards.append(Board(board_collector, draws))

        self.draws = draws
        self.boards = boards

    def __repr__(self) -> str:
        return f"InputReader< Board Count: {len(self.boards)} >"

if __name__ == "__main__":
    ir = InputReader()
    draws = ir.draws
    winning_draw = min(map(lambda x: x.wins_at_draw, ir.boards))
    winning_boards = filter(lambda x: x.wins_at_draw == winning_draw, ir.boards)
    highest_score = max(map(lambda x: x.score(draws), winning_boards))

    losing_draw = max(map(lambda x: x.wins_at_draw, ir.boards))
    losing_boards = filter(lambda x: x.wins_at_draw == losing_draw, ir.boards)
    lowest_score = min(map(lambda x: x.score(draws), losing_boards))
    print(f"The highest possible score for these Bingo boards is: {highest_score}. The lowest is: {lowest_score}.")
