import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
marks = [88, 76, 90, 69, 84]

# Pie Chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# Bar Chart
plt.bar(subjects, marks, color="orange")
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()