import os
import numpy as np


class InvalidFileTypeError(Exception):
    def __init__(self, message):
        self.message = message


def return_time_data(filename):
    data = None

    try:
        data = np.load(filename)
        return data
    except Exception:
        pass

    try:
        data = np.loadtxt(filename)
        return data
    except Exception:
        raise InvalidFileTypeError(
            f"File: {filename} is neither NumPy .npy-format nor tabular .dat"
        )


def write_data(filename, time, vals):
    data = np.c_[time[:, np.newaxis], vals[:, np.newaxis]]
    name, extension = os.path.splitext(filename)

    if not extension:
        np.save(filename, data)
    else:
        np.savetxt(filename, data)
