# Amberの計算結果検証

https://ambermd.org/tutorials/basic/tutorial14/index.php のデータを利用する。

## How to test

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

