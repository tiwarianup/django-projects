from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
#from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import notice
from .forms import createNoticeModelForm

# Create your views here.

def homepage(request):
    qs = notice.objects.all().published()
    context = {"objects" : qs}
    templateName = "listNotices.html"
    return render(request, templateName, context)

def noticeDetails(request, slug):
    #obj = notice.objects.get(noticeSlug=slug) for 1 entry OR obj = notice.objects.filter(noticeSlug=slug) return List
    obj = get_object_or_404(notice, noticeSlug=slug)
    context = {"object": obj}
    templateName = "noticeDetails.html"
    return render(request, templateName, context)

def listNotices(request):
    customTitle = False
    qs = notice.objects.all().published()
    if request.user.is_authenticated:
        my_qs = notice.objects.filter(noticeUser = request.user)
        qs = (qs | my_qs ).distinct()
        customTitle = True

    #now = timezone.now()
    #qs = notice.objects.filter(publishDate__lte=now)
    context = {"objects": qs, "customTitle": customTitle}
    templateName = "listNotices.html"
    return render(request, templateName, context)

# @login_required
@staff_member_required
def createNotice(request):
    form = createNoticeModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.noticeUser = request.user
        obj.save()
        print(form.cleaned_data.get('noticeSlug'))
        # obj = form.save(commit=False) obj.title = form.cleaned_data.get("title") obj.save() #To manipulate form data
        #obj = notice.objects.create(**form.cleaned_data)
        form = createNoticeModelForm()
    context = {"form": form}
    templateName = "createNotice.html"
    return render(request, templateName, context)

@staff_member_required
def deleteNotice(request, slug):
    obj = get_object_or_404(notice, noticeSlug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"object": obj}
    templateName = "deleteNotice.html"
    return render(request, templateName, context)

@staff_member_required
def updateNotice(request, slug):
    obj = get_object_or_404(notice, noticeSlug=slug)
    form = createNoticeModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form, "title": f"Update Notice: {obj.noticeTitle}"}
    templateName = "updateNotice.html"
    return render(request, templateName, context)