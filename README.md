# package_prac
This is practice of packaging python packages and modules neatly.

## Execute Celery
### crawler_2
```shell
$ celery -A crawler_2.task multi start crawler_2.task.download -Q download -c 2 -P threads -l info --logfile=worker-download.log --pidfile=worker-download.pid
$ celery -A crawler_2.task multi start crawler_2.task.media -Q media -c 2 -P threads -l info --logfile=worker-media.log --pidfile=worker-media.pid
```

then run
```shell
$ python3 crawler_2
```
