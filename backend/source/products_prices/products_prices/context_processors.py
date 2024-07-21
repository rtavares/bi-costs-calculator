import datetime
import git
from django.conf import settings


def date_context_processor(request):
    current_datetime = datetime.datetime.now()
    repo = git.Repo('.', search_parent_directories=True)

    return {
        'current_year': current_datetime.year,
        'active_branch': repo.active_branch.name
    }