from django.shortcuts import render
from .forms import PictureForm
from upload.models import Picture
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required(login_url='/login/')
@permission_required('upload.add_picture', raise_exception=True)
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = PictureForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='/login/')
@permission_required('upload.view_picture', raise_exception=True)
def image_show(request):
    """Dynamic gallery of picture"""
    resultdisplay = Picture.objects.all()
    return render(request, 'main.html', {'Picture': resultdisplay})
