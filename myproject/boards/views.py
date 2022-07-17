from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    try:
      print("pk: {}".format(pk)) 
      #board = Board.objects.get(id=pk)
      board = get_object_or_404(Board, pk=pk)
      print("board: {}".format(board))     
      return render(request, 'topics.html', {'board': board})
    except Board.DoesNotExist:
        raise Http404
