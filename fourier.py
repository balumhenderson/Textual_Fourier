import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-poster")

sample_rate = 512
time_step = 1.0 / sample_rate
time_axis = np.arange(0, 1, time_step)


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


def fft(signal):
    """
    A recursive implementation of the 1D Cooley-Tukey FFT.
    The input should have a length which is a power of 2.
    Taken from 'https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.03-Fast-Fourier-Transform.html'
    """
    N = len(signal)

    if N == 1:
        return signal
    else:
        input_even = fft(signal[::2])
        input_odd = fft(signal[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)

        output = np.concatenate(
            [
                input_even + factor[: int(N / 2)] * input_odd,
                input_even + factor[int(N / 2) :] * input_odd,
            ]
        )

    return output


def freqAnalysis(data, sample_rate):
    N = len(data)
    n = np.arange(N)
    T = N / sample_rate
    freq = n / T

    return freq


# Define the input waves
inputs = [
    CosineWave(3, 1, -0.5 * np.pi),
    CosineWave(1, 4, -0.5 * np.pi),
    CosineWave(0.5, 7, -0.5 * np.pi),
]

# Sum the input waves into a single input series
linear_signal = (
    inputs[0].series(time_axis)
    + inputs[1].series(time_axis)
    + inputs[2].series(time_axis)
)

# Fourier transform
output = fft(linear_signal)
frequencies = freqAnalysis(output, sample_rate)
half = len(output) // 2
frequencies_oneside = frequencies[:half]
output_normalised = output[:half] / half


########## Plotting ###########

fig = plt.figure()
ax1 = plt.subplot(321)
ax2 = plt.subplot(323, projection="polar")
ax3 = plt.subplot(325)
ax4 = plt.subplot(326)

inputs[0].plot(ax1, time_axis)
inputs[1].plot(ax1, time_axis)
inputs[2].plot(ax1, time_axis)

ax1.plot(time_axis, linear_signal, label="Input Sum", color="r")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Signal (a.u.)")
ax1.set_title("Linear representation of signal")

ax2.plot(time_axis, linear_signal, color="r")

ax3.stem(frequencies, abs(output), "b", markerfmt=" ", basefmt="-b")
ax3.set_xlabel("Freq (Hz)")
ax3.set_ylabel("FFT Amplitude |X(freq)|")

ax4.stem(frequencies_oneside, abs(output_normalised), "b", markerfmt=" ", basefmt="-b")
ax4.set_xlabel("Freq (Hz)")
ax4.set_ylabel("Normalized FFT Amplitude |X(freq)|")
ax4.set_xlim(0, 50)

print(abs(output_normalised))

plt.show()
