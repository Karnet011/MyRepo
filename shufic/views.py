from django.shortcuts import render, redirect
from shufic.models import Video, Comment
from . import forms
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth


def hello(request, video_id):
    return render(request, 'oneVideo.html',
                  {"video": Video.objects.get(id=video_id), "comment": Comment.objects.filter(Comment_Video_id=video_id)})


def oneVideo(request, video_id = 1):
    comment_form = form.CommentForm
    args = {}
    args.update(csrf(request))
    args['video'] = Video.objects.get(id=video_id)
    args['comment'] = Comment.objects.filter(Comment_Video_id=video_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'oneVideo.html', args)


def addlike(request, video_id):
    video = Video.objects.get(id=video_id)
    video.Video_likes += 1
    video.save()
    if request.path.split('/')[2][0] == 'V':
        return redirect("/video/")
    return redirect("/video/get/" + str(video_id))


def ajaxlike(request):
    if request.GET:
        idlike = request.GET["addlike"]
        video = Video.objects.get(id=idlike)
        video.Video_likes += 1
        video.save()
    return HttpResponse(video.Video_likes)


def addlike1(request, video_id):
    if video_id not in request.COOKIES:
        video = Video.objects.get(id=video_id)
        video.Video_likes += 1
        video.save()
        if request.path.split('/')[2][0] == 'V':
            response = redirect('/video/')
        else:
            response = redirect('/video/get/' + str(video_id))
        response.set_cookie(video_id, "test")                 #создаем печеньку
        return response
    if request.path.split('/')[2][0] == 'V':
        return redirect("/video/")
    return redirect("/video/get/" + str(video_id))


def addcomment(request, video_id):
    if request.POST:
        forma = form.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            forma.save()
    return redirect('/video/get/%s/' % video_id)


def addcomment1(request, video_id):
    if request.POST and ('pause' not in request.session):
        forma = form.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            forma.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/video/get/%s/' % video_id)


def showvideo(request):
    class content(type(Video.objects.all())):
        comment = ""
    content_list = []
    for i in Video.objects.all():
        j = content()
        j.Video_url = i.Video_url
        j.Video_name = i.Video_name
        j.Video_o = i.Video_o
        j.Video_data = i.Video_data
        j.Video_likes = i.Video_likes
        j.id = i.id
        j.comment = Comment.objects.filter(Comment_Video_id=i.id)
        content_list.append(j)
    return render(request, 'videocontent.html', {"Video": content_list, "username": auth.get_user(request).username})
# Create your views here.
