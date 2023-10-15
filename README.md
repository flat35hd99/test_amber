# Amberの計算結果検証

https://ambermd.org/tutorials/basic/tutorial14/index.php のデータを利用する。

## How to test

あらかじめnetcdf4をインストールしておく。

```console
# On PBS
mkdir log
cd log

qsub -N test_force ../job.sh

# On IMS
mkdir log
cd log

jsub -N test_force ../job.sh
```

## Result

```
$ python test_result.py 
Max error: 5.128322300151922e-06
Min error: 0.0
Mean error: 1.5130504494861366e-07
/home/users/wataru/miniconda3/envs/netcdf/lib/python3.12/site-packages/numpy/core/fromnumeric.py:771: UserWarning: Warning: 'partition' will ignore the 'mask' of the MaskedArray.
  a.partition(kth, axis=axis, kind=kind, order=order)
Median error: --
```
