name = "Чанг"
group = "4731204/50001"
score = 5
print(f"Студент {name} из группы {group} получил {score} баллов")

f = open("result.txt", "w", encoding="utf-8")
print("Результаты работы", file=f)
f.close()