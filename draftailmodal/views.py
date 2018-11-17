from wagtail.admin.modal_workflow import render_modal_workflow


def chooser(request):
    return render_modal_workflow(
        request, 'draftailmodal/chooser.html', None, {})
