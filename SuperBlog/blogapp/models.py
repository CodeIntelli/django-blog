from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField

#when we are using editor then in tinymce it will not work so we are working with js file 

# Create your models here.
# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/")
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.title)

    

    def image_show(self):
        return format_html('<img src="/Media/{}" width="150" />'.format(self.image))


# post models
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/")

    def __str__(self):
        return str(self.post_id)

    def image_show(self):
        return format_html('<img src="/Media/{}" width="150" />'.format(self.image))



    

