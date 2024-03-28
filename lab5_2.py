run_results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
               27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

top_best = sorted(run_results, reverse=True)
top_worst = sorted(run_results)

print(f"3 лучших результата: {top_best[0:3]}")
print(f"3 худших результата: {top_worst[0:3]}")
print(f"Результаты начиная с 10: {run_results[9:]}")
