from django.urls import path

from . import func_views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", func_views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", func_views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", func_views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", func_views.vote, name="vote"),
]