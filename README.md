
o3
==

Hadoop-Airflow Analytics.


Development Environment
-----------------------

    git clone git@github.com:mblomdahl/o3.git
    cd o3/
    wget -P resources/ http://apache.mirrors.spacedump.net/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
    wget -P resources/ http://apache.mirrors.spacedump.net/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
    wget -P resources/ http://apache.mirrors.spacedump.net/hive/hive-2.3.4/apache-hive-2.3.4-bin.tar.gz
    python3 -m venv venv && source venv/bin/activate
    SLUGIFY_USES_TEXT_UNIDECODE=yes pip install -r requirements.txt


Windows VirtualEnv
------------------

To support installing all the pip requirements for PyCharm development under Windows, create a Docker image and
[configure the IDE with it](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html). E.g.

    docker build -t mblomdahl/o3-venv .
    docker run -it mblomdahl/o3-venv pip freeze


Links
-----

* https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/

* https://www.linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/

* https://cwiki.apache.org/confluence/display/Hive/GettingStarted#GettingStarted-InstallationandConfiguration

