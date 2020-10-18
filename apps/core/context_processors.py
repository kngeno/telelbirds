from django.conf import settings


def third_party_tracking_ids(request):
    """
    Retrieve 3rd-party tracking IDs from the settings file and add them to the
    request context.
    """
    return {
        'google_analytics_tracking_id': settings.GOOGLE_ANALYTICS_TRACKING_ID,
        'intercom_app_id': settings.INTERCOM_APP_ID,
        'addthis_publisher_id': settings.ADDTHIS_PUBLISHER_ID,
    }


def site_info(request):
    """
    Return site-related information.
    """
    return {
        'site_name': settings.SITE_NAME,
        'site_domain': settings.SITE_DOMAIN,
    }