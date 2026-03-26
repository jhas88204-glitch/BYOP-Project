import numpy as np
import matplotlib.pyplot as plt

# Sample Data (Study Hours vs Marks)
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Plot Graph
plt.figure()
plt.scatter(study_hours, marks, label="Data Points")

# Best Fit Line
m, b = np.polyfit(study_hours, marks, 1)
plt.plot(study_hours, m*study_hours + b, label="Best Fit Line")

# Labels
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Time vs Marks Analysis")
plt.legend()

# Show graph
plt.show()
