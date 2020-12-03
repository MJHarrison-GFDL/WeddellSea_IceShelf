Weddell Sea regional test case for IceShelf Thermodynamic Coupling Test



INSTALL:

Follow MOM6-examples  build instructions for MOM6_SIS2 coupled configuration

(wget ftp://ftp.gfdl.noaa.gov/pub/Matthew.Harrison/Regional_MOM6/WeddellSea_IceShelf/INPUT.tar;tar xvf INPUT.tar)

RUN:

e.g.

(mpirun -n 128 $MOM6_SIS2_EXECUTABLE 2> std.err > std.out)
