
scores = [54,65,85,95,65,45,68,52,65,32,95,70]

maxScore = -254645

for score in scores:
    if score > maxScore:
        maxScore=score

print(f"The highest score you got : {maxScore}")
