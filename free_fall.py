GRAVITY = 9.81 # m/s^2


def kinetic_energy(mass: float, velocity: float) -> float:
    '''Return the kinetic energy in joules.'''
    return 0.5 * mass * velocity ** 2
def fall_speed(time: float) -> float:
    '''Return the speed of a freely falling object after 'time' seconds.'''
    return GRAVITY * time

speed = fall_speed(2.0)
energy = kinetic_energy(1.0, speed)
print(speed)
print(energy)