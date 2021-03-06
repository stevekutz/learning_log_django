from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """ The home page for Learning Log """
    return render(request, 'learning_logs/index.html')

# refactored check logged in user to owner of topic
def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404    
    
#    return None   

@login_required
def topics(request):
    """ Show all topics """
    # topics = Topic.objects.order_by('data_added')
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Show a single topic and all of its entries""" 
    topic = Topic.objects.get(id=topic_id)
    
    # # Make sure the topic belongs to the current user
    # if topic.owner != request.user:
    #     raise Http404

    # refactored
    check_topic_owner(topic, request)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Add new topic """       
    if (request.method != 'POST' and request.method == 'GET'):
        # There was no POST data sumitted, return blank form
        form = TopicForm()
    else:
        # POST data exists, process data within request.POST
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            # form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)           

@login_required
def new_entry(request, topic_id):
    """ Add new entry for specific topic """    
    topic = Topic.objects.get(id = topic_id)

    # refactored
    check_topic_owner(topic, request)

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

@login_required
def edit_entry(request, entry_id):
    """ Edit an exiting entry """
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    # # Make sure the topic belongs to the current user
    # if topic.owner != request.user:
    #     raise Http404

    # refactored
    check_topic_owner(topic, request)

    if (request.method != 'POST' and request.method == 'GET'):
        # GET request => this is an initial request, pre-fill form with current entry data
        form = EntryForm(instance=entry)
    else: 
        # POST request => updated data submitted, fill form with updated data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)        
           
