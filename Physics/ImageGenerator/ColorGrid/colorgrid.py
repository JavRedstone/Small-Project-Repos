from PIL import Image, ImageDraw
import random

def generate_grid_image(rect_width, rect_height, grid_width, grid_height, colors, output_path):
    image_width = grid_width * rect_width
    image_height = grid_height * rect_height

    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    for i in range(grid_width):
        for j in range(grid_height):
            x = i * rect_width
            y = j * rect_height

            color1 = random.choice(colors)
            colors.remove(color1)  # Remove the chosen color from the available options

            color2 = random.choice(colors)

            # Draw a smooth gradient within each square
            for k in range(rect_width):
                for l in range(rect_height):
                    ratio_x = k / rect_width
                    ratio_y = l / rect_height

                    r = int((1 - ratio_x) * int(color1[1:3], 16) + ratio_x * int(color2[1:3], 16))
                    g = int((1 - ratio_y) * int(color1[3:5], 16) + ratio_y * int(color2[3:5], 16))
                    b = int((1 - ratio_x) * int(color1[5:], 16) + ratio_x * int(color2[5:], 16))

                    blended_color = (r, g, b)
                    draw.point((x + k, y + l), fill=blended_color)

            colors.append(color1)  # Add back the chosen color to the available options

    image.save(output_path, "PNG")
    print(f"Image saved to: {output_path}")

# Example usage
rect_width = 25
rect_height = 25
grid_width = 120
grid_height = 60
# colors = ["#82B1FF", "#448AFF", "#2979FF", "#FFE57F", "#FFD740", "#FFC400"]  # List of hex colors
# colors = ["#64b5f6", "#81c784", "#f44336", "#ffeb3b", "#ff9800", "#9e9e9e",]
# colors = ["#E91E63", "#AD1457", "#F48FB1", "#2196F3", "#1565C0", "#90CAF9"]
colors = ["#FFB74D", "#FF8A65", "#FFCC80", "#FB8C00", "#FFE0B2", "#64B5F6", "#1976D2", "#90CAF9", "#0D47A1", "#BBDEFB"]
output_path = "grid_image.png"

generate_grid_image(rect_width, rect_height, grid_width, grid_height, colors, output_path)
