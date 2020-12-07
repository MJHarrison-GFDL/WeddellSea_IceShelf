# IPython log file

import netCDF4 as nc
f=nc.Dataset('MOM.res.nc','a')
g=nc.Dataset('../../../thick.nc')
thick=g.variables['thick'][:]
u=f.variables['u'][:]*0.0
f.variables['u'][:]=u
v=f.variables['v'][:]*0.0
f.variables['v'][:]=v
h=nc.Dataset('../MOM_IC.nc')
h_ic = h.variables['h'][:]
h_res=f.variables['h'][:]
h_res[:,:,thick==0.]=h_ic[:,:,thick==0.]
f.variables['h'][:]=h_res
ave_ssh=f.variables['ave_ssh'][:]
ave_ssh[:,thick==0.]=0.
sfc=f.variables['sfc'][:]
sfc[:,thick==0.]=0.
f.variables['ave_ssh'][:]=ave_ssh
f.variables['sfc'][:]=sfc
f.sync()
f.close()
