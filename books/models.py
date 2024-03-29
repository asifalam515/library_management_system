from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserAccount
from datetime import datetime
# Category model
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    image = models.ImageField(upload_to='books/images/')
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category', related_name='books')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_account.user.first_name} - {self.book.title}"

class Review(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE,default=None)
    borrowed_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE,default=None)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.borrowed_book.book.title} by {self.user_account.user.username}"

def get_default_user():
    # Replace this logic to get the desired default user
    return User.objects.first()



class ReturnTransaction(models.Model):
    borrowed_book = models.OneToOneField(BorrowedBook, on_delete=models.CASCADE, related_name='return_transaction')
    return_date = models.DateField(auto_now_add=True)
    returned_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.borrowed_book.user_account.user.first_name} - {self.borrowed_book.book.title} - Returned Amount: {self.returned_amount}"
