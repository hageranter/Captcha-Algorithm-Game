import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
from PIL import Image
import numpy as np
import os

# Sample data: Categories and their corresponding image URLs (multiple URLs per category)
images = [
    {"url": "lOIP - Copy - Copy.jpeg", "category": "Car"},
    {"url": "lOIP - Copy - Copy.jpeg", "category": "Car"},
    {"url": "lOIP - Copy - Copy.jpeg", "category": "Car"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "Tree"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "Tree"},
    {"url": "R - Copy (2) - Copy.jpeg", "category": "Tree"},
    {"url": "hi - Copy - Copy.jpg", "category": "Building"},
    {"url": "hi - Copy - Copy.jpg", "category": "Building"},
    {"url": "hi - Copy - Copy.jpg", "category": "Building"},
    ]

# Create categories dictionary with multiple URLs for each category
categories = {}
for image in images:
    category = image["category"]
    if category not in categories:
        categories[category] = []  # Initialize an empty list for each category
    categories[category].append(image["url"])

# Generate a grid of random images with their corresponding labels
grid_size = 2 # 4x4 grid
grid_labels = []
grid_objects = []
target_category = random.choice(list(categories.keys()))  # Randomly choose a target category

# Populate grid with random categories and objects
for _ in range(grid_size ** 2):
    category = random.choice(list(categories.keys()))
    icon = random.choice(categories[category])  # Select a random URL from the category's list
    grid_labels.append(category)
    grid_objects.append(icon)

# Record correct answers for the target category
correct_indices = [i for i, label in enumerate(grid_labels) if label == target_category]

# Visualization function
def display_grid():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.axis("off")
    selected = []

    # Display grid with images
    for i in range(grid_size):
        for j in range(grid_size):
            idx = i * grid_size + j
            # Open the image from the file path
            img_path = grid_objects[idx]
            
            # Check if the image exists
            if not os.path.exists(img_path):
                print(f"Error: Image not found at {img_path}")
                continue  # Skip this image if not found

            try:
                img = Image.open(img_path)
                img = img.resize((100, 100))  # Resize to fit grid (adjust size as needed)
                ax.imshow(np.array(img), extent=[j, j + 1, grid_size - i - 1, grid_size - i])  # Display the image
                ax.add_patch(
                    patches.Rectangle(
                        (j, grid_size - i - 1),
                        1,
                        1,
                        edgecolor="black",
                        facecolor="none",  # Make the rectangle transparent
                    )
                )
            except Exception as e:
                print(f"Error loading image at {img_path}: {e}")

    # Button callback for validation
    def validate(event):
        if sorted(selected) == sorted(correct_indices):
            print("Correct! 🎉")
            ax.set_facecolor('green')  # Change background to green on success
        else:
            print("Incorrect. Try Again!")
            ax.set_facecolor('red')  # Change background to red on failure
        plt.draw()

    # Button callback for selecting squares
    def on_click(event):
        if event.inaxes == ax:
            x, y = int(event.xdata), int(grid_size - event.ydata - 1)
            idx = y * grid_size + x
            
            # Toggle selection on left click (button 1)
            if event.button == 1:  # Left click
                if idx not in selected:
                    selected.append(idx)
                    ax.add_patch(
                        patches.Rectangle(
                            (x, grid_size - y - 1),
                            1,
                            1,
                            edgecolor="green",
                            facecolor="none",
                            linewidth=2,
                        )
                    )
                else:
                    selected.remove(idx)
                    ax.add_patch(
                        patches.Rectangle(
                            (x, grid_size - y - 1),
                            1,
                            1,
                            edgecolor="black",
                            facecolor="none",
                        )
                    )
                plt.draw()

    # Add validate button
    validate_ax = plt.axes([0.8, 0.05, 0.1, 0.075])
    validate_button = Button(validate_ax, "Check")
    validate_button.on_clicked(validate)

    # Display instructions
    plt.figtext(0.5, 0.95, f"Select all {target_category}s!", ha="center", fontsize=14, color='purple')
    plt.figtext(0.5, 0.9, "Click on the grid cells to select your answers", ha="center", fontsize=12)

    # Connect the click event
    cid = fig.canvas.mpl_connect("button_press_event", on_click)

    # Show the grid
    plt.show()

# Run the visualization
display_grid()