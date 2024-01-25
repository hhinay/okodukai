from django.shortcuts import render, get_object_or_404, redirect
from .models import Money
from .models import Want
from .forms import MoneyForm
from .forms import WantForm
from django.views.generic import CreateView, ListView

# Create your views here.
def index(request):
    moneys = Money.objects.all()
    context = { "moneys" : moneys }
    return render(request, 'app/index.html', context)

def passbook(request):
    moneys = Money.objects.order_by("duedate")
    old_title = 0
    old_balance = 0
    old_title2 = 0
    for money in moneys:
        money.titil = old_title + money.title
        old_title = money.titil
        money.titil2 = old_title2 + money.title2
        old_title2 = money.titil2
        money.balance = old_balance + (money.title2 - money.title)
        old_balance = money.balance
        money.save()
    # latest_money = Money.objects.latest()

    header = ['日付','メモ','支出','収入','残高']

    my_dict2 = {
        # 'title': '通帳',
        'moneys': moneys,
        # 'latest_money': latest_money,
        'header':header,
        'old_title':old_title,
        'old_title2':old_title2,
        'old_balance':old_balance
    }
    return render(request, 'app/passbook.html', my_dict2)

def want(request):
    wants = Want.objects.all()
    moneys = Money.objects.all()
    old_balance = 0
    for money in moneys:
        money.balance = old_balance + (money.title2 - money.title)
        old_balance = money.balance
        money.save()
    latest_money = Money.objects.order_by("-id").first()

    context = {
        'wants':wants,
        'moneys': moneys,
        'latest_money': latest_money,
    }
    return render(request, 'app/want.html', context)

    def want(request):
        return render(request, 'app/want.html', context)

def setting(request):
    return render(request, 'app/setting.html')

def new(request):
    if request.method == "POST":
        money_form=MoneyForm(request.POST)
        if money_form.is_valid():
            money_form.save()
            moneys = Money.objects.all()
            context = { "moneys" : moneys }
            return redirect('app:passbook')
    money_form = MoneyForm()
    context = {
        "money_form": money_form,
    }
    return render(request, 'app/new.html', context)

def neww(request):
    if request.method == "POST":
        money_form=MoneyForm(request.POST)
        if money_form.is_valid():
            money_form.save()
            moneys = Money.objects.all()
            context = { "moneys" : moneys }
            return redirect('app:passbook')
    money_form = MoneyForm()
    context = {
        "money_form": money_form,
    }
    return render(request, 'app/neww.html', context)

# def swap(request, id):
#     money = get_object_or_404(Money, pk=id)
#     money.swap_title_and_title2()
#     context = {
#         "money" : money
#     }
#     return render(request, 'app/swap.html', context)

def edit(request, id):
    money = get_object_or_404(Money, pk=id)
    money_form = MoneyForm(instance=money)
    context = {
        "money" : money,
        "money_form" : money_form,
    }
    return render(request, 'app/edit.html', context)

def editi(request, id):
    money = get_object_or_404(Money, pk=id)
    money.swap_title_and_title2()
    money_form = MoneyForm(instance=money)
    context = {
        "money" : money,
        "money_form" : money_form,
    }
    return render(request, 'app/editi.html', context)

def edito(request, id):
    money = get_object_or_404(Money, pk=id)
    money.swap_title_and_title2()
    money_form = MoneyForm(instance=money)
    context = {
        "money" : money,
        "money_form" : money_form,
    }
    return render(request, 'app/edito.html', context)
    
def edit0(request, id):
    money = get_object_or_404(Money, pk=id)
    money_form = MoneyForm(instance=money)
    context = {
        "money" : money,
        "money_form" : money_form,
    }
    return render(request, 'app/edit0.html', context)

def update(request, id):
    if request.method == "POST":
        money =get_object_or_404(Money, pk=id)
        money_form = MoneyForm(request.POST, instance=money)
        if money_form.is_valid():
            money_form.save()
            return redirect(to='/app/passbook')
    context = {
        "money" : money,
    }
    return render(request, 'app/update.html', context)

def delete(request, id):
    money = get_object_or_404(Money, pk=id)
    money.delete()
    moneys = Money.objects.all()
    context = { "moneys" : moneys }
    return redirect('app:passbook')

def new1(request):
    if request.method == "POST":
        want_form = WantForm(request.POST)
        if want_form.is_valid():
            want_form.save()
            wants = Want.objects.all()
            context = { "wants" : wants }
            return redirect("app:want")
    want_form = WantForm()
    context = { "want_form" : want_form }
    return render(request, 'app/new1.html', context)

def edit1(request, id):
    want = get_object_or_404(Want, pk=id)
    want_form = WantForm(instance=want)
    context = {
        "want" : want,
        "want_form" : want_form,
    }
    return render(request, 'app/edit1.html', context)
    
def update1(request, id):
    if request.method == "POST":
        want =get_object_or_404(Want, pk=id)
        want_form = WantForm(request.POST, instance=want)
        if want_form.is_valid():
            want_form.save()
            return redirect(to='/app/want')
    context = {
        "want" : want,
    }
    return render(request, 'app/update1.html', context)

def delete1(request, id):
    want = get_object_or_404(Want, pk=id)
    want.delete()
    wants = Want.objects.all()
    context = { "wants" : wants }
    return redirect("app:want")