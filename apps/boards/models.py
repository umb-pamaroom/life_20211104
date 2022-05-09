from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe
from django.conf import settings
from apps.activity.models import Activity
from django.contrib.contenttypes.fields import GenericRelation

User = settings.AUTH_USER_MODEL
class Board(models.Model):
    """
        This is the model for a board
    """
    name = models.TextField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    activity = GenericRelation(Activity)
    
    def __str__(self):
        return "{}".format(self.name , self.owner)


class BoardMember(models.Model):
    """
        This is the model for a board member
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    activity = GenericRelation(Activity)
    archived= models.BooleanField(default=False)

    def __str__(self):
        return "{} in {}".format(self.user, self.board)

class Referral(models.Model):
    """
        This is the model for a referral.
        Referral are used for inviting members.
    """
    board_member = models.ForeignKey(BoardMember,on_delete=models.CASCADE)
    token = models.TextField()
    email = models.TextField()
    activity = GenericRelation(Activity)
    archived= models.BooleanField(default=False)
        
    def generate_token(self):
        # Generating secure token using python 3.6 libraries
        not_found = True
        while(not_found):
            new_token = token_urlsafe(32)
            if not Referral.objects.filter(token=new_token):
                self.token = new_token
                not_found = False

    def __str__(self):
        return "{}-referral".format(self.email)

class Column(models.Model):
    """
        This is the model for column
    """
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.TextField()
    position = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)
    activity = GenericRelation(Activity)

    def __str__(self):
        return "{}".format(self.name)

class Card(models.Model):
    """
        This is the model for the card
    """
    name = models.TextField()
    description = models.TextField(null=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    position = models.IntegerField()
    due_date = models.DateTimeField(null=True)
    date = models.DateField('日付', null=True)
    archived = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    activity = GenericRelation(Activity)

    def __str__(self):
        return "{}".format(self.name)

    # Mabalik na ni sa json
    @property
    def is_overdue(self):
        return True

class CardMember(models.Model):
    """
        This is the model for a card member
    """
    board_member = models.ForeignKey(BoardMember, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    activity = GenericRelation(Activity)
    archived = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}-{}".format(self.card.name,self.board_member.user)

class CardComment(models.Model):
    """
        This is the model for a card comment
    """
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)
    activity = GenericRelation(Activity)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.user, self.comment)
