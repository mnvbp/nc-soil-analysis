"""information needed to send requests to the website during scraping"""
import http.client

conn = http.client.HTTPSConnection("www.ncagr.gov")

payload = ""

headers = {
    
}