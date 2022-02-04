import sklearn.datasets as datasets
import matplotlib.pyplot as plt

from timeit import default_timer as timer
from datetime import timedelta

from sklearn import preprocessing

from force_scheme import ForceScheme


def main():
    raw = datasets.load_iris(as_frame=True)
    X = raw.data.to_numpy()
    X = preprocessing.StandardScaler().fit_transform(X)

    start = timer()
    y = ForceScheme().fit_transform(X)
    end = timer()

    print('ForceScheme took {0} to execute'.format(timedelta(seconds=end - start)))

    plt.figure()
    plt.scatter(y[:, 0], y[:, 1], c=raw.target,
                cmap='Set1', edgecolors='face', linewidths=0.5, s=4)
    plt.grid(linestyle='dotted')
    plt.show()

    return


if __name__ == "__main__":
    main()
    exit(0)
