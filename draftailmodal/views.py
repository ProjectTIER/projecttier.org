import json
from wagtail.admin.modal_workflow import render_modal_workflow
from . import forms


"""
View that handles the ModalWorkflow stuff on the back-end.
It takes arbitrary URL params and returns JSON that Draftail can use.

Undocumented Wagtail stuff, but you can see some example chooser views here:
https://github.com/wagtail/wagtail/blob/master/wagtail/admin/views/chooser.py
"""
def chooser(request):
    json_data = {'step': 'chooser'}  # default "step"

    if request.GET.get("data"):
        # A tip is being edited, fill in the form
        form = forms.TipForm({
            'tip_content': request.GET.get("data"),
            'color': request.GET.get("color"),
            'entity_key': request.GET.get("entityKey")
        })
    else:
        # Create an empty form
        form = forms.TipForm()

    # Form has been submitted - same for editing and creating a new tip
    if request.method == "POST":
        tip = request.POST.get("tip_content")
        json_data={
            'step': 'tip_chosen',
            'result': json.loads(tip),
            'entityKey': request.POST.get("entity_key"),
            'color': request.POST.get("color"),
        }

    # Render the JSON data!
    return render_modal_workflow(
        request,
        'draftailmodal/chooser.html',
        None,
        template_vars={'form': form},
        json_data=json_data
    )
