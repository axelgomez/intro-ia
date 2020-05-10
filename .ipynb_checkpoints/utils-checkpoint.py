def graficar(ax, datox, datoy, param_dicc):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    datox : array
       The x data

    datoy : array
       The y data

    param_dicc : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(datox, datoy, **param_dicc)
    return out