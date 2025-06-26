import tropycal.tracks as tracks

basin = tracks.TrackDataset(basin='north_atlantic',source='hurdat',include_btk=False)
season = basin.get_season(2017)
assert season.summary()["season_storms"] == 18
print("did tropycal test")
