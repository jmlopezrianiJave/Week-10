Powershell command for container:
```console
docker run -it --rm -v "${PWD}:/data" -w /data my-parallel-python bash
```
Sequential command:
```console
time bash -c 'for f in *.csv; do for c in 0 1 2; do python3 script.py "$f" $c; done; done'
```
Parallel Command:
```console
parallel python3 script.py {1} {2} ||| *.csv ||| 0 1 2
```