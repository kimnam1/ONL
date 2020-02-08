import wikipediaapi

wiki = wikipediaapi.Wikipedia('ko')

testing = wiki.page('7월 21일')


print(testing.sections)