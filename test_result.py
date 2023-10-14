import netCDF4 as nc

former_id = "10200.pbs-server"
latter_id = "10200.pbs-server"

nc_former = nc.Dataset(f"output/{former_id}/RAMP1_md.force.nc", "r")
nc_latter = nc.Dataset(f"output/{latter_id}/RAMP1_md.force.nc", "r")

forces_former = nc_former.variables["forces"][:]
forces_latter = nc_latter.variables["forces"][:]

diff = (forces_former - forces_latter)

print(sum(diff**2))
