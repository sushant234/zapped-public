from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    datentime = models.DateTimeField(auto_now=True)

class employee(models.Model):
    img = models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    f_name = models.CharField(max_length=70)
    l_name = models.CharField(max_length=70)
    postn = models.CharField(max_length=100)
    twitter = models.CharField(max_length=150, default='twitter.com')
    facebook = models.CharField(max_length=150, default='facebook.com')
    git = models.CharField(max_length=150, default='github.com')
    link = models.CharField(max_length=150, default='linkedin.com')

class client(models.Model):
    logo = models.ImageField(upload_to='pics',default='Null')
    desc = models.TextField()
    website = models.CharField(max_length=150)
    img_alt = models.CharField(max_length=150)
    companyname = models.CharField(max_length=70)


class mldesc(models.Model):
    imgs =  models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    desc = models.TextField()
    state = models.CharField(max_length=10, default='Null')

class mldescbox(models.Model):
    desc = models.TextField()

class wddesc(models.Model):
    imgs =  models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    desc = models.TextField()
    state = models.CharField(max_length=10, default='Null')

class wddescbox(models.Model):
    desc = models.TextField()

class dsdesc(models.Model):
    imgs =  models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    desc = models.TextField()
    state = models.CharField(max_length=10, default='Null')

class dsdescbox(models.Model):
    desc = models.TextField()

class addesc(models.Model):
    imgs =  models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    desc = models.TextField()
    state = models.CharField(max_length=10, default='Null')

class addescbox(models.Model):
    desc = models.TextField()

class blog(models.Model):
    imgs =  models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    heading = models.CharField(max_length=500)
    summary = models.CharField(max_length=1000)
    desc = models.TextField()
    title = models.CharField(max_length=100)
    meta = models.TextField()
    author = models.CharField(max_length=100,default='ZAPPAD')

class homepage(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()
    anim_txt1 = models.CharField(max_length=100)
    anim_txt2 = models.CharField(max_length=100)
    anim_txt3 = models.CharField(max_length=100)

class anddev(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()

class blog1(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()

class catalogue(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()

class digseo(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()

class maclea(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()

class webdev(models.Model):
    title = models.CharField(max_length=100)
    meta = models.TextField()
