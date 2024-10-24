def grafica_pro(data, ancho, altura):
    plt.rc('font', size=14)
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=14)
    plt.rc('xtick', labelsize=10)
    plt.rc('ytick', labelsize=10)
    data.hist(bins=50, figsize=(ancho, altura))
    plt.show()
