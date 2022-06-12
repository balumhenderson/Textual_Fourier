import numpy as np
import signalGenerator as sg


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


if __name__ == "__main__":
    linear_signal, input_waves = sg.signalGenerator(time_axis)

    # Fourier transform
    output = fft(linear_signal)
    frequencies = freqAnalysis(output, sample_rate)
    half = len(output) // 2
    frequencies_oneside = frequencies[:half]
    output_normalised = output[:half] / half

    # %% ####### Plotting ###########
    # TODO: Get rid of executable code from main file
    import plotext as plo

    plo.subplots(3, 1)
    plo.plotsize(100, 100)

    plo.subplot(1, 1)
    plo.scatter(time_axis, linear_signal)
    plo.xlabel("Time (s)")
    plo.ylabel("Signal (a.u.)")
    plo.title("Random Signal")
    plo.xticks([0.2 * i for i in range(5)])
    plo.yticks([4 * i for i in range(-4, 5)])

    plo.subplot(2, 1)

    plo.plot(frequencies_oneside, abs(output_normalised))
    plo.xlim(0, 10)
    plo.xlabel("Frequency (Hz)")
    plo.ylabel("Normalised Amplitude (a.u.)")
    plo.title("FFT Results")
    plo.xticks([2 * i for i in range(8)])
    plo.yticks([2 * i for i in range(6)])

    plo.subplot(3, 1)

    plo.show()
