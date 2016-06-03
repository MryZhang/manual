#!/usr/bin/env python

import json
import sys
import re

from pandocfilters import toJSONFilter, Header, Str, RawBlock, RawInline, Image

# This file fixes cross-references when building Sphinx documentation
# from the manual's .tex files.

def rb(x):
  return RawBlock('rst', x)

def mk_ref(x):
  return RawInline('rst', ":ref:`" + x + "`")

def behead(key, value, format, meta):
  # pandoc does not emit labels before sections -> insert
  if key == 'Header':
    lbl = value[1][0]
    if lbl:
      new_lbl = ".. _" + lbl + ":\n\n"
      value[1][0] = ""
      return [rb(new_lbl), Header(value[0], value[1], value[2])]
  # pandoc generates [refname] as strings for \ref{refname} -> fix
  elif key == 'Str':
    if len(value) > 3:
      if value[0] == '[':
        return mk_ref(value[1:-1])
      elif value[1] == '[':
        return mk_ref(value[2:-1])
  # images don't have file endings in .tex -> add .png
  elif key == 'Image':
    return Image(value[0], value[1], [value[2][0] + ".png", value[2][1]])

if __name__ == "__main__":
  toJSONFilter(behead)

