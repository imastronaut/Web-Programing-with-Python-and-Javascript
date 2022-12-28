from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import util
import markdown2
from django import forms
from random import choice

class Datafrom(forms.Form):
    title = forms.CharField(label="Title", max_length = 64)
    content = forms.CharField(label="Content", widget=forms.Textarea)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    content = util.get_entry(title)
    if not content:
        return HttpResponse("Entry doesn't exist!")
    content=markdown2.markdown(content)
    return render(request,"encyclopedia/entry.html",{
        "title":title,
        "content":content
    })
def search(request):
    if request.method=="POST":
        name = request.POST.get("q")
        entry_list = []
        entries = util.list_entries()
        for entry in entries:
            if name.lower()==entry.lower():
                return HttpResponseRedirect(reverse("entry",args=(entry,)))
            if name.lower() in entry.lower():
                entry_list.append(entry)
        return render(request, "encyclopedia/results.html",{
            "entries":entry_list,
            "name":name
        })
    return render(request, "encyclopedia/index.html")

def newpage(request):
    if request.method=="POST":
        title = request.POST.get("title").Capitalize()
        content = request.POST.get("content")
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/newpage.html",{
                "warning":True
            })
        util.save_entry(title, content)
    return render(request, "encyclopedia/newpage.html")
def editpage(request,entry):
    if request.method=="POST":
        content = request.POST.get("content")
        util.save_entry(entry, content)
        return HttpResponseRedirect(reverse("entry",args=(entry,)))
    content=util.get_entry(entry)
    return render(request, "encyclopedia/editpage.html", {
        "content":content,
        "title":entry
    })
def random(request):
    entry_list=util.list_entries()
    entry=choice(entry_list)
    return HttpResponseRedirect(reverse("entry",args=(entry,)))