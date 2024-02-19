from django.contrib import admin
from .models import Category,Book,BorrowedBook,Review,ReturnTransaction
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Review)
admin.site.register(ReturnTransaction)