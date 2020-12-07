# IPython log file

import xarray as xr
ds=xr.open_dataset('MOM.res.nc')
ds2=ds.drop_vars(['u2','v2','h2','uh','vh','diffu','diffv','ubtav','vbtav','ubt_IC','vbt_IC','Kd_shear','Kv_shear','MLD','hML'])
ds2.to_netcdf('MOM.res.new.nc',format='NETCDF3_CLASSIC')
