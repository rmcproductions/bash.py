def norm_file_size(file):
    if file / 1e+6 <= 1000 and file / 1e+3 < 100000:
        return str(round(file / 1e+3)) + "kB"
    elif file / 1e+6 >= 1000:
        return str(round(file / 1e+9)) + "GB"
    else:
        return str(round(file / 1e+6)) + "MB"
