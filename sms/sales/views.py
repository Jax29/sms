from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer


def listorders(request):

    return render(request, 'orders.html', {})


def listcustomers(request):

    qs = Customer.objects.values()
    # 检查url中是否有参数phonenumber：
    ph = request.GET.get('phonenumber', None)
    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)
    # 定义返回字符串
    reStr = ''
    for customer in qs:
        for name, value in customer.items():
            reStr += f'{name}: {value} |'

        reStr += '<br/>'
    return HttpResponse(reStr)
