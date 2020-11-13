apt-get install default-jdk -qq > /dev/null
[ -f spark-3.0.1-bin-hadoop2.7.tgz ] || wget -q https://mirrors.netix.net/apache/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
[ -d spark-3.0.1-bin-hadoop2.7 ] || tar -xzf spark-3.0.1-bin-hadoop2.7.tgz
pip install -q findspark