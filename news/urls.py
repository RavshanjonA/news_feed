from django.urls import path

from news.views import home_page, contact_page, page_notfound, single_page

app_name="news"

urlpatterns = [
    path('', home_page, name="home-page"),
    path('contact', contact_page, name="contact-page"),
    path('404', page_notfound, name="page-notfound"),
    path('single_page', single_page, name="single-page"),
]
