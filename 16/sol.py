from operator import imul, add, and_, or_, gt, eq
from functools import partial
from sys import stdin
import re
from heapq import heappush, heappop
from collections import deque


def oprr(regs, op, a, b, c):
    return regs[:c] + (op(regs[a], regs[b]), ) + regs[c + 1:]
    
def opri(regs, op, a, b, c):
    return regs[:c] + (op(regs[a], b), ) + regs[c + 1:]

def opir(regs, op, a, b, c):
    return regs[:c] + (op(a, regs[b]), ) + regs[c + 1:]

def setr(regs, a, b, c):
    return regs[:c] + (regs[a], ) + regs[c + 1:]

def seti(regs, a, b, c):
    return regs[:c] + (a, ) + regs[c + 1:]

# all possible opcodes
opcodes = [
    # addr
    lambda regs, a, b, c: oprr(regs, add, a, b, c),
    # addi
    lambda regs, a, b, c: opri(regs, add, a, b, c),

    # mulr
    lambda regs, a, b, c: oprr(regs, imul, a, b, c),
    # muli
    lambda regs, a, b, c: opri(regs, imul, a, b, c),

    # banr
    lambda regs, a, b, c: oprr(regs, and_, a, b, c),
    # bani
    lambda regs, a, b, c: opri(regs, and_, a, b, c),

    # borr
    lambda regs, a, b, c: oprr(regs, or_, a, b, c),
    # bori
    lambda regs, a, b, c: opri(regs, or_, a, b, c),

    # setr
    setr,
    # seti
    seti,

    # gtir
    lambda regs, a, b, c: opir(regs, gt, a, b, c),
    # gtri
    lambda regs, a, b, c: opri(regs, gt, a, b, c),
    # gtrr
    lambda regs, a, b, c: oprr(regs, gt, a, b, c),

    # eqir
    lambda regs, a, b, c: opir(regs, eq, a, b, c),
    # eqri
    lambda regs, a, b, c: opri(regs, eq, a, b, c),
    # eqrr
    lambda regs, a, b, c: oprr(regs, eq, a, b, c)
]

def parse_line(line, regex):
    state = next(re.finditer(regex, line)).groups()
    return tuple(map(int, state))

def parse(sample):
    lines = sample.splitlines()
    state_regex = r'\[(\d+), (\d+), (\d+), (\d+)\]'
    opcode_regex = r'(\d+) (\d+) (\d+) (\d+)'
    before = parse_line(lines[0], state_regex)
    after = parse_line(lines[-1], state_regex)
    opcode = parse_line(lines[1], opcode_regex)
    return before, after, opcode

def filter_opcodes(opcodes, before, after, opcode):
    for i in range(len(opcodes)):
        f = opcodes[i]
        if f(before, *opcode[1:]) == after:
            yield i

def decode_opcode_number(opcodes, samples):
    poss = [set(range(len(opcodes))) for _ in range(len(opcodes))]
    for bef, aft, opcode in samples:
        poss_opcodes = set(filter_opcodes(opcodes, bef, aft, opcode))
        poss[opcode[0]] = poss[opcode[0]] & poss_opcodes
        poss_opcodes = set(filter_opcodes(opcodes, bef, aft, opcode))
    q = deque([i for i in range(len(poss)) if len(poss[i]) == 1])
    done = {i for i in q}
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            for i in range(len(poss)):
                if i != n:
                    poss[i] = poss[i] - poss[n]
                if i not in done and len(poss[i]) == 1:
                    q.append(i)
                    done.add(i)
    return [p.pop() for p in poss]

def part1(opcodes, samples):
    res = 0
    for bef, aft, opcode in samples:
        poss = list(filter_opcodes(opcodes, bef, aft, opcode))
        if len(poss) >= 3:
            res += 1            
    return res

def step(regs, opcodes, instruction):
    num, rest = instruction[0], instruction[1:]
    return opcodes[num](regs, *rest)

def steps(regs, opcodes, instructions):
    for instr in instructions:
        regs = step(regs, opcodes, instr)
    return regs

def part2(opcodes, samples, instructions):
    correct = decode_opcode_number(opcodes, samples)
    opcodes = [opcodes[i] for i in correct]
    regs = tuple(0 for _ in range(NUM_REGISTERS))
    return steps(regs, opcodes, instructions)

NUM_REGISTERS = 4
samples_txt, instructions_txt = "".join(stdin).split("\n\n\n\n")
samples = [parse(sample) for sample in samples_txt.split("\n\n")]
instructions = [parse_line(line, r'(\d+) (\d+) (\d+) (\d+)') for line in instructions_txt.splitlines()]

print(part1(opcodes, samples))
print(part2(opcodes, samples, instructions)[0])

