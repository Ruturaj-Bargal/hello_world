import urllib

def read_text():
    quotes = open("/Users/rutuzoa/Documents/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/xml?text="+text_to_check)
    output = connection.read()
    print (output)
    connection.close()
read_text() 

