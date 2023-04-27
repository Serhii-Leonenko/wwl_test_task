from django.urls import path

from core.views import (
    TaskListView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
    task_status_change,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/change_status/", task_status_change, name="task-status-change"),
]

app_name = "core"
