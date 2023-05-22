from django.urls import path

from .views import (
   PostList, PostDetail, PostCreate,
   PostUpdate, PostDelete, NewComment,
   CommentList, CommentDetail
   )


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('comment/', NewComment.as_view(), name='comment'),
   path('comments/', CommentList.as_view(), name='comments'),
   path('comment/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
]