from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category,Page

'''def index(request):
    return HttpResponse("Rango says hello world!"<a href='/rango/about'>"About"</a>)
'''
def about(request):
    context = RequestContext(request)

    return render_to_response('rango/about.html',context)

def index(request):
       # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]

    page_list=Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':page_list}


    for category in category_list:
        category.url = category.name.replace(' ', '_')



    # Render the response and send it back!
    return render_to_response('rango/index.html', context_dict, context)


def category(request, category_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    category_name = category_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'category_name': category_name}

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('rango/category.html', context_dict, context)
print page_list
print context_dict
'''def twtmeup():
     from tweepy.streaming import StreamListener
 from tweepy import OAuthHandler
 from tweepy import Stream
 from django.http import HttpResponse

 consumer_key="XXXXX"
 consumer_secret="XXXXX"

 access_token="XXXXXX"
 access_token_secret="XXXXX"

class StdOutListener(StreamListener):

def on_data(self, data):
    print data
    return True

def on_error(self, status):
    print status

if __name__ == '__main__':
     l = StdOutListener()
     auth = OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['BT'])


 def index(request):
  return HttpResponse("try")
'''
