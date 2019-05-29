import matplotlib.pyplot as plt
import pandas as pd
from Ex2_ThemePark import generalization
from Ex2_ThemePark.parameters import params


def plotting(data):
    # Single plotting
    fig, ax = plt.subplots()

    cols = ['avg_fun', 'avg_shop_balance', 'avg_consumer_balance']
    legend = ['Average Fun', 'Avg. Shop Balance', 'Avg. Consumer Balance']
    colors = ['red', 'blue', 'grey']

    for i, k in enumerate(legend):
        data.plot(x='num_consumers', y=cols[i], alpha=.35, color=colors[i], ax=ax)

    ax.legend(legend, frameon=False)
    # ax.set(xlabel='Ideology', ylabel='Frequency', title='Projects by output')

    # Using plot help from
    # https://matplotlib.org/gallery/showcase/bachelors_degrees_by_gender.html#
    # sphx-glr-gallery-showcase-bachelors-degrees-by-gender-py
    # Remove the plot frame lines. They are unnecessary here.
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary.
    # ax.set_xlim(0, 360)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
    # Provide tick lines across the plot to help your viewers trace along
    # the axis ticks. Make sure that the lines are light and small so they
    # don't obscure the primary data lines.
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
    # Remove the tick marks; they are unnecessary with the tick lines we just
    # plotted.
    plt.tick_params(axis='both', which='both', bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)

    plt.savefig('{}.png'.format('Output Theme Park'), bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    generalization.main(params)
    file = 'accounts_results.csv'
    df = pd.read_csv(file, sep=';')
    plotting(df)
