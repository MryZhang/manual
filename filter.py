#!/usr/bin/env python

import json
import sys
import re

from pandocfilters import toJSONFilter, Header, Str, RawBlock, RawInline, Image, Space

# This file fixes cross-references when building Sphinx documentation
# from the manual's .tex files.

def rb(x):
  return RawBlock('rst', x)

def mk_ref(x):
  return RawInline('rst', ":ref:`" + x + "`")

last_element = ('', '')

def store(key, value):
  global last_element
  last_element = (key, value)

def behead(key, value, format, meta):
  global last_element
  # pandoc does not emit labels before sections -> insert
  if key == 'Header':
    lbl = value[1][0]
    if lbl:
      new_lbl = ".. _" + lbl + ":\n\n"
      value[1][0] = ""
      store(key, value)
      return [rb(new_lbl), Header(value[0], value[1], value[2])]
  # fix two bugs with string parsing
  elif key == 'Str':
    # pandoc does not parse \xpsace correctly -> insert whitespace after CAF
    if last_element == ('Str', 'CAF') and value.isalnum():
      store(key, value)
      return [Space(), Str(value)]
    if len(value) > 3:
      # pandoc generates [refname] as strings for \ref{refname} -> fix
      if value[0] == '[':
        store(key, value)
        return mk_ref(value[1:-1])
      elif value[1] == '[':
        store(key, value)
        return mk_ref(value[2:-1])
  # images don't have file endings in .tex -> add .png
  elif key == 'Image':
    store(key, value)
    return Image(value[0], value[1], [value[2][0] + ".png", value[2][1]])
  store(key, value)

if __name__ == "__main__":
  toJSONFilter(behead)

