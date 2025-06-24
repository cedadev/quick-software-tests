from ceda_datapoint import DataPointClient

print("doing ceda_datapoint test...")
client = DataPointClient(org="CEDA")
search = client.search(collections=["cmip6"],
                       data_selection={},
                       query=["cmip6:institution_id=MOHC",
                              "cmip6:activity_id=ScenarioMIP",
                              "cmip6:experiment_id=ssp119",
                              "cmip6:variant_label=r1i1p1f2",
                              "cmip6:variable_id=psl",
                              "cmip6:table_id=Amon",
                              ],
                       max_items=10)
#search.display_cloud_assets()
cluster = search.collect_cloud_assets()
product = cluster["CMIP6.ScenarioMIP.MOHC.UKESM1-0-LL.ssp119.r1i1p1f2.Amon.psl.gn.v20190830-reference_file"]
ds = product.open_dataset()
psl = ds["psl"]
val = psl[1,2,3].to_numpy().item()
print(val)
assert 99211 < val < 99212
print("done")
