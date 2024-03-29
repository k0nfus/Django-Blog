from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    AboutPageView,
    ProjektePageView,
    )

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("", BlogListView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("projekte", ProjektePageView.as_view(), name="projekte"),
]
