import netCDF4 as nc
import numpy as np

former_id = "10204.pbs-server"
latter_id = "5278351.ccpbs1"

nc_former = nc.Dataset(f"output/{former_id}/RAMP1_md.force.nc", "r")
nc_latter = nc.Dataset(f"output/{latter_id}/RAMP1_md.force.nc", "r")

# Get first frame
forces_former = nc_former.variables["forces"][:][0]
forces_latter = nc_latter.variables["forces"][:][0]

square_diff = np.power(forces_former - forces_latter, 2)
square_latter = np.power(forces_latter, 2)
square_former = np.power(forces_former, 2)
errors = np.sqrt(
    square_diff.sum(axis=-1) / square_former.sum(axis=-1)
    )


print(f"Max error: {errors.max()}")
print(f"Min error: {errors.min()}")
print(f"Mean error: {errors.mean()}")
print(f"Median error: {np.median(errors)}")
