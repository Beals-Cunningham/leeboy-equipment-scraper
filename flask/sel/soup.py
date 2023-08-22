import bs4, time, json, os, re

path = os.path.join(os.getcwd(), "web", "js", "queries.json")
with open(path) as f:
    Leeboy_soup = json.load(f)
    f.close()

def simmer(data, driver):
    url = data["url"]
    html = data["html"]
    flavor = data["flavor"]
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return serve(soup, flavor, url, driver)

def serve(soup, flavor, url, driver):
    #this is the main processing function- find relevant data and dish it up
    queries = Leeboy_soup[flavor]
    scoop = {}
    
    for query in queries:
        print(query)
        if 'el' in query:
            el = query['el']
        else:
            el = None
        if 'id' in query:
            id = query['id']
        else:
            id = None
        if 'class' in query:
            class_ = query['class']
        else:
            class_ = None
        if 'attrs' in query:
            attrs = query['attrs']
        else:
            attrs = None

        if query['el'] == 'query':
                if query['col'] == 'description':
                    ladle1 = soup.select_one(query['selector1'])
                    ladle2 = soup.select_one(query['selector2'])
                    l = str(ladle1) + str(ladle2)
                    scoop[query['col']] = l.replace('\n', '')
                elif query['col'] == 'technical_specs':
                    l = soup.select_one(query['selector'])
                    scoop[query['col']] = str(l).replace('\n', '')
                else:
                    l = soup.select_one(query['selector'])
                    scoop[query['col']] = l.text.replace('\n', '')
        
        ladle = soup.find_all(el, id=id, class_=class_, attrs=attrs)
        for slurp in ladle:
            if query['el'] != 'query':
                if query["col"] == 'eq_image':
                    scoop[query['col']] = slurp['src']
                elif query["col"] == "title":
                    scoop[query['col']] = slurp.text
            
                        
    spoon = {"data":scoop, "url":url}
    return spoon