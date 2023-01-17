from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = ["Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers. Today, IBM Quantum makes real quantum hardware -- a tool scientists only began to imagine three decades ago -- available to hundreds of thousands of developers.",
"ChatGPT is a chatbot launched by OpenAI in November 2022. It is built on top of OpenAI's GPT-3 family of large language models, and is fine-tuned with both supervised and reinforcement learning techniques.","OpenAI is an artificial intelligence research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc. The company conducts research in the field of AI with the stated goal of promoting and developing friendly AI in a way that benefits humanity as a whole"]

def section(request,pk):
    if 1<=pk<=3:
        return HttpResponse(texts[pk-1])
    else:
        raise Http404("request section does not exists")

