#!/bin/bash

# Запрос данных у пользователя
read -p "Введите ваше имя: " NAME
read -p "Введите год вашего рождения: " BIRTH_YEAR
readonly CURRENT_YEAR=2026  # Защищаем от изменения

# Расчет возраста
AGE=$((CURRENT_YEAR - BIRTH_YEAR))

# Вывод результата
echo "Пользователь $NAME родился в $BIRTH_YEAR году, текущий возраст — $AGE лет."