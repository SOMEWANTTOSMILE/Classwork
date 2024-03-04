from django.urls import path
from blog_app import views


urlpatterns = {
    path('', views.posts_list, name="post_list"),
    path('post/<int:post_id>', views.post_detail, name="post_detail"),
    path('create_post/', views.create_post, name="create_post"),
}
