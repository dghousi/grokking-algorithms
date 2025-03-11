cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
    
def get_data_from_server(url):
    return url


print(get_page("www.google.com"))
print(get_page("www.google.com/about"))
print(get_page("www.google.com/contacts"))
print(get_page("www.google.com/services"))