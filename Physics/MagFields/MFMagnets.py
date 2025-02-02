import numpy as np
from mayavi import mlab

def calculate_magnetic_field(position, magnets):
    """Calculate the magnetic field at a given position due to magnets."""
    magnetic_field = np.zeros(3)
    for magnet in magnets:
        r = position - magnet['position']
        magnitude = magnet['strength'] / np.linalg.norm(r)**3
        magnetic_field += 1e-7 * magnitude * np.cross(magnet['moment'], r)
    return magnetic_field

def plot_magnetic_field(magnets):
    """Generate a 3D plot of the magnetic field produced by magnets."""
    # Create a grid of points where the magnetic field will be calculated
    x, y, z = np.mgrid[-20:21:0.5, -20:21:0.5, -20:21:0.5]
    positions = np.vstack((x.ravel(), y.ravel(), z.ravel())).T

    # Calculate the magnetic field at each point
    magnetic_fields = [calculate_magnetic_field(position, magnets) for position in positions]

    # Reshape the magnetic field values to match the grid shape
    Bx = np.array(magnetic_fields)[:, 0].reshape(x.shape)
    By = np.array(magnetic_fields)[:, 1].reshape(x.shape)
    Bz = np.array(magnetic_fields)[:, 2].reshape(x.shape)

    # Create the 3D plot
    mlab.figure(bgcolor=(1, 1, 1))
    mlab.quiver3d(x, y, z, Bx, By, Bz, color=(0, 0, 1))
    mlab.axes()
    mlab.show()

# Define the magnets with their positions, strengths, and magnetic moments
magnets = [
    {'position': np.array([0, 0, 0]), 'strength': 1, 'moment': np.array([0, 0, 1])},
    {'position': np.array([5, 0, 0]), 'strength': 1, 'moment': np.array([0, 0, -1])}
]

# Generate the 3D plot of the magnetic field
plot_magnetic_field(magnets)
