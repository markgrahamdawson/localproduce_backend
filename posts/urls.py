from django.urls import path

from .views import SiteList, SiteDetail, PostList, PostDetail, SiteDetailExtended, ItemList, ItemDetail

urlpatterns = [
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("post/",PostList.as_view(), name="post_list"),
    path("site/<int:pk>/", SiteDetail.as_view(), name="site_detail"),
    path("site/",SiteList.as_view(), name="site_list"),
    path("site_extended/<int:pk>/", SiteDetailExtended.as_view(), name="post_detail_extended"),
    path("item/<int:pk>/", ItemDetail.as_view(), name="item_detail"),
    path("item/",ItemList.as_view(), name="item_list")
]