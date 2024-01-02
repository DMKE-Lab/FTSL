import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

# if __name__ == '__main__':
    # names = ['1', '3', '5', '10']
    # x = [1, 3, 5, 7]
    # plt.rcParams['font.sans-serif'] = ['times new roman']  # 显示汉字
    #
    # # 创建一个包含四个子图的画布
    # fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    #
    # y_1 = [0.172, 0.243, 0.222, 0.219]
    # y_2 = [0.157, 0.196, 0.210, 0.215]
    # y_3 = [0.182, 0.267, 0.272, 0.273]
    #
    # axs[1, 1].plot(x, y_1, color='orangered', marker='o', linestyle='-', label='FAAN')
    # axs[1, 1].plot(x, y_2, color='blue', marker='D', linestyle='-', label='FSRL')
    # axs[1, 1].plot(x, y_3, color='green', marker='*', linestyle='-', label='TFSL')
    #
    # axs[1, 1].axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    # axs[1, 1].axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    # axs[1, 1].axvline(x=6, color='lightgray', linestyle='-', linewidth=1)
    #
    # axs[1, 1].yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    # axs[1, 1].legend()
    # axs[1, 1].set_xticks(x)
    # axs[1, 1].set_xticklabels(names)
    #
    # axs[1, 1].set_xlabel("K-Shot", fontsize=18)
    # axs[1, 1].set_ylabel("MRR", fontsize=18)
    # axs[1, 1].set_xlim(left=1, right=7)
    # axs[1, 1].set_ylim(bottom=0.1)
    # axs[1, 1].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # axs[1, 1].grid(color='lightgray')
    # axs[1, 1].grid(True)
    # axs[1, 1].legend(fontsize=14)
    # axs[1, 1].tick_params(axis='x', labelsize=18)
    # axs[1, 1].tick_params(axis='y', labelsize=18)
    #
    # u_1 = [0.134, 0.17, 0.19, 0.15] #k = 1
    # u_2 = [0.11, 0.13, 0.148, 0.15]  # y轴的值
    # u_3 = [0.14, 0.19, 0.205, 0.221]
    #
    # axs[0, 0].plot(x, u_1, color='orangered', marker='o', linestyle='-', label='FAAN')
    # axs[0, 0].plot(x, u_2, color='blue', marker='D', linestyle='-', label='FSRL')
    # axs[0, 0].plot(x, u_3, color='green', marker='*', linestyle='-', label='TFSL')
    #
    # axs[0, 0].axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    # axs[0, 0].axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    # axs[0, 0].axvline(x=6, color='lightgray', linestyle='-', linewidth=1)
    #
    # axs[0, 0].yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    # axs[0, 0].legend()
    # axs[0, 0].set_xticks(x)
    # axs[0, 0].set_xticklabels(names)
    #
    # axs[0, 0].set_xlabel("K-Shot", fontsize=18)
    # axs[0, 0].set_ylabel("Hits@1", fontsize=18)
    # axs[0, 0].set_xlim(left=1, right=7)
    # axs[0, 0].set_ylim(bottom=0.1)
    # axs[0, 0].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # axs[0, 0].grid(color='lightgray')
    # axs[0, 0].grid(True)
    # axs[0, 0].legend(fontsize=14)
    # axs[0, 0].tick_params(axis='x', labelsize=18)
    # axs[0, 0].tick_params(axis='y', labelsize=18)
    #
    # i_1 = [0.171, 0.286, 0.260, 0.290] #k = 1
    # i_2 = [0.183, 0.248, 0.264, 0.249]  # y轴的值
    # i_3 = [0.221, 0.317, 0.320, 0.327]
    # axs[0, 1].plot(x, i_1, color='orangered', marker='o', linestyle='-', label='FAAN')
    # axs[0, 1].plot(x, i_2, color='blue', marker='D', linestyle='-', label='FSRL')
    # axs[0, 1].plot(x, i_3, color='green', marker='*', linestyle='-', label='TFSL')
    #
    # axs[0, 1].axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    # axs[0, 1].axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    # axs[0, 1].axvline(x=6, color='lightgray', linestyle='-', linewidth=1)
    #
    # axs[0, 1].yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    # axs[0, 1].legend()
    # axs[0, 1].set_xticks(x)
    # axs[0, 1].set_xticklabels(names)
    #
    # axs[0, 1].set_xlabel("K-Shot", fontsize=18)
    # axs[0, 1].set_ylabel("Hits@5", fontsize=18)
    # axs[0, 1].set_xlim(left=1, right=7)
    # axs[0, 1].set_ylim(bottom=0.1)
    # axs[0, 1].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # axs[0, 1].grid(color='lightgray')
    # axs[0, 1].grid(True)
    # axs[0, 1].legend(fontsize=14)
    # axs[0, 1].tick_params(axis='x', labelsize=18)
    # axs[0, 1].tick_params(axis='y', labelsize=18)
    #
    # o_1 = [0.243, 0.362, 0.327, 0.354]  # k = 1
    # o_2 = [0.224, 0.289, 0.312, 0.310]  # y轴的值
    # o_3 = [0.267, 0.408, 0.407, 0.412]
    #
    # axs[1, 0].plot(x, o_1, color='orangered', marker='o', linestyle='-', label='FAAN')
    # axs[1, 0].plot(x, o_2, color='blue', marker='D', linestyle='-', label='FSRL')
    # axs[1, 0].plot(x, o_3, color='green', marker='*', linestyle='-', label='TFSL')
    #
    # axs[1, 0].axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    # axs[1, 0].axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    # axs[1, 0].axvline(x=6, color='lightgray', linestyle='-', linewidth=1)
    #
    # axs[1, 0].yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    # axs[1, 0].legend()
    # axs[1, 0].set_xticks(x)
    # axs[1, 0].set_xticklabels(names)
    #
    # axs[1, 0].set_xlabel("K-Shot", fontsize=18)
    # axs[1, 0].set_ylabel("Hits@10", fontsize=18)
    # axs[1, 0].set_xlim(left=1, right=7)
    # axs[1, 0].set_ylim(bottom=0.1)
    # axs[1, 0].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # axs[1, 0].grid(color='lightgray')
    # axs[1, 0].grid(True)
    # axs[1, 0].legend(fontsize=14)
    # axs[1, 0].tick_params(axis='x', labelsize=18)
    # axs[1, 0].tick_params(axis='y', labelsize=18)
    #
    # fig.subplots_adjust(left=0.05)  # 调整子图布局
    # # fig.subplots_adjust(right=0.05)  # 调整子图布局
    #
    # plt.show()

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

if __name__ == '__main__':
    names = ['1', '3', '5', '10']
    x = [1, 3, 5, 7]
    plt.rcParams['font.sans-serif'] = ['times new roman']  # 显示汉字

    # 创建一个包含四个子图的画布，使用gridspec
    fig = plt.figure(figsize=(12, 10))
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], hspace=0.5, wspace=0.3)


    y_1 = [0.243, 0.362, 0.327, 0.354]
    y_2 = [0.224, 0.289, 0.312, 0.310]
    y_3 = [0.267, 0.368, 0.373, 0.412]
    ax1 = plt.subplot(gs[1, 0])  # 左下
    ax1.plot(x, y_1, color='orangered', marker='o', linestyle='-', label='FAAN', markersize=8)
    ax1.plot(x, y_2, color='blue', marker='D', linestyle='-', label='FSRL', markersize=8)
    ax1.plot(x, y_3, color='green', marker='*', linestyle='-', label='TFSL', markersize=8)

    ax1.axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    ax1.axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    ax1.axvline(x=6, color='lightgray', linestyle='-', linewidth=1)

    ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax1.legend()
    ax1.set_xticks(x)
    ax1.set_xticklabels(names)

    ax1.set_xlabel("K-Shot", fontsize=18)
    ax1.set_ylabel("Hits@10", fontsize=18)
    ax1.set_xlim(left=1, right=7)
    ax1.set_ylim(bottom=0.1)
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax1.grid(color='lightgray')
    ax1.grid(True)
    ax1.legend(fontsize=14)
    ax1.tick_params(axis='x', labelsize=18)
    ax1.tick_params(axis='y', labelsize=18)

    u_1 = [0.134, 0.17, 0.19, 0.15]
    u_2 = [0.11, 0.13, 0.148, 0.15]
    u_3 = [0.14, 0.18, 0.192, 0.221]

    ax2 = plt.subplot(gs[0, 0])  # 左上
    ax2.plot(x, u_1, color='orangered', marker='o', linestyle='-', label='FAAN', markersize=8)
    ax2.plot(x, u_2, color='blue', marker='D', linestyle='-', label='FSRL', markersize=8)
    ax2.plot(x, u_3, color='green', marker='*', linestyle='-', label='TFSL', markersize=8)

    ax2.axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    ax2.axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    ax2.axvline(x=6, color='lightgray', linestyle='-', linewidth=1)

    ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax2.legend()
    ax2.set_xticks(x)
    ax2.set_xticklabels(names)

    ax2.set_xlabel("K-Shot", fontsize=18)
    ax2.set_ylabel("Hits@1", fontsize=18)
    ax2.set_xlim(left=1, right=7)
    ax2.set_ylim(bottom=0.05)
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax2.grid(color='lightgray')
    ax2.grid(True)
    ax2.legend(fontsize=14)
    ax2.tick_params(axis='x', labelsize=18)
    ax2.tick_params(axis='y', labelsize=18)

    i_1 = [0.171, 0.286, 0.260, 0.290]
    i_2 = [0.183, 0.248, 0.264, 0.249]
    i_3 = [0.221, 0.307, 0.312, 0.327]

    ax3 = plt.subplot(gs[0, 1])  # 右上
    ax3.plot(x, i_1, color='orangered', marker='o', linestyle='-', label='FAAN', markersize=8)
    ax3.plot(x, i_2, color='blue', marker='D', linestyle='-', label='FSRL', markersize=8)
    ax3.plot(x, i_3, color='green', marker='*', linestyle='-', label='TFSL', markersize=8)

    ax3.axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    ax3.axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    ax3.axvline(x=6, color='lightgray', linestyle='-', linewidth=1)

    ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax3.legend()
    ax3.set_xticks(x)
    ax3.set_xticklabels(names)

    ax3.set_xlabel("K-Shot", fontsize=18)
    ax3.set_ylabel("Hits@5", fontsize=18)
    ax3.set_xlim(left=1, right=7)
    ax3.set_ylim(bottom=0.1)
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax3.grid(color='lightgray')
    ax3.grid(True)
    ax3.legend(fontsize=14)
    ax3.tick_params(axis='x', labelsize=18)
    ax3.tick_params(axis='y', labelsize=18)

    o_1 = [0.172, 0.243, 0.222, 0.219]
    o_2 = [0.157, 0.196, 0.210, 0.215]
    o_3 = [0.182, 0.247, 0.253, 0.257]

    ax4 = plt.subplot(gs[1, 1])  # 右下
    ax4.plot(x, o_1, color='orangered', marker='o', linestyle='-', label='FAAN', markersize=8)
    ax4.plot(x, o_2, color='blue', marker='D', linestyle='-', label='FSRL', markersize=8)
    ax4.plot(x, o_3, color='green', marker='*', linestyle='-', label='TFSL', markersize=8)

    ax4.axvline(x=2, color='lightgray', linestyle='-', linewidth=1)
    ax4.axvline(x=4, color='lightgray', linestyle='-', linewidth=1)
    ax4.axvline(x=6, color='lightgray', linestyle='-', linewidth=1)

    ax4.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
    ax4.legend()
    ax4.set_xticks(x)
    ax4.set_xticklabels(names)

    ax4.set_xlabel("K-Shot", fontsize=18)
    ax4.set_ylabel("MRR", fontsize=18)
    ax4.set_xlim(left=1, right=7)
    ax4.set_ylim(bottom=0.1)
    ax4.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax4.grid(color='lightgray')
    ax4.grid(True)
    ax4.legend(fontsize=14)
    ax4.tick_params(axis='x', labelsize=18)
    ax4.tick_params(axis='y', labelsize=18)
    plt.savefig('res.svg')
    plt.show()
