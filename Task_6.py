items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return selected_items, total_calories

def dynamic_programming(budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    selected_items = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    item_names = list(items.keys())
    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_cost = items[item_names[i - 1]]['cost']
            item_calories = items[item_names[i - 1]]['calories']
            if item_cost <= w:
                if dp[i - 1][w] < dp[i - 1][w - item_cost] + item_calories:
                    dp[i][w] = dp[i - 1][w - item_cost] + item_calories
                    selected_items[i][w] = selected_items[i - 1][w - item_cost] + [item_names[i - 1]]
                else:
                    dp[i][w] = dp[i - 1][w]
                    selected_items[i][w] = selected_items[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                selected_items[i][w] = selected_items[i - 1][w]

    return selected_items[n][budget], dp[n][budget]

# Введіть бюджет
budget = 100

# Виконання жадібного алгоритму
greedy_items, greedy_calories = greedy_algorithm(budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Сумарна калорійність:", greedy_calories)

# Виконання алгоритму динамічного програмування
dp_items, dp_calories = dynamic_programming(budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_items)
print("Сумарна калорійність:", dp_calories)