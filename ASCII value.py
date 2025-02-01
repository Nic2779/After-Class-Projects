def find_x(val, xdata, ydata):
    x = np.where(ydata==val)
    return int(xdata[x])