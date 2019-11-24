from django.shortcuts import render, redirect
from article.models import Article




def list_article(request):

    articles = Article.objects.all()
    data = {'articles': articles}

    return render(request, 'article/list.html', data)




def create_article(request):
    if request.method =='POST':
        # print(request.POST)
        # title = request.POST['title']
        # None은 찾은 값이 없을때 반환하는 값 위처럼 썼을때 없으면 오류가 난다.
        title = request.POST.get('title', None)
        content =request.POST.get('content', None)
        if title and content:
            article = Article.objects.create(title=title, content=content)
            return redirect('list')
    #  create는 함수작동과 동시에 db에 적용되며 바뀌는데
    #  save는 어떤 함수를 작동하고 구문을 써줘야지 db에 저장한다.
    return render(request, 'article/create.html')


def detail_article(request,pk):
    article = Article.objects.get(pk=pk)
    data ={
        'article': article
    }

    return render(request, 'article/detail.html' , data)