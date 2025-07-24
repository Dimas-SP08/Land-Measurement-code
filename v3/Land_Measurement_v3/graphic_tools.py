import matplotlib.pyplot as plt

def make_graphic(table):
    '''Make and save three survey plots: line, bar, scatter'''
    
    '''Make elevation profile plot'''
    fig1, ax = plt.subplots(dpi=100, tight_layout=True)
    ax.plot(table['POINT NUMBER'], table['ELEVATION (AMSL)'],lw=2, ls='-.')
    ax.grid(True)
    ax.set_xlabel('Point Number')
    ax.set_ylabel('Elevation (m)')
    ax.set_title('Elevation Profile')
    plt.xticks(rotation=45, ha='right')
    fig1.savefig('elevation_profile_plot.png')

    '''Make height difference bar plot'''
    fig2, ax2 = plt.subplots(dpi=100, tight_layout=True)
    ax2.bar(table['POINT NUMBER'], table['HEIGHT DIFFERENCE'], color='orange')
    ax2.set_xlabel('Point Number')
    ax2.set_ylabel('Height Difference (m)')
    ax2.set_title('Height Difference Between Points')
    plt.xticks(rotation=45, ha='right')
    fig2.savefig('height_difference_bar_plot.png')

    '''Make distance vs elevation with scatter plot'''
    fig=plt.figure(dpi=100)
    plt.scatter(table['DISTANCE (m)'], table['ELEVATION (AMSL)'])
    plt.title("Distances vs Elevation")
    plt.xlabel("Cumulative Distances (m)")
    plt.ylabel("Elevation AMSL (m)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    fig.savefig('elevation_scatter_plot.png')