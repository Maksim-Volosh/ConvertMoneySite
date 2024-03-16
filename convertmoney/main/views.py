from django.shortcuts import render
from .forms import CurrencyForm
from .pars import check_status, get_curr_value

def index(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            curr = float(form.cleaned_data['curr'])
            from_curr = form.cleaned_data['from_curr']
            to_curr = form.cleaned_data['to_curr']
            
            status = check_status()
            if not status:
                errors = "At the moment, the server is not responding..."
                return render(request, 'main/index.html', {"form": form, "errors": errors})
            
            from_curr_value = get_curr_value(from_curr)
            to_curr_value = get_curr_value(to_curr)
            if not (isinstance(curr, str) and isinstance(from_curr, str) and isinstance(to_curr, str)):
                result = round((to_curr_value / from_curr_value) * curr, 2)
                converted = f"{result} {to_curr} "
                return render(request, 'main/index.html', {"form": form, "result": converted})
            else:
                errors = "At the moment, the server is not responding..."
                return render(request, 'main/index.html', {"form": form, "errors": errors})

    else:
        form = CurrencyForm()
        
    return render(request, 'main/index.html', {"form": form})
