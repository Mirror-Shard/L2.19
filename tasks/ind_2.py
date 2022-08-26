#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Разработайте аналог утилиты tree в Linux.
Используйте возможности модуля argparse для управления отображением дерева
каталогов файловой системы. Добавьте дополнительные уникальные возможности в
данный программный продукт.
"""

import argparse
import pathlib


def tree(directory, dir=False, pattern="*", sep="|--"):
    if dir:
        pattern = '.'
    for path in sorted(directory.rglob(pattern)):
        depth = len(path.relative_to(directory).parts)
        spacer = '\t' * depth
        print(spacer + sep + ' ' + path.name)


def main(command_line=None):
    # Основной парсер командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", default=pathlib.Path.cwd())
    parser.add_argument("--dir", type=bool, default=False)
    parser.add_argument("--pattern", type=str, default='*')
    parser.add_argument("--separator", type=str, default="|--")

    # Работа программы
    args = parser.parse_args(command_line)
    filepath = pathlib.Path(args.filepath)
    tree(filepath, args.dir, args.pattern, args.separator)


if __name__ == "__main__":
    main()
