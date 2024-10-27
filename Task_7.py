import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Встановимо кількість симуляцій (кидань кубиків)
num_simulations = 1000000

# Імітація кидків двох кубиків
dice1 = np.random.randint(1, 7, num_simulations)
dice2 = np.random.randint(1, 7, num_simulations)
sums = dice1 + dice2

# Підрахунок кількості появ кожної суми
sum_counts = {i: np.count_nonzero(sums == i) for i in range(2, 13)}

# Розрахунок ймовірностей для кожної суми
monte_carlo_probabilities = {k: v / num_simulations * 100 for k, v in sum_counts.items()}

# Теоретичні ймовірності з таблиці
theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Створення таблиці результатів
results_df = pd.DataFrame({
    'Sum': list(monte_carlo_probabilities.keys()),
    'Monte Carlo Probability (%)': list(monte_carlo_probabilities.values()),
    'Theoretical Probability (%)': list(theoretical_probabilities.values())
})

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(results_df['Sum'] - 0.2, results_df['Monte Carlo Probability (%)'], width=0.4, label="Monte Carlo")
plt.bar(results_df['Sum'] + 0.2, results_df['Theoretical Probability (%)'], width=0.4, label="Theoretical")
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability (%)")
plt.title("Comparison of Monte Carlo and Theoretical Probabilities for Dice Sums")
plt.legend()
plt.xticks(range(2, 13))
plt.show()
