#!/usr/bin/env python3
# -*- coding: utf-8 -*-і
"""
Лабораторна робота 3.1 - Дослідження роботи з файлами та проектування зв'язків між сутностями
Автор: Сорочан Ярослав
Група: Б-121-24-3-ПІ
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from console_interface import ConsoleMenu


def main():
    """Головна функція програми"""
    try:
        print("=" * 60)
        print("ЛАБОРАТОРНА РОБОТА 3.1")
        print("Дослідження роботи з файлами та проектування зв'язків між сутностями")
        print("=" * 60)
        print("Завдання: Обчислити кількість студентів 4-го курсу,")
        print("які не отримують стипендії. Отримати їх дані з файлу.")
        print("=" * 60)

        # Створюємо та запускаємо консольне меню
        menu = ConsoleMenu()
        menu.show_main_menu()

    except KeyboardInterrupt:
        print("\n\nПрограма перервана користувачем.")
    except Exception as e:
        print(f"\nПомилка виконання програми: {e}")
        print("Зверніться до розробника або перевірте вхідні дані.")
    finally:
        print("Програма завершена.")


if __name__ == "__main__":
    main()
