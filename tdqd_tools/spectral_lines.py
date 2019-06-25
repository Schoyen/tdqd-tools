import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt


def get_spectral_lines(
    time_points, dipole_moment, stop_laser=0, xlim=(None, None)
):
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

    lower_bound = xlim[0] if xlim[0] is not None else np.min(freq)
    upper_bound = xlim[1] if xlim[1] is not None else np.max(freq)

    mask = (freq >= lower_bound) & (freq <= upper_bound)

    return freq[mask], a[mask]


def plot_spectral_lines(freq, a):
    plt.plot(freq, a)
    plt.show()
