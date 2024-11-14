import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def scrap_page():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        scraped_data = []
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            scraped_data.append(f'"{text}" - {author}')
        
        return "\n".join(scraped_data)
    else:
        return "Erro ao acessar a página."

def send_email(subject, body):
    from_email = "rafaelmoura2032@gmail.com"
    to_email = "" #Coloque algum email válido aqui, Professor
    password = "udqi oyfv kbel nbyw"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    data = scrap_page()
    subject = "Citações extraídas do site"
    send_email(subject, data)
    print("Email enviado com sucesso!")

if __name__ == "__main__":
    main()
