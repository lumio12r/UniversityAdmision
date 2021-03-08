import statistics 

scores = []
first_score = scores.append(int(input()))
second_score = scores.append(int(input()))
third_score = scores.append(int(input()))
mean = statistics.mean(scores)
print(mean)
if mean >= 60.00:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")