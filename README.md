# Web Scraping and Preloading Script
## This script is designed to crawl a website starting from a specified base URL, discover all internal links, and preload each page to improve caching performance.

## Features
• Crawl Website: Discover internal URLs starting from a specified base URL.

• Preload URLs: Fetch and preload each discovered URL to cache for faster access.

• Status Reporting: Logs status of each URL fetch and preload attempt.


## Usage

### Prerequisites
• Python 3.x installed

• Required Python libraries (requests, BeautifulSoup) installed. You can install them using pip:
  ``` pip install requests beautifulsoup4 ```


## Setup
Download the script file (WebPagePreload.py)

Update the BASE_URL variable in the script with your website's base URL. (ex. https://google.com or https://www.google.com)

## Legal Compliance and Use
Please ensure compliance with all applicable laws and the terms of service of the website you are crawling. Respect the rights and privacy of others when using this script. The intended use of this program is to crawl your own website and preload it for cache purposes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
