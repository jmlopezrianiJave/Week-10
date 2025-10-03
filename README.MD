Powershell command for container:
```console
    docker run -it --rm -v "${PWD}:/data" -w /data my-parallel-python bash
```
Parallel Command:
```console
    parallel python3 script.py {1} {2} ||| *.csv ||| 0 1 2
```