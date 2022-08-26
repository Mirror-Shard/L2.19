#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Для своего варианта лабораторной работы 2.17 добавьте возможность хранения файла данных
в домашнем каталоге пользователя. Для выполнения операций с файлами необходимо
использовать модуль pathlib.
"""

import pathlib
import json
import argparse


# Создаёт словарь "студент" и возвращает его
def get_student(name, group, average_estimation):
    # Создать словарь.
    return {
        'name': name,
        'group': group,
        'average_estimation': average_estimation,
    }


# Выводит список студентов
def show_list(staff):
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Ф.И.О.",
                "Группа",
                "Средняя оценка"
            )
        )
        print(line)
        # Вывести данные о всех студентах.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('average_estimation', 0)
                )
            )
        print(line)
    else:
        print("Список пуст")


# Выводит справку о работе с программой
def show_help():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


# Сохраняет данные в файл
def save_students(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=3)


# Читает данные из файла
def load_students(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        file = json.load(fin)
        return file


def main(command_line=None):
    # Парсер для определения имени файла
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The data file name"
    )

    # Основной парсер командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", type=bool, default=False)
    subparsers = parser.add_subparsers(dest="command")

    # Субпарсер для добавления студента
    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new student"
    )
    add.add_argument(
        "-n",
        "--name",
        help="The student`s name"
    )
    add.add_argument(
        "-g",
        "--group",
        help="The student`s group"
    )
    add.add_argument(
        "-ae",
        "--average_estimation",
        help="The student`s average estimation"
    )

    # Субпрасер показывающий список студентов
    subparsers.add_parser(
        "list",
        parents=[file_parser],
        help="Show list of student`s"
    )

    # Работа программы
    args = parser.parse_args(command_line)
    if args.home:
        filename = pathlib.Path.home() / args.filename
    else:
        filename = pathlib.Path.cwd() / args.filename

    is_dirty = False
    if pathlib.Path.exists(filename):
        students = load_students(filename)
    else:
        students = []

    if args.command == "add":
        student = get_student(args.name, args.group, args.average_estimation)
        students.append(student)
        is_dirty = True
    elif args.command == "list":
        show_list(students)
    else:
        print("Неизвестная команда!")

    if is_dirty:
        save_students(filename, students)


if __name__ == '__main__':
    main()
