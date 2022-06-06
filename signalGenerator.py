import numpy.random as rand
import numpy as np


class CosineWave:
    def __init__(self, frequency=1, amplitude=1, phase=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase

    def describe(self):
        print(
            f"The frequency of this wave is {self.frequency}, it's amplitude is {self.amplitude} and it has a phase of {self.phase} radians."
        )

    def series(self, time_axis):
        return self.amplitude * np.cos(
            2 * np.pi * self.frequency * time_axis + self.phase
        )

    def plot(self, ax, time_axis, label=None, color="b"):
        ax.plot(time_axis, self.series(time_axis), label=label, color=color, lw=0.8)


def randWave():
    frequency, amplitude, phase = (
        10 * rand.random(),
        rand.randint(1, 5),
        2 * np.pi * rand.random(),
    )
    return CosineWave(frequency, amplitude, phase)


def signalGenerator(time_axis):
    number_of_waves = rand.randint(2, 8)
    waves = []
    signal = np.zeros_like(time_axis)
    for i in range(number_of_waves):
        wave = randWave()
        wave.describe()
        waves.append(wave)
        signal += wave.series(time_axis)

    return signal, waves
