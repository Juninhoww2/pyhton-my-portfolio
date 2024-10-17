from scraper import scrape_techcrunch

def test_scrape_techcrunch():
    headlines = scrape_techcrunch()
    # Assertions to check the results
    assert isinstance(headlines, list)  # Check if it returns a list
    assert len(headlines) > 0          # Check if the list is not empty
    assert isinstance(headlines[0], tuple)  # Check if each item is a tuple (headline, link)
    # Add more specific assertions as needed (e.g., check for certain keywords in headlines)