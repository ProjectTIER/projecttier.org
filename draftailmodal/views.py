from wagtail.admin.modal_workflow import render_modal_workflow


def chooser(request):

    if request.method == "POST":
        tip = request.POST.get("tip-content")

        return render_modal_workflow(
            request, 'draftailmodal/chooser.html', None, {},
            json_data={'step': 'tip_chosen', 'result': tip}
        )


    return render_modal_workflow(
        request, 'draftailmodal/chooser.html', None, {},
        json_data={'step': 'chooser'}
    )
