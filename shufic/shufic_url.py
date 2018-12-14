from django.urls import re_path
from shufic.views import showvideo, hello, addlike, oneVideo, addcomment, addlike1, addcomment1, ajaxlike


urlpatterns = [
    re_path(r'^$', showvideo),
    re_path(r'^get/(?P<video_id>\d+)/$', oneVideo),
    re_path(r'^addlike/ajax/', ajaxlike),
    re_path(r'^addlikes/(?P<video_id>\d+)/$', addlike1),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', addcomment1),
    re_path(r'^Vaddlikes/(?P<video_id>\d+)/$', addlike1),
]