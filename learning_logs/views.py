from django.shortcuts import render, redirect
from .models import Topic    # ADDED this  400
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """ The home page for Learning Log """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Show all topics """
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Show a single topic and all of its entries""" 
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Add new topic """       
    if (request.method != 'POST' and request.method == 'GET'):
        # There was no POST data sumitted, return blank form
        form = TopicForm()
    else:
        # POST data exists, process data within request.POST
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)           


def new_entry(request, topic_id):
    """ Add new entry for specific topic """    
    topic = Topic.objects.get(id = topic_id)

    if (request.method != 'POST' and request.method == 'GET'):
        # No POST data submitted, return blank form
        form = EntryForm()

    else:
        # POST data exists, process data within request.POST
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) 
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)           