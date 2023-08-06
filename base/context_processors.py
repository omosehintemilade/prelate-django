from base.forms import NewsletterSubscriberForm


def footer_form(request):
    return {'subscribe_form': NewsletterSubscriberForm()}
