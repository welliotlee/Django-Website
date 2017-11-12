import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_prog.settings')

import django
django.setup()

from newp_app1.models import Category, Page


def populate():
    python_cat = add_cat('Python', 64, 128)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=100)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=100)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=100)

    django_cat = add_cat("Django", 32, 64)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=100)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=100)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", 16, 32)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=101)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=101)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, likes=0, views=0):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting Project population script...")
    populate()