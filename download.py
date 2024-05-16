
import wikipediaapi 

title = input('insert title ')

wiki_wiki = wikipediaapi.Wikipedia('Digital_Content_Retrival/1.0 (alerotta@yahoo.it)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI)

page = wiki_wiki.page(title)

if page.exists() :
     with open('/Users/alessandrorotta/Desktop/project/' + title + '.txt', 'w', encoding='utf-8') as file:
        file.write(page.text)
else :
    print("page not found")
