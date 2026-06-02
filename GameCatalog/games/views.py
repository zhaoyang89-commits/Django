from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Game
from .forms import GameForm

#首页
def home(request):
    latest_games = Game.objects.order_by('-id')[:6]
    return render(request, 'home.html',{'latest_games':latest_games})

#游戏列表页
def game_list(request):
    games = Game.objects.all()
    search = request.GET.get('search')
    if search :
        games = games.filter(
            title__icontains=search
        )
    return render(request,'game_list.html',{'games':games})

#游戏详情页
def game_detail(request,game_id):
    game = get_object_or_404(
        Game,
        id=game_id
    )
    return render(request,'game_detail.html',{'game':game})

#添加游戏
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('game_list')

    else:
        form = GameForm()
    return render(request,'add_game.html',{'form':form})

