from django.contrib import admin
from .models import feedback
from .models import employee
from .models import client
from .models import mldesc
from .models import wddesc
from .models import dsdesc
from .models import addesc
from .models import mldescbox
from .models import wddescbox
from .models import dsdescbox
from .models import addescbox
from .models import blog
from .models import homepage
from .models import blog1
from .models import anddev
from .models import catalogue
from .models import digseo
from .models import maclea
from .models import webdev
# Register your models here.

admin.site.register(feedback)
admin.site.register(employee)
admin.site.register(client)
admin.site.register(mldesc)
admin.site.register(wddesc)
admin.site.register(dsdesc)
admin.site.register(addesc)
admin.site.register(mldescbox)
admin.site.register(wddescbox)
admin.site.register(dsdescbox)
admin.site.register(addescbox)
admin.site.register(blog)
admin.site.register(homepage)
admin.site.register(blog1)
admin.site.register(anddev)
admin.site.register(catalogue)
admin.site.register(digseo)
admin.site.register(webdev)