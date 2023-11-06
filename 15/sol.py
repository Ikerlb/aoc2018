from sys import stdin
from collections import deque, Counter
from itertools import product

def extract_path(visited, r, c):
    res = [(r, c)]
    while visited[(r, c)] is not None:
        r, c = visited[(r, c)]
        res.append((r, c))
    res.reverse()
    return res

class Warrior:
    def __init__(self, r, c, band, hp = 200, ap = 3):
        self.r = r
        self.c = c
        self.band = band
        self.hp = hp
        self.ap = ap

    def clone(self):
        return Warrior(self.r, self.c, self.band, self.hp, self.ap)

    def attack_range(self, grid):
        neighbors = list(grid.neighbors(self.r, self.c, include_warriors = True))
        for t in neighbors:
            if t not in grid.warriors:
                continue
            if grid.warriors[t].band == self.band:
                continue
            yield grid.warriors[t]

    def move_range(self, grid):
        enemies = [w for w in grid.warriors.values() if w.band!=self.band]
        if not enemies:
            return None

        inrange = set()
        for e in enemies:
            for ner, nec in grid.neighbors(e.r, e.c):
                inrange.add((ner, nec))

        if not inrange:
            return []

        # do simple bfs, to see if it is
        # possible to reach an enemy's neighs
        q = deque([(self.r, self.c)])
        visited = {(self.r, self.c): None}
        k = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in inrange:
                    # extract from visited.
                    # the logic is that, rather
                    # than calculating all of the
                    # possible paths, if we use a
                    # queue, then if the neighbors
                    # functions visits in reading
                    # order, then whenever we find
                    # a target, it is guaranteed
                    # to be the first in reading order
                    # I wrap it in a list because my previous
                    # solution used a list of paths (didn't
                    # think it'd be this big)
                    return [extract_path(visited, r, c)]
                for nr, nc in grid.neighbors(r, c):
                    if (nr, nc) not in visited:
                        visited[(nr, nc)] = (r, c)
                        q.append((nr, nc))
            k += 1
        return []

    def attack(self, grid, target):
        target.hp -= self.ap
        if target.hp <= 0:
            #print(f"{self.r},{self.c} killed {target}")
            del grid.warriors[(target.r, target.c)]

    # obvs it mutates self and grid
    def move(self, grid):
        if (ars := list(self.attack_range(grid))):
            ars.sort(key = lambda w: (w.hp, w.r, w.c))
            target = ars[0]
            self.attack(grid, target)
        else:
            mrs = self.move_range(grid)
            if mrs is None: # can't complete round, its over
                #print(f"{self.r},{self.c} encountered no enemies")
                return False
            elif mrs:
                mrs.sort()
                path = mrs[0]
                r, c = path[0]
                nr, nc = path[1]
                del grid.warriors[(r, c)]
                grid.warriors[(nr, nc)] = self
                self.r = nr
                self.c = nc
                if (ars := list(self.attack_range(grid))):
                    ars.sort(key = lambda w: (w.hp, w.r, w.c))
                    target = ars[0]
                    self.attack(grid, target)
        return True

    def __repr__(self):
        return f"{self.band}({self.hp})"

class Grid:
    def __init__(self, lines):
        self.warriors = {}
        self.inbounds = set()
        self.rows = len(lines)
        self.cols = len(lines[0])

        for row, line in enumerate(lines): 
            for col, c in enumerate(line):
                if c == "#":
                    continue
                self.inbounds.add((row, col))
                if c in "EG":
                    self.warriors[(row, col)] = Warrior(row, col, c)

    def neighbors(self, r, c, include_warriors = False):
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            tup = (r + dr, c + dc)
            if tup in self.inbounds and include_warriors:
                yield tup
            elif tup in self.inbounds and tup not in self.warriors:
                yield tup

    def move(self):
        order = list(self.warriors.values())
        order.sort(key = lambda w: (w.r, w.c))
        for w in order:
            if w.hp > 0 and not w.move(self):
                return False
        return True

    def __repr__(self):
        res = []
        for r in range(self.rows):
            row = []
            warriors = []
            for c in range(self.cols):
                if (r, c) not in self.inbounds:
                    row.append("#")
                elif (r, c) in self.warriors:
                    warrior = self.warriors[(r, c)]
                    warriors.append(warrior)
                    row.append(warrior.band)
                else:
                    row.append(".")
            if warriors:
                row.append("\t")
                row.append(",".join(map(str, warriors)))
            res.append("".join(row))
        return "\n".join(res)

lines = [line[:-1] for line in stdin]

def part1(lines):
    grid = Grid(lines)    
    i = 0
    while grid.move():
        i += 1
    return i * sum(w.hp for w in grid.warriors.values())

def try_with_elves_attack_power(lines, ap):
    grid = Grid(lines)
    for w in grid.warriors.values():
        if w.band == "E":
            w.ap = ap
    total = Counter(w.band for w in grid.warriors.values())["E"]
    
    i = 0
    while grid.move(): 
        i += 1
    c = Counter(w.band for w in grid.warriors.values())
    if c["E"] == total:
        return True, i * sum(w.hp for w in grid.warriors.values())
    return False, None

def part2(lines):
    l, h = 3, 200
    res = None
    while l <= h:
        m = (l + h) >> 1
        poss, out = try_with_elves_attack_power(lines, m)
        if poss:
            res = (m, out)
            h = m - 1
        else:
            l = m + 1
    return res


# p1
print(part1(lines))

# p2
print(part2(lines))
