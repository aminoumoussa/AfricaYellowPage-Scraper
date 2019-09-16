FROM python:3.7
COPY . /AfricaYellowPage-Scraper
WORKDIR /AfricaYellowPage-Scraper
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# install requirements
RUN pip3 install -r requirements.txt
# install africayellowpage module
RUN pip3 install -e .
# define entrypoint
ENTRYPOINT ["africayellowpage-scraper","mine"] 