# Advent of code 2020 / haskell

This directory contains a utility script and my solutions for [advent of code](adventofcode.com)

Please don't use the solutions.

#### How to use `run` (again)

`./run` is a shell script that will download your input for the day, build the executable from haskell, and run it.
Usage: `./run <day>`, where `<day>` is the day you want to run the solution for.

##### Requirements
To use `run`, you need:
- make
- a shell
- ghc, the Glasgow Haskell Compiler
- a file named `.env` that contains a line of the format `export COOKIE='session=...'` (see `utils.run`)
