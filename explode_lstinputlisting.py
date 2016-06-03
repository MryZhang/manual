#!/usr/bin/env python

# This script demystifies C++ compiler output for CAF by
# replacing cryptic `typed_mpi<...>` templates with
# `replies_to<...>::with<...>` and `atom_constant<...>`
# with human-readable representation of the actual atom.

import sys
import re

def parse_range(astr):
  result = set()
  for part in astr.split(','):
    x = part.split('-')
    result.update(range(int(x[0]), int(x[-1]) + 1))
  return sorted(result)

def print_selected(fname, line_nums):
  with open(fname) as mfile:
    for num, line in enumerate(mfile, 1):
      if num in line_nums:
        sys.stdout.write(line)

def print_entire_file(fname):
  with open(fname, 'r') as fin:
    sys.stdout.write(fin.read())

for line in sys.stdin:
  rx = re.compile(r"\\lstinputlisting(\[.+\])?{(.+)}")
  linerange_rx = re.compile(r".*linerange={(.+)}.*")
  needle = "\lstinputlisting"
  idx = line.find(needle)
  if idx == -1:
    sys.stdout.write(line)
  else:
    m = rx.match(line)
    if not m:
      continue
    print r"\begin{lstlisting}"
    if not m.group(1):
      print_entire_file(m.group(2))
    else:
      m2 = linerange_rx.match(m.group(1))
      if not m2 or not m2.group(1):
        print_entire_file(m.group(2))
      else:
        line_range = parse_range(m2.group(1))
        print_selected(m.group(2), line_range)
    print r"\end{lstlisting}"

