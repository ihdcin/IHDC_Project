from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import TransactionSerializer


# Create your views here.

# Home Page Function
def home(request):
    return render(request, 'home.html')


# User registration
def Register(request):
    if request.method == 'POST':
        nm = request.POST['nm']
        em = request.POST['em']
        pw = request.POST['pw']
        cp = request.POST['cp']
        if User.objects.filter(username=em).exists():
            print("Email Already Exists")
            messages.info(request, 'Email Already Exists')
        else:
            user = User.objects.create_user(email=em, username=em, password=pw, first_name=nm, is_staff=True)
            user.save()
            print("Registered successfully..!")
            messages.info(request, 'Registered successfully..!')
            return redirect('/')
    return render(request, 'register.html')


# Login Function
def LoginFunction(request):
    if request.method == "POST":
        em = request.POST['em']
        pw = request.POST['pw']
        user = authenticate(username=em, password=pw)
        if user is not None:
            messages.info(request, f"Welcome {user.first_name.title()}")
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'login.html')


# Logout Function
def Logout_Function(request):
    logout(request)
    return redirect('/')


# Create Vendor

@csrf_exempt
def add_vendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vn')
        account_number = request.POST.get('acn')
        ifsc_code = request.POST.get('ifsc')

        vendor = Vendor(vendor_name=vendor_name, account_number=account_number, ifsc_code=ifsc_code)
        vendor.save()
        messages.info(request, "Vendor Added successfully")
        return JsonResponse({'status': 'success', 'message': 'Vendor added successfully!'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})


@login_required(login_url='login')
def Create_vendor(request):
    return render(request, 'create_vendor.html')


# Vendor CRUD Operations

# Vendor Table
@login_required(login_url='login')
def vendor_table(request):
    vend = Vendor.objects.all().order_by('-id')
    return render(request, 'vendor_table.html', {'vend': vend})


# Deleting Vendor Function

@csrf_exempt
def delete_vendor(request, vendor_id):
    if request.method == 'DELETE':
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.delete()
            return JsonResponse({'status': 'success', 'message': 'Vendor deleted successfully!'})
        except Vendor.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Vendor not found'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})


# Editing Vendor Details

@csrf_exempt
def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)

    if request.method == 'POST':
        # Update vendor fields based on POST data
        vendor.vendor_name = request.POST.get('vn')
        vendor.account_number = request.POST.get('acn')
        vendor.ifsc_code = request.POST.get('ifsc')
        vendor.save()

        return JsonResponse({'status': 'success', 'message': 'Vendor updated successfully!'})

    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)


@login_required(login_url='login')
def EditingVendor(request, id):
    v = Vendor.objects.get(id=id)
    if request.method == "POST":
        v.vendor_name = request.POST['vn']
        v.account_number = request.POST['acn']
        v.ifsc_code = request.POST['ifsc']
        v.save()
        messages.info(request, "Updated successfully")

    return render(request, 'venedit.html', {'v': v})


# Rest Api endpoint for downloading data to print data into an excel file

def vendor_transactions_api(request):
    vendor_id = request.GET.get('vendor_id')
    if vendor_id:
        vendor = get_object_or_404(Vendor, id=vendor_id)
        transactions = Transaction.objects.filter(vendor=vendor)
        serializer = TransactionSerializer(transactions, many=True)

        return JsonResponse({
            'vendor_id': vendor.id,
            'vendor_name': vendor.vendor_name,
            'vendor_account_no': vendor.account_number,
            'IFSC_Code': vendor.ifsc_code,
            'transactions': serializer.data
        })

    return JsonResponse({'transactions': []})


# Adding Transaction
@login_required(login_url='login')
def AddingTransaction(request):
    vens = Vendor.objects.all().order_by('-id')

    return render(request, 'addtrans.html', {'vens': vens})


def AddTransaction(request):
    if request.method == 'POST':
        ven = Vendor.objects.get(id=request.POST['ven'])
        des = request.POST['desc']
        amt = request.POST['amt']
        date = request.POST['date']
        trans = Transaction(vendor=ven, description=des, amount=amt, date=date)
        trans.save()
        messages.info(request, f"Transaction added successsfully to the vendor {ven.vendor_name}")
        return redirect('addtran')
