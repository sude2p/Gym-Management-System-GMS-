from django.shortcuts import render, redirect
from .models import Member
from django.utils import timezone
from datetime import timedelta
from .forms import MemberModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.urls import *



# Create your views here.
 #-------------------method for viewing all member data---------------------------------------------------#
 
@login_required(login_url='login')
def projectView(request):
    project = Member.objects.all()
    member_count = Member.objects.count()
    remaining_data = []
    current_day = timezone.now().date()
    for field in project:
        remaining_days = (field.date_finish - current_day).days
        remaining_data.append({
            'field':field,
            'remaining_days': remaining_days,
            
        })

    
    context = {'project': remaining_data, 'member': member_count,}
    return render(request, 'Project/project.html', context)
 #----------------------------------------------------------------------#  
               
#---------method for add member--------------------------------------#

@login_required(login_url='login')
def projectAdd(request):
    project = Member.objects.all()

    form = MemberModelForm()
    context = {'form': form, 'project':project}
    if request.method == 'POST':
        form = MemberModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # print('Data saved:', form.cleaned_data)
            return redirect('home')
        else:
            # print('Form errors:', form.errors)
            messages.error(request, 'Error in adding New Member')

    return render(request, 'Project/project_create.html', context)
    
    
  #----------------------------------------------------------------------#   

#---------method for view pk--------------------------------------#

@login_required(login_url='login')
def projectIdView(request, pk):
    page = 'Idview'
    project = Member.objects.get(id=pk)
    name = project.f_name
    
    form = MemberModelForm(instance=project)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
       
        

    context = {'form':form, 'name':name,'project':project,'page':page,}
    return render(request, 'Project/project_view.html',context)
 #----------------------------------------------------------------------#


#--------method for update Member data-----------------------------------------#

@login_required(login_url='login')
def projectUpdate(request, pk):
    page = 'edit'
    project = Member.objects.get(id=pk)
    # form = MemberModelForm(instance=project)
    if request.method == 'POST':
        form = MemberModelForm(request.POST,request.FILES,instance=project)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated!!')
            return redirect('home')
        else:
            messages.error(request, 'invalid edit')
    else:
        form = MemberModelForm(instance=project)
    context = {'form':form, 'page':page, 'project':project}
    return render(request,'Project/project_view.html',context)

#-------------------------------------------------------------------------------#

@login_required(login_url='login')
def projectDelete(request, pk):
    project = Member.objects.get(id=pk)
    context = {'project':project}
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    else:
        project = Member.objects.get(id=pk)   
   
    return render(request, 'Project/project_del_confirm.html')

#--------------------------method for user count---------------------------------------#

# def userCount(request):
#     member_count = Member.objects.count()
#     context = {'member':member_count}
#     return render(request, 'templates/main.html', context)
    





#-------------------------------------------------------------------------------------#
# def memberProfile(request):
#     profile = 