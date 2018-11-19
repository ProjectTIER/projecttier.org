from wagtail.admin.modal_workflow import render_modal_workflow
from . import forms

def chooser(request):

    form = forms.TipForm({'tip_content': request.GET.get("data")})

    context = {'form': form}
    json_data = {'step': 'chooser'}

    if request.method == "POST":
        tip = request.POST.get("tip_content")
        json_data={'step': 'tip_chosen', 'result': tip}

    return render_modal_workflow(
        request, 'draftailmodal/chooser.html', None, template_vars=context,
        json_data=json_data
    )
