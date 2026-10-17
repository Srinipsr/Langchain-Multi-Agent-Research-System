from src.tools.tools import web_search, scrape_url

#results =web_search("latest news on AI research?")


#results =scrape_url("https://blog.google/innovation-and-ai/products/")


#results = web_search.invoke("latest news on AI research?")
#print (results)

results = scrape_url.invoke("https://openai.com/news")
print (results)