# package_prac
This is practice of packaging python packages and modules neatly.

## crawler_2
### Execute Celery
Execute the follwoing command in `py_src/crawler/`to create Daemon.
```shell
$ celery -A crawler_2.task multi start crawler_2.task.download -Q download -c 2 -P threads -l info --logfile=worker-download.log --pidfile=worker-download.pid
$ celery -A crawler_2.task multi start crawler_2.task.media -Q media -c 2 -P threads -l info --logfile=worker-media.log --pidfile=worker-media.pid
```

Then run
```shell
$ python3 crawler_2
```

To empty queue
```shell
$ celery -A crawler_2.task purge
```

To empty Daemon
```shell
$ kill `cat worker-download.pid`
$ kill `cat worker-media.pid`
```

To monitor Celery tasks
```shell
$ pip install flower
$ celery -A crawler_2.task flower &
```
