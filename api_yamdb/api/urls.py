from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    GetJWTokenView, ReviewViewSet, SignUpView, TitleViewSet,
                    UserViewSet)

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="admin_users")
router.register("titles", TitleViewSet, basename="titles")
router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register(
    r"^titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename="review",
)
router.register(
    r"^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comment",
)
auth = [
    path("token/", GetJWTokenView.as_view(), name="get_jwtoken"),
    path("signup/", SignUpView.as_view(), name="sign_up"),
]

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/", include(auth)),
]
