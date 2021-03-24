begin

  wks = gsn_open_wks("x11", "test")

  res              = True
  res@gsnFrame     = False
  res@mpMinLatF    = 51.10
  res@mpMaxLatF    = 51.85
  res@mpMinLonF    = -0.70
  res@mpMaxLonF    = 0.60

  plot = gsn_csm_map(wks, res)

  filename = "england_gor_2011.shp"
  dum1 = gsn_add_shapefile_polylines(wks, plot, filename, True)
  draw(plot)
  frame(wks)

end
