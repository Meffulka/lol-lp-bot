FROM armv7/armhf-ubuntu

RUN apt-get update & apt-get install python python-pip
RUN pip install python-telegram-bot --upgrade

RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-arm7hf.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

RUN apt-get install firefox-esr

RUN pip install selenium
RUN pip install pyvirtualdisplay

WORKDIR /app
COPY ./bot.py /app

CMD python bot.py