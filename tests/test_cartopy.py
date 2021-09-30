import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
# import cartopy.feature as cfeature
# from matplotlib.offsetbox import AnchoredText


def main():

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()

    ny_lon, ny_lat = -75, 43
    delhi_lon, delhi_lat = 77.23, 28.61

    plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
                      color='blue', linewidth=2, marker='o',
                      transform=ccrs.Geodetic(),
                      )

    plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
                      color='gray', linestyle='--',
                      transform=ccrs.PlateCarree(),
                      )

    plt.text(ny_lon - 3, ny_lat - 12, 'New York',
                      horizontalalignment='right',
                      transform=ccrs.Geodetic())

    plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
                      horizontalalignment='left',
                      transform=ccrs.Geodetic())

    plot_dir = os.environ['PLOT_DIR']
    png = os.path.join(plot_dir, 'cartopy.1.png')
    plt.savefig(png)
    print(f'Wrote: {png}')


# def main():
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#     ax.set_extent([80, 170, -45, 30], crs=ccrs.PlateCarree())
# 
#     # Put a background image on for nice sea rendering.
#     ax.stock_img()
# 
#     # Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
#     states_provinces = cfeature.NaturalEarthFeature(
#         category='cultural',
#         name='admin_1_states_provinces_lines',
#         scale='50m',
#         facecolor='none')
# 
#     SOURCE = 'Natural Earth'
#     LICENSE = 'public domain'
# 
#     ax.add_feature(cfeature.LAND)
#     ax.add_feature(cfeature.COASTLINE)
#     ax.add_feature(states_provinces, edgecolor='gray')
# 
#     # Add a text annotation for the license information to the
#     # the bottom right corner.
#     text = AnchoredText('\u00A9 {}; license: {}'
#                         ''.format(SOURCE, LICENSE),
#                         loc=4, prop={'size': 12}, frameon=True)
#     ax.add_artist(text)
# 
#     plot_dir = os.environ['PLOT_DIR']
#     png = os.path.join(plot_dir, 'cartopy.1.png')
#     plt.savefig(png)
#     print(f'Wrote: {png}')


if __name__ == '__main__':
    main()

