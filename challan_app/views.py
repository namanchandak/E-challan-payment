from django.shortcuts import render, HttpResponse
from challan_app.models import Contact,Police,Challan,Universal
from django.shortcuts import render , redirect
import os
from twilio.rest import Client

# Create your views here.
def index(request):
    return render(request, 'index.html')

def policelogin(request):
    context={"name":"Traffic Police Login",
             "login":"policelogin"}
    if request.method=="POST":
        nuser=Police.objects.filter(UserName=request.POST['name'],Password=request.POST['password'])
        if nuser.exists():
            request.session['id']=nuser[0].Id
            return redirect(police)
        else:
            return render(request, 'login.html',context) 
    
    return render(request, 'login.html',context)

def adminlogin(request):
    context={"name":"Admin Login",
             "login":"adminlogin"}
    if request.method=="POST":
        if(request.POST['name']=="Admin" and request.POST['password']=="1234"):
            return redirect(admin)
        else:
            return render(request, 'login.html',context)
    print("hii")
    
    return render(request, 'login.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        mail=request.POST['mail']
        phone=request.POST['phone_number']
        message=request.POST['message']
        user=Contact(Name=name,Mail=mail,Phone_number=phone,Message=message)
        user.save()
        return redirect(index)

def admin(request):
    return render(request, 'admin.html')

def police(request):
    return render(request, 'police.html')

def createchallan(request):
    if request.method=="POST":
        vehicle=request.POST['vehicle_number']
        offences=request.POST['Offences']
        location=request.POST['location']
        price={
            '1':1000,
            '2':1000,
            '3':1000,
            '4':500,
            '5':500,
            '6':500,
            '7':25000,
            '8':5000,
            '9':5000,
            '10':5000,
            '11':10000,
            '12':2000,
            '13':1000,
            '14':1000,
            '15':5000,
            '16':2000,
            '17':2000
        }
        rule={
            '1':"Driving without a seat belt",
            '2':"Triple riding on two-vehicle",
            '3':"Driving without helmet",
            '4':"Carrying excess luggage",
            '5':"Driving without a number plate",
            '6':"Parking in ‘no parking zone",
            '7':"Minor driving vehicle",
            '8':"Disobey of traffic signals",
            '9':"Dangerous/rash driving",
            '10':"Using a mobile phone while driving",
            '11':"Drunken driving",
            '12':"Driving vehicle without registration",
            '13':"Over-speeding",
            '14':"Driving when mentally or physically unfit to drive",
            '15':"Driving without a valid driving license",
            '16':"Driving without insurance",
            '17':"Overloading"
        }
        universal=Universal.objects.get(Vehicle_number=vehicle)
        police=Police.objects.get(Id=request.session['id'])
        challan=Challan(Fees=price[offences],Offences=rule[offences],Vehicle_number=universal,Location=location,Police_id=police)
        challan.save()
        

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
        account_sid = 'AC6744357eb2547ad71c5914b20e32ffd5'
        auth_token = 'fbe396656116a1a5df7e52c518314995'
        client = Client(account_sid, auth_token)
        u=Universal.objects.get(Vehicle_number=vehicle)
        number=u.Phone_number
        print("1")
        message_body=f"The owner of Vehicle number {u.Vehicle_number} is fine rs. {challan.Fees} for {challan.Offences} "
        print(number)
        message = client.messages \
                        .create(
                            body=message_body,
                            from_='+15736464463',
                            to=str(number)
                        )
        print(str(number))
        print(message.sid)
        return redirect(index)
    return redirect(createchallan)

def pay_challan(request):
    return render(request, 'pay_challan.html')

def challan_form(request):
    if request.method == 'POST':
        Vehicle_number = request.POST['vehicle_no']
        universal=Universal.objects.get(Vehicle_number=Vehicle_number)
        challan_instance = Challan.objects.filter(Vehicle_number=universal) 
        if challan_instance.exists():
            context={
                "challan_instance": challan_instance
            }
            return render(request, 'pay_challan.html', context)
        else:
            # Vehicle does not exist, display a message
            message = "No challans pendings."
            return render(request, 'challan_form.html', {'message': message})
    
    return render(request, 'challan_form.html')  # Render the form template


def createpolice(request):
    if request.method=="POST":
        name=request.POST['Police_Name']
        police_id=request.POST['Police_Id']
        phone_number=request.POST['Phone_Number']
        rank=request.POST['Rank']
        username=request.POST['Username']
        password=request.POST['Password']
        create_police = Police(Name=name, Id=police_id,Phone_number=phone_number,Rank=rank,UserName=username,Password=password)
        create_police.save()
        return redirect(admin)

    return render(request, 'admin.html')

def createuser(request):
    if request.method=="POST":
        user_name=request.POST['Name']
        license_no=request.POST['License_no']
        vehicle_no=request.POST['Vehicle_no']
        phone_no=request.POST['Phone_no']
        mail=request.POST['Mail']
        insurance_no=request.POST['Insurance_no']
        registration_no=request.POST['Registration_no']
        address=request.POST['Address']
        create_user = Universal(Name=user_name, License_number=license_no,Vehicle_number=vehicle_no,Phone_number=phone_no,Mail=mail,Insurance_number=insurance_no,Registration_number=registration_no,Address=address)
        create_user.save()
        return redirect(admin)

    return render(request, 'admin.html')

def police_list(request):
    context={
        "police":Police.objects.all()
    }
    return render(request, 'police_list.html', context)

def user_list(request):
    context={
        "user":Universal.objects.all()
    }
    return render(request, 'user_list.html', context)



