from django.shortcuts import render

@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    projects = Project.objects.order_by('-overall').all()
    # top = projects[1]
    runners=Project.objects.all()[:4]
    try:
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render(request, 'index.html', locals())
