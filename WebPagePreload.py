import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Enter your website URL below / replace [https://your-website.splicate.com] with your URL
BASE_URL = 'https://your-website.splicate.com'


def crawl_website(base_url):
    discovered_urls = set()
    to_crawl = [base_url]

    while to_crawl:
        url = to_crawl.pop(0)
        if url in discovered_urls:
            continue

        try:
            response = requests.get(url)
            if response.status_code == 200:
                discovered_urls.add(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    full_url = urljoin(base_url, href)
                    if full_url.startswith(base_url) and full_url not in discovered_urls:
                        to_crawl.append(full_url)
            else:
                print(f"Failed to fetch {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

    return discovered_urls


def preload_urls(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Preloaded: {url}")
            else:
                print(f"Failed to preload: {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error preloading {url}: {e}")


def main():
    
    discovered_urls = crawl_website(BASE_URL)

    if discovered_urls:
        print(f"Found {len(discovered_urls)} URLs to preload.")
        
        preload_urls(discovered_urls)
        print("All pages have been preloaded for cache.")
    else:
        print("No URLs found to preload.")

if __name__ == "__main__":
    main()
