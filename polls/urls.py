from django.urls import path

import polls.views as views

urlpatterns = [
    path('polls/', views.PollsList.as_view(), name='polls_view'),
    path('polls/<int:polls_id>/question',
         views.PollsDetail.as_view(), name='question_view'),
    path('polls/answer_save', views.AnswerSaveView.as_view(),
         name='answer_save_view'),
    path('polls/<int:user_id>/statistic',
         views.StatisticUserViewView.as_view(), name='statistic_view'),
]
