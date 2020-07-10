from django.shortcuts import redirect,render

def isauthentication(view_func):
    def wrapper_func(request,*args, **kwargs):

        if request.user.is_authenticated:
            return redirect("home")

        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func


def allowed(allowed_roles= []):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)

            else:
                return render(request, 'blogapp/allow.html')

        return wrapper_func

    return decorators