#!/bin/bash
FILE_PATH="config.txt"
if [ -f "$FILE_PATH" ]; then
    sed -i 's/\bname\b/user_name/g' "$FILE_PATH"
    echo "Замена успешно выполнена"
else
    echo "Ошибка: Файл не найден."
fi
