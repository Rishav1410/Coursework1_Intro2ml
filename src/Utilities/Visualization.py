import matplotlib.pyplot as plt
import numpy as np
import os

label_colors = {
    1: (1.0, 0.0, 0.0),    # Red
    2: (0.0, 1.0, 0.0),    # Green
    3: (1.0, 0.75, 0.8),   # Pink
    4: (0.0, 0.0, 1.0)     # Blue
}

# Generates a random color
def generate_random_color():
    return np.random.rand(3,)

def plot_tree(ax, node, label_colors, x_offset=0.5, y_offset=1, y_step=0.05, x_spacing=0.025, depth=0, parent_coords=None, font_size=8, max_depth=10, parent_colors=None):
    # Decide color of the subtree
    if parent_colors is None:
        parent_colors = {}
    if parent_coords not in parent_colors:
        parent_colors[parent_coords] = generate_random_color()
    color = parent_colors[parent_coords]

    if node.is_leaf():
        leaf_color = label_colors.get(node.value, np.random.rand(3,))
        ax.scatter(x_offset, y_offset, s=200, c=[leaf_color], edgecolors='black', zorder=5)
    else:
        ax.text(x_offset, y_offset, f"x{node.feature} <= {node.threshold}", ha='center', va='center', fontsize=font_size, bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3"))
        
        left_x_offset = x_offset - x_spacing / (depth + 1)
        right_x_offset = x_offset + x_spacing / (depth + 1)
        
        if node.left:
            plot_tree(ax, node.left, label_colors, left_x_offset, y_offset - y_step, y_step, x_spacing, depth + 1, (x_offset, y_offset), font_size, max_depth, parent_colors)
        if node.right:
            plot_tree(ax, node.right, label_colors, right_x_offset, y_offset - y_step, y_step, x_spacing, depth + 1, (x_offset, y_offset), font_size, max_depth, parent_colors)
    
    if parent_coords:
        ax.plot([parent_coords[0], x_offset], [parent_coords[1], y_offset], '-', color=color, lw=2)

# Add a legend for the leaf node colors based on labels
def add_legend(ax, label_colors):
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color=color, label=f'Label {label}', markersize=10, markeredgewidth=1.5, markeredgecolor='black')
        for label, color in label_colors.items()
    ]
    ax.legend(handles=legend_elements, loc='upper right', title="Leaf Node Labels")

def save_tree_as_png(root_node, folder="tree_visualizations", filename="decision_tree.png", subtext=""):
    if not os.path.exists(folder):
        os.makedirs(folder)

    fig, ax = plt.subplots(figsize=(44, 20))
    ax.set_axis_off()

    fig.suptitle("Decision Tree | Left: True, Right: False", fontsize=30)
    if subtext != "":
        fig.text(0.5, 0.95, subtext, ha='center', va='top', fontsize=25)
    plot_tree(ax, root_node, label_colors)
    add_legend(ax, label_colors) # For leaf nodes
    
    # Display the tree in the current workspace
    plt.show()

    filepath = os.path.join(folder, filename)
    plt.savefig(filepath, bbox_inches='tight')
    plt.close(fig)
    print(f"Tree visualization saved as: {filepath}")
