import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt


def get_spectral_lines(time_points, dipole_moment, stop_laser=0):
    mask = time_points >= stop_laser

    dt = time_points[1] - time_points[0]

    freq = (
        scipy.fftpack.fftshift(scipy.fftpack.fftfreq(len(time_points[mask])))
        * 2
        * np.pi
        / dt
    )
    a = np.abs(scipy.fftpack.fftshift(scipy.fftpack.fft(dipole_moment[mask])))

    a /= a.max()

    return freq, a


def plot_spectral_lines(freq, a, xlim=(None, None)):
    plt.plot(freq, a)
    plt.xlim(*xlim)
    plt.show()
