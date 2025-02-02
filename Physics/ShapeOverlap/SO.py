import math
import matplotlib.pyplot as plt

class Shape:
    def __init__(self, shape_type, parameters):
        self.shape_type = shape_type
        self.parameters = parameters

    def calculate_overlap(self, other_shape):
        """
        Calculates the overlap between two shapes.
        """
        if self.shape_type == "circle" and other_shape.shape_type == "circle":
            return self.calculate_circle_overlap(other_shape)
        # Add more shape types and their corresponding overlap calculation methods here
        else:
            raise ValueError("Unsupported shape type")

    def calculate_circle_overlap(self, other_circle):
        """
        Calculates the overlap between two circles.
        """
        radius_1 = self.parameters["radius"]
        radius_2 = other_circle.parameters["radius"]
        distance = self.parameters["center"] - other_circle.parameters["center"]

        # Calculate overlap using the circle overlap formula from the previous example
        overlap = calculate_overlap(radius_1, radius_2, distance)
        return overlap


def calculate_overlap(radius_fixed, radius_moving, distance):
    """
    Calculates the overlap between two circles with given radii and distance between their centers.
    """
    distance = abs(distance)
    if distance >= radius_fixed + radius_moving:
        # No overlap if the distance between centers is greater than or equal to the sum of the radii
        return 0
    elif distance <= abs(radius_fixed - radius_moving):
        # Complete overlap if one circle is completely inside the other
        return math.pi * min(radius_fixed, radius_moving) ** 2
    else:
        # Partial overlap
        r1 = radius_fixed
        r2 = radius_moving
        d = distance

        a = r1 ** 2 * math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
        b = r2 ** 2 * math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))
        c = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))

        return a + b - c

# Example usage
shape1 = Shape("circle", {"radius": 5, "center": 0})
shape2 = Shape("circle", {"radius": 7, "center": 0})

default = 10

total_distance = default
iterations = 10
time = 0

time_interval = 0.1
current_distance = -default

# Lists to store time and overlap values for plotting
time_values = []
overlap_values = []

for _ in range(iterations):
    while current_distance <= total_distance:
        shape2.parameters["center"] = current_distance
        overlap = shape1.calculate_overlap(shape2)
        time_values.append(time)
        overlap_values.append(overlap)
        current_distance += time_interval
        time += time_interval

    current_distance = -default

# Plotting the graph
plt.ylim(1, 100)

plt.plot(time_values, overlap_values)
plt.xlabel("Time")
plt.ylabel("Overlap")
plt.title("Overlap of Two Shapes Over Time")
plt.grid(True)

# Saving the graph as an image
plt.savefig("overlap_graph.png")
plt.show()