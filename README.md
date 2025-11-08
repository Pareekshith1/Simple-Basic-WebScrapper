# Simple-Basic-WebScrapper

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup-4-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A simple and efficient web scraper built with Python that extracts pickup lines from popular websites. This project demonstrates basic web scraping techniques using BeautifulSoup4 and requests library.

## 📋 Overview

This Python web scraper extracts pickup lines from two different websites and saves them to a text file. The scraper is designed to be simple, easy to understand, and modifiable for scraping multiple sites.

**Current Sources:**
- [Woman's Day](https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/)
- [Pickup Lines Shopify](https://pickuplines.myshopify.com/blogs/funny-pickup-lines)

## 🔧 Components

### Main Components

1. **main.py** - The core scraper script containing:
   - HTTP request handlers using `requests` library
   - HTML parsing logic with `BeautifulSoup`
   - Data extraction from specific HTML elements
   - File writing operations to save extracted data

2. **pickuplines.txt** - Output file where scraped pickup lines are stored

### Technical Details

- **Parser**: Uses `lxml` parser for fast HTML/XML processing
- **Target Elements**: 
  - Woman's Day: `<div class="article-body-content">` → `<li>` tags
  - Pickup Lines Shopify: `<div class="page-container">` → `<strong>` tags
- **Encoding**: UTF-8 encoding for proper character handling
- **Output Format**: Plain text file with one pickup line per line

## 📦 Requirements

### Dependencies

The following Python packages are required to run this project:

```
beautifulsoup4
requests
lxml
```

### Python Version
- Python 3.6 or higher

## 🚀 Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Simple-Basic-WebScrapper.git
cd Simple-Basic-WebScrapper
```

### Step 2: Install Required Packages

You can install the required packages using pip:

```bash
pip install beautifulsoup4
pip install requests
pip install lxml
```

Or install all at once:

```bash
pip install beautifulsoup4 requests lxml
```

### Step 3: Verify Installation

Verify that all packages are installed correctly:

```bash
pip list | grep -E "beautifulsoup4|requests|lxml"
```

## ▶️ Running the Scraper

### Basic Usage

Run the scraper using Python:

```bash
python main.py
```

### What Happens When You Run It

1. The script sends HTTP GET requests to both websites
2. Parses the HTML content using BeautifulSoup
3. Extracts pickup lines from specific HTML elements
4. Prints the raw extracted data to console
5. Writes the cleaned pickup lines to `pickuplines.txt`

### Expected Console Output

You'll see two lists printed:
- First list: Raw HTML elements from Woman's Day
- Second list: Raw HTML elements from Pickup Lines Shopify

## 📤 Output

### Output File: `pickuplines.txt`

- **Location**: Same directory as `main.py`
- **Format**: Plain text, one pickup line per line
- **Encoding**: UTF-8
- **Note**: The file is overwritten each time the script runs (second source overwrites the first)

### Sample Output Structure

```
Are you a magician? Because whenever I look at you, everyone else disappears.
Do you have a map? I keep getting lost in your eyes.
Are you a parking ticket? Because you've got FINE written all over you.
...
```

## ⚙️ Customization

### Adding More Websites

To scrape additional websites, follow this pattern:

```python
# Add new source
new_source = requests.get('YOUR_URL_HERE').text
soup = BeautifulSoup(new_source, 'lxml')
data = soup.find('div', class_='your-target-class')
items = data.find_all('your-target-tag')

# Append to file instead of overwriting
with open('pickuplines.txt', 'a', encoding='utf-8') as file:
    for item in items:
        file.write(item.text + '\n')
```

### Modifying Target Elements

Change the `class_` and tag names to match your target website's HTML structure:

```python
pickups = soup.find('div', class_='your-class-name')
lines = pickups.find_all('your-tag-name')
```

## ⚠️ Known Issues

1. **File Overwriting**: The second source overwrites data from the first source. To preserve all data, change the second file write operation to append mode (`'a'` instead of `'w'`)

2. **Error Handling**: The script doesn't include error handling for network failures or missing HTML elements

## 🛠️ Future Improvements

- Add error handling for network requests
- Implement append mode to preserve data from all sources
- Add command-line arguments for customizable output
- Create a configuration file for easy website addition
- Add logging functionality
- Implement rate limiting to be respectful to source websites

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Version**: 1.0  
**Last Updated**: November 2025
