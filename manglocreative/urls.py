"""manglocreative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# ============================================================================================================ #
#   kkk      kkk      ooooo       dddddddd         eeeeeeeeee   kkk      kkk      ooooo            ooooo       #
#   kkk     kkk     ooooooooo     ddddddddddd      eeeeeeeeee   kkk     kkk     ooooooooo        ooooooooo     # 
#   kkk    kkk     ooo     ooo    ddd      ddd     eee          kkk    kkk     ooo     ooo      ooo     ooo    #
#   kkk   kkk     oooo     oooo   ddd       ddd    eee          kkk   kkk     oooo     oooo    oooo     oooo   #
#   kkk  kkk      oooo     oooo   ddd        ddd   eee          kkk  kkk      oooo     oooo    oooo     oooo   #
#   kkkkkkkk      oooo     oooo   ddd        ddd   eeeeeeeeee   kkkkkkkk      oooo     oooo    oooo     oooo   #
#   kkk  kkk      oooo     oooo   ddd        ddd   eee          kkk  kkk      oooo     oooo    oooo     oooo   #
#   kkk   kkk     oooo     oooo   ddd       ddd    eee          kkk   kkk     oooo     oooo    oooo     oooo   #
#   kkk    kkk     ooo     ooo    ddd      ddd     eee          kkk    kkk     ooo     ooo      ooo     ooo    #
#   kkk     kkk     ooooooooo     dddddddddd       eeeeeeeeee   kkk     kkk     ooooooooo        ooooooooo     #
#   kkk      kkk      ooooo       ddddddd          eeeeeeeeee   kkk      kkk      ooooo            ooooo       #
# ============================================================================================================ #


from django.conf.urls import include, url

from django.contrib import admin

from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^manage/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
