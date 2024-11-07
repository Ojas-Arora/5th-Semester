import matplotlib.pyplot as plt
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000
def compute_outcode(x, y, window):
    x_min, y_min, x_max, y_max = window
    code = INSIDE
    
    if x < x_min: 
        code |= LEFT
    elif x > x_max:  
        code |= RIGHT
    if y < y_min:  
        code |= BOTTOM
    elif y > y_max:  
        code |= TOP
    
    return code
def cohen_sutherland_line_clip(line, window):
    x_min, y_min, x_max, y_max = window
    (x0, y0), (x1, y1) = line
    
    outcode0 = compute_outcode(x0, y0, window)
    outcode1 = compute_outcode(x1, y1, window)
    accept = False
    clipped = False  
    
    while True:
        if outcode0 == 0 and outcode1 == 0:  
            accept = True
            break
        elif (outcode0 & outcode1) != 0:  
            break
        else:
            x, y = 0, 0
            outcode_out = outcode0 if outcode0 != 0 else outcode1
            clipped = True  
            
            if outcode_out & TOP:  
                x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif outcode_out & BOTTOM:  
                x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            elif outcode_out & RIGHT:  
                y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif outcode_out & LEFT: 
                y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min
            
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0, window)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, window)
    
    if accept:
        if clipped:
            return "partially", [(x0, y0), (x1, y1)], line  
        else:
            return "inside", [(x0, y0), (x1, y1)], line
    else:
        return "outside", line, line  

if __name__ == "__main__":
    lines = [
        [(10, 10), (200, 200)],
        [(50, 150), (150, 50)],
        [(30, 200), (130, 100)],
        [(160, 160), (180, 180)],
        [(70, 80), (90, 120)]
    ]
    
    window = (40, 40, 160, 160)
    
    inside_lines = []
    partially_clipped_lines = []
    outside_lines = []

    for line in lines:
        category, clipped_line, original_line = cohen_sutherland_line_clip(line, window)
        if category == "inside":
            inside_lines.append(line)
        elif category == "partially":
            partially_clipped_lines.append((clipped_line, original_line))
        elif category == "outside":
            outside_lines.append(line)

    print("Inside Lines:", inside_lines)
    print("Partially Clipped Lines:", partially_clipped_lines)
    print("Outside Lines:", outside_lines)

    plt.figure(figsize=(8, 8))

    plt.plot([window[0], window[0], window[2], window[2], window[0]], 
             [window[1], window[3], window[3], window[1], window[1]], color='black', linewidth=2, label='Clipping Window')

    for line in inside_lines:
        (x0, y0), (x1, y1) = line
        plt.plot([x0, x1], [y0, y1], color='green', linewidth=2, marker='o', label='Inside Line' if line == inside_lines[0] else "")
        plt.text(x0, y0, f'({x0}, {y0})', fontsize=9, color='black')
        plt.text(x1, y1, f'({x1}, {y1})', fontsize=9, color='black')

    for clipped_line, original_line in partially_clipped_lines:
        (ox0, oy0), (ox1, oy1) = original_line
        plt.plot([ox0, ox1], [oy0, oy1], color='gray', linewidth=1, linestyle='--', marker='x', label='Original Line' if original_line == partially_clipped_lines[0][1] else "")
        plt.text(ox0, oy0, f'({ox0}, {oy0})', fontsize=9, color='black')
        plt.text(ox1, oy1, f'({ox1}, {oy1})', fontsize=9, color='black')
        (x0, y0), (x1, y1) = clipped_line
        plt.plot([x0, x1], [y0, y1], color='blue', linewidth=2, marker='s', label='Clipped Line' if clipped_line == partially_clipped_lines[0][0] else "")
        plt.text(x0, y0, f'({x0:.0f}, {y0:.0f})', fontsize=9, color='black')
        plt.text(x1, y1, f'({x1:.0f}, {y1:.0f})', fontsize=9, color='black')

    for line in outside_lines:
        (x0, y0), (x1, y1) = line
        plt.plot([x0, x1], [y0, y1], color='red', linewidth=2, linestyle=':', marker='x', label='Outside Line' if line == outside_lines[0] else "")
        plt.text(x0, y0, f'({x0}, {y0})', fontsize=9, color='black')
        plt.text(x1, y1, f'({x1}, {y1})', fontsize=9, color='black')

    plt.xlim(0, 250)
    plt.ylim(0, 250)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.title('Line Clipping Visualization (Cohen-Sutherland Algorithm)')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
