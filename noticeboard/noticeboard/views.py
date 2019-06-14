from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import notice
from .forms import createNoticeModelForm

# Create your views here.

def noticeDetails(request, slug):
    #obj = notice.objects.get(noticeSlug=slug) for 1 entry OR obj = notice.objects.filter(noticeSlug=slug) return List
    obj = get_object_or_404(notice, noticeSlug=slug)
    context = {"object": obj}
    templateName = "noticeDetails.html"
    return render(request, templateName, context)

def listNotices(request):
    obj = notice.objects.all()
    context = {"objects": obj}
    templateName = "listNotices.html"
    return render(request, templateName, context)

# @login_required
@staff_member_required
def createNotice(request):
    form = createNoticeModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        # obj = form.save(commit=False) obj.title = form.cleaned_data.get("title") obj.save() #To manipulate form data
        #obj = notice.objects.create(**form.cleaned_data)
        form = createNoticeModelForm()
    context = {"form": form}
    templateName = "createNotice.html"
    return render(request, templateName, context)

def deleteNotice(request, slug):
    context = {"form": None}
    templateName = "deleteNotice.html"
    return render(request, templateName, context)

def updateNotice(request, slug):
    context = {"form": None}
    templateName = "updateNotice.html"
    return render(request, templateName, context)