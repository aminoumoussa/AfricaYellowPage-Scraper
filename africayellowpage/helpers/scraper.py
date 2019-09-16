from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import csv , time
import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')
global PAGE
PAGE="https://www.yellowpagesofafrica.com"
def get_driver():
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    return driver

def process_companies(companies):
    rows = []
    for company in companies:
        row = extract_data(company)
        rows.append(row)

    return rows

def extract_data(company):
    # company name
    name = company.find('div', class_='ct-product--tilte')
    if name and name.getText().strip():
        name = name.getText().strip()
        print(name)

    # company address
    address = company.find('i', class_='fa fa-map-marker')
    if address:
        address = address.next_sibling.strip()
        print(address)

    # company email
    email = company.find('i', class_='fa fa-envelope')
    if email:
        email = email.next_sibling.strip()
        print(email)

    # company website
    website = company.find('i', class_='fa fa-link')
    if website:
        website = website.next_sibling.strip()
        print(website)

    # company number
    number = company.find('i', class_='fa fa-phone')
    if number:
        number = number.next_sibling.strip()
        print(number)

    # company fax
    fax = company.find('i', class_='fa fa-fax')
    if fax:
        fax = fax.next_sibling.strip()
        print(fax)
    
    row = dict(cname=name,
            caddress=address,
            cemail=email,
            cwebsite=website,
            cnumber=number,
            cfax=fax)
    
    return row

def get_pages(what,where):
        global PAGE
        driver = get_driver()
        driver.get(PAGE)
        element = driver.find_element_by_id("s")
        element.send_keys(what)
        element = driver.find_element_by_id("s2")
        element.send_keys(where)
        element.send_keys(Keys.RETURN)
        page = 1
        results = []
        clickable_link = driver.find_elements_by_class_name('buttonShowCo')
        if len(clickable_link) >0:
            while True:
                logging.info(f'[+] request:{PAGE}')
                for link in clickable_link:
                    #print(link)
                    driver.execute_script("arguments[0].click();", link)
                    time.sleep(5)
            
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                companies = soup.find_all('div', class_='ct-main-text')
                results.extend(process_companies(companies))
                page += 10 
                PAGE = f'https://www.yellowpagesofafrica.com/companies/search/start-{page}/'
                driver.get(PAGE)
                clickable_link = driver.find_elements_by_class_name('buttonShowCo')
                if len(clickable_link) == 0:
                    logging.info('[+] Done!')
                    break
            return results 
        else:
            logging.info("[+] No Result!")
            return None
        
            
def save_results(dict_data,csv_file):
    try:
        with open(csv_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=['cname','caddress','cemail','cwebsite','cnumber','cfax'])
            writer.writeheader()
            writer.writerows(dict_data)
    except Exception as e:
        logging.error(f"[ERROR WRITING FILE] {e}")
        return False



