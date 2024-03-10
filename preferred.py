import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功
        return response.text
    except requests.RequestException as e:
        print(f"请求错误：{e}")
        return None

def extract_ip_addresses(html):
    soup = BeautifulSoup(html, 'html.parser')
    ip_addresses = []

    # 找到表格，此处假设IP地址在具有id为data-table的表格中
    table = soup.find('table', id='data-table')
    if table:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1:  # 确保单元格数量足够
                ip_address = cells[1].text
                ip_addresses.append(ip_address)
    return ip_addresses

def save_ips_to_txt(ip_addresses, filename='ip_addresses.txt'):
    with open(filename, 'w') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

if __name__ == '__main__':
    url = 'https://monitor.gacjie.cn/page/cloudflare/ipv4.html'
    html_content = fetch_html(url)
    if html_content:
        ip_addresses = extract_ip_addresses(html_content)
        save_ips_to_txt(ip_addresses)
        print(f"IP地址已保存到TXT文件.")
