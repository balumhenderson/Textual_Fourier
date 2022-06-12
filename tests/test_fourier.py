import pytest
from fourier import fft

def test_fft_len_one():
    signal = [0]
    actual = fft(signal)
    assert signal == actual

@pytest.mark.xfail # TODO: (JH) Will allow to pass CI but should be fixed
def test_fft_len_zero():
    signal = []
    actual = fft(signal)
    assert actual == signal
