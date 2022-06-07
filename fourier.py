import numpy as np
import matplotlib.pyplot as plt
import signalGenerator as sg

plt.style.use("seaborn-poster")

sample_rate = 512
time_step = 1.0 / sample_rate
time_axis = np.arange(0, 1, time_step)


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


linear_signal, input_waves = sg.signalGenerator(time_axis)

# Fourier transform
output = fft(linear_signal)
frequencies = freqAnalysis(output, sample_rate)
half = len(output) // 2
frequencies_oneside = frequencies[:half]
output_normalised = output[:half] / half


########## Plotting ###########

fig = plt.figure()
ax1 = plt.subplot(321)
ax2 = plt.subplot(322, projection="polar")
ax3 = plt.subplot(325)
ax4 = plt.subplot(326)

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
ax4.set_xlim(0, 12)

plt.show()
