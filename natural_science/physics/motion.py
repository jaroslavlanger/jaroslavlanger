import numpy as np

v = velocity = (10., 0.)
a = acceleration = (0., 9.81)
t = time = 10.

def simulate_displacement(velocity, acceleration, time):
    velocity = np.array(velocity)
    acceleration = np.array(acceleration)
    parts = 5
    time_delta = time / parts
    displacement = np.array([0., 0.])
    for _ in range(parts):
        velocity_next = velocity + acceleration * time_delta
        displacement += ((velocity_next + velocity) / 2) * time_delta
        velocity = velocity_next
    return displacement


def calculate_displacement(velocity, acceleration, time):
    velocity = np.array(velocity)
    acceleration = np.array(acceleration)
    return velocity * time + 1/2 * acceleration * time**2,


print(f'{velocity=}, {acceleration=}, {time=}')
print(f'{simulate_displacement(v, a, t)=}m')
print(f'{calculate_displacement(v, a, t)=}m')
