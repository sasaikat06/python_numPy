import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def golden_ratio_model(levels):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')

    # Create a circle
    circle = plt.Circle((0, 0), 1, edgecolor='b', facecolor='none')
    ax.add_patch(circle)

    # Golden ratio
    golden_ratio = (1 + np.sqrt(5)) / 2

    # Plot rectangles based on the golden ratio
    width, height = 1, 1 / golden_ratio
    for _ in range(levels):
        rect = Rectangle((-width / 2, -height / 2), width, height, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        width, height = height, height / golden_ratio

    plt.title('Golden Ratio Model in a Circle')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    golden_ratio_model(levels=10)
