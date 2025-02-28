#Point Clipping in Computer Graphics
import matplotlib.pyplot as plt
def point_clipping(points, window):
    # Extract window coordinates
    x_min, y_min, x_max, y_max = window
    
    # Create lists to store clipped and discarded points
    clipped_points = []
    discarded_points = []

    for point in points:
        x, y = point
        
        # Check the conditions for point clipping
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            # Point is inside the clipping window
            clipped_points.append(point)
        else:
            # Point is outside the clipping window
            discarded_points.append(point)

    return clipped_points, discarded_points

# Example usage
if __name__ == "__main__":
    # Input points to be clipped (you can add more points here)
    points = [
        (50, 50),
        (150, 150),
        (200, 200),
        (30, 30),
        (100, 100),
        (75, 75),
        (180, 60)
    ]
    
    # Coordinates of the clipping window (x_min, y_min, x_max, y_max)
    window = (40, 40, 160, 160)
    
    # Perform point clipping
    clipped_points, discarded_points = point_clipping(points, window)
    
    # Display the clipped and discarded points
    print("Clipped Points:", clipped_points)
    print("Discarded Points:", discarded_points)

    # Plotting
    plt.figure(figsize=(8, 8))

    # Plot the clipping window
    plt.plot([window[0], window[0], window[2], window[2], window[0]], 
             [window[1], window[3], window[3], window[1], window[1]], color='black', linewidth=2, label='Clipping Window')

    # Label clipping window corners
    window_corners = [(window[0], window[1]), (window[0], window[3]),
                      (window[2], window[3]), (window[2], window[1])]
    
    for corner in window_corners:
        plt.scatter(*corner, color='blue', s=100, marker='s', label='Clipping Window Corners')
        plt.text(corner[0] + 2, corner[1] + 2, f'{corner}', fontsize=9, color='blue')

    # Plot clipped points
    if clipped_points:
        x_clipped, y_clipped = zip(*clipped_points)
        plt.scatter(x_clipped, y_clipped, color='green', label='Clipped Points', s=100, marker='o')
        for point in clipped_points:
            plt.text(point[0] + 2, point[1] + 2, f'{point}', fontsize=9, color='black')

    # Plot discarded points
    if discarded_points:
        x_discarded, y_discarded = zip(*discarded_points)
        plt.scatter(x_discarded, y_discarded, color='red', label='Discarded Points', s=100, marker='x')
        for point in discarded_points:
            plt.text(point[0] + 2, point[1] + 2, f'{point}', fontsize=9, color='black')

    # Labels and legend
    plt.xlim(0, 250)
    plt.ylim(0, 250)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.title('Point Clipping Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
