from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import UserModel
from .forms import Registration
# from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def show_details(request):
    if request.method=="POST":
        form=Registration(request.POST)
        if form.is_valid():

            user_obj = form.save(commit=False) #don't save yet
            
            user_obj.save() 
            
            messages.success(request, "User created successfully.")
            
            all_data = UserModel.objects.all().order_by('-id')

            return render(request,'TestProject1/user_reg_form.html',{'form':Registration(),
                                                                     'data':all_data,
                                                                     'valid_form':'ok',
                                                                     'is_update':False})
        else:
            print('Form is not valid!!!')
    else:
        form=Registration()
    data = UserModel.objects.all()  # fetching all data from database
    return render(request,'TestProject1/user_reg_form.html',{'form':form,
                                                             'data':data, 
                                                             'is_update':False})



#DELETE FUNCTION START

def delete_details(request, id):
    user = get_object_or_404(UserModel, pk=id)
    user.delete()
    
    messages.success(request, "User deleted sucessfully")

    all_data = UserModel.objects.all().order_by('-id')
    return render(request,'TestProject1/user_reg_form.html',{'form':Registration(),
                                                             'data':all_data, 
                                                             'valid_form':'ok'
                                                            })




#UPDATE FUNCTION

def update_details(request, id):
    instance = get_object_or_404(UserModel, pk=id)
    old_password = instance.Password
    if request.method == "POST":
        form = Registration(request.POST, instance=instance)

        if form.is_valid():
            User_obj = form.save(commit=False)

            raw_password = form.cleaned_data.get('Password')

            if raw_password:
                User_obj.Password =raw_password #new password again
            else:
                User_obj.Password = old_password

            User_obj.save()

            messages.success(request,"Form is successfully updated")

            data = UserModel.objects.all().order_by('-id')
            return render(request, 'TestProject1/user_reg_form.html',{'form':Registration(),
                                                                  'data':data, 
                                                                  'is_update':False,
                                                                  'valid_form':'ok'})
    
        else:
            messages.error(request, 'Update Failed!!. Please check the form')


    else:
        form = Registration(instance=instance)
        print('Updated User:',instance.Password)

    data = UserModel.objects.all().order_by('-id')
    return render(request, 'TestProject1/user_reg_form.html',{'form':form,
                                                            'data':data,
                                                            'is_update':True,
                                                            'valid_form':'ok'})
