from django.apps import apps
import django
import os
import json
# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataloading.settings')
django.setup()

models = apps.get_models()
for model in models:
    print(model)
    print(model.__name__)

from book.models import Book 

# Get all field names
field_names = [field.name for field in Book._meta.get_fields()]
#mv books.json book/fixtures/book/
fixture_name = "books.json"
#python manage.py loaddata book/fixtures/book/books.json 

#read the data file json, csv etc.
with open('data.json','r') as fp:
    books= json.load(fp)
books_fixture =[]
pk=30 #get the pk value from model , if there is data
for book in books:
    book_fixture={}
    book_fixture['model']= 'book.book'
    pk+=1
    book_fixture['pk']=pk
    #assuming the data has same fields name as model else mapping is required
    book_fixture['fields']=book
    books_fixture.append(book_fixture)

with open(fixture_name,'w') as fp:
    json.dump(books_fixture,fp)

print(field_names)
# def create_book():
#     book = Book(
#         title="This is from script",
#         author ="ajit",
#         isbn = "2024-0809",
#         pages=300,
#         language ='English'
#     )
#     book.save()
#     print(f'Book {book.title} by {book.author} created.')

# if __name__ =='__main__' :
    #create_book()  