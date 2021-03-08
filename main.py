import statistics 

scores = []
first_score = scores.append(int(input()))
second_score = scores.append(int(input()))
third_score = scores.append(int(input()))
mean = statistics.mean(scores)
print(mean)
print("Congratulations, you are accepted!")