FROM python:3

ADD MainController.py /
ADD JsonController.py /
ADD RestController.py /
ADD MySQLController.py /
ADD ConfigFile.properties /

RUN pip install configparser
RUN pip install requests
RUN pip install mysqlclient
RUN pip install mysql-connector

CMD [ "python", "./MainController.py" ]