import pickle
from matplotlib import pyplot as plt
import os


def plot_loss(dict_path):
    if os.path.exists(dict_path) == False:
        print("路径不存在")

    '''

    '''
    with open(dict_path, 'rb') as f:
        loss_d = pickle.load(f)
    ###########

    for k, v in loss_d.items():
        if "loss" in k or 'acc' in k:
            losses = loss_d[k]
            loss = []
            l = int(len(losses) / 100)
            for i in range(l):
                end = (i + 1) * 100 if (i + 1) * 100 <= len(losses) else len(losses)
                Len = 100 if (i + 1) * 100 <= len(losses) else len(losses) - i * 100
                loss.append(sum(losses[i:end]) / Len)
            plt.figure()
            plt.title(k)
            plt.xlabel(os.path.basename(dict_path))
            plt.plot(loss)
            plt.show()


if __name__ == '__main__':
    ver = "v1"
    p = r'Experiments\{}\running_loss_{}.pickle'.format(ver, ver)
    plot_loss(p)
