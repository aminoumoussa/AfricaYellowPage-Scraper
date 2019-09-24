# AfricaYellowPage-Scraper
Africa Yellow Page Scraper  

A command line tool to scrape [Yellow Page Africa](https://www.yellowpagesofafrica.com) 

## How to use it:
* __install requirements__
```bash
pip install -r requirements.txt
```

* __install package__
```bash
pip install -e .
```

* __command to run the scraping__
```python
"""
Usage:
    africayellowpage_scraper mine <what> <where> [--file_path=<destination_file>]

Options:
    <what>    Qui,quoi? (Hotels)
    <where>        Où? (Ghana)   
    --file_path file to save results to 
"""
```

## Run as docker image

### From Repository
* __build image__
```bash
docker build -t africa_yellowpage .
```

* __run image with arguments__
(Example)
```bash
docker run -it --rm africa_yellowpage Hotels Ghana