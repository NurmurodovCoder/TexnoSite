from django.shortcuts import render, redirect
from .models import Post, Category, Author, Carusel, CommentPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from .forms import PostForm, PostFormCreated


def post(request):
    carusel = Carusel.objects.filter(is_active=True)

    new_posts = Post.objects.all().order_by("-id")[:6]

    top_like = Post.objects.all().order_by("like")[:6]

    last_web = Post.objects.filter(category__name="Web dasturlsh").order_by("-id")[
        1:7
    ]  # web-------
    last_one_web = Post.objects.filter(category__name="Web dasturlsh").last()

    last_mob = Post.objects.filter(category__name="Mobil dasturlash").order_by("-id")[
        1:7
    ]  # mobil
    last_one_mob = Post.objects.filter(category__name="Mobil dasturlash").last()

    last_it = Post.objects.filter(category__name="IT tehnologiyalar").order_by("-id")[
        1:7
    ]  # it texno
    last_one_it = Post.objects.filter(category__name="IT tehnologiyalar").last()

    last_ai = Post.objects.filter(category__name="Ai, Game, DevOps ...").order_by(
        "-id"
    )[
        1:7
    ]  # Ai, Game, DevOps ...
    last_one_ai = Post.objects.filter(category__name="Ai, Game, DevOps ...").last()

    context = {
        "carusel": carusel,
        "new_posts": new_posts,
        "top_like": top_like,
        "last_web": last_web,
        "last_one_web": last_one_web,
        "last_mob": last_web,
        "last_one_mob": last_one_web,
        "last_it": last_web,
        "last_one_it": last_one_web,
        "last_ai": last_web,
        "last_one_ai": last_one_web,
    }
    return render(request, "index.html", context)
    # return render(request, 'users/base.html', context)


def post_get(request, id):
    post = Post.objects.get(id=id)
    category = Category.objects.all()
    comment = CommentPost.objects.filter(post_id=post.id)
    post_cat = Post.objects.filter(category=post.category).order_by("-id")[:10]

    hit_count = get_hitcount_model().objects.get_for_object(post)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    if hit_count_response.hit_counted:
        hits += 1

    if request.method == "POST":
        user = request.user
        text = request.POST["text"]
        comment = CommentPost(text=text, post_id=post.id, user=user).save()
        messages.success(request, "Comment yozildi !")
        return redirect("post_get", id=post.id)

    elif "like" in request.GET:
        post.like.add(request.user)
        post.save()

        return redirect("post_get", id=post.id)
    elif "no-like" in request.GET:
        messages.error  (request, "Royhatdan o`ting yoki tizimga kiring !")

    context = {
        "post": post,
        "last_it": post_cat,
        "category": category,
        "comment": comment,
        "hits": hits,
    }
    return render(request, "pages/single_page.html", context)


@login_required(login_url="user_login")
def post_edit(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Maqola o`zgartirildi")
            return redirect("post_get", id=id)
        else:
            messages.error(request, "Xatoliklar bor. Qayta urinib ko`ring !")
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "edit_post.html", context)


@login_required(login_url="user_login")
def post_create(request):
    user = request.user
    form_create = PostFormCreated()
    if request.method == "POST":
        form_create = PostFormCreated(request.POST, request.FILES)
        if form_create.is_valid():
            article = form_create.save(commit=False)
            article.author = user
            form_create.save(commit=True)
            messages.success(request, "Maqola yaratildi")
            return redirect("post_get", article.id)
        else:
            messages.error(request, "Maqolada xatolik bor. Qabul qilinmadi !")
    context = {"form_create": form_create}

    return render(request, "edit_post.html", context)


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request, "Maqolada muvaffaqiyatli o`chirildi !")

    return redirect("post")


def category_post(request, category):
    category_post = Post.objects.filter(category__name=category).order_by("-id").all()
    posts = Paginator(category_post, 7)
    page_num = request.GET.get("page")
    page = posts.page(page_num)

    context = {"category_post": page, "category_name": category, "page": page}
    return render(request, "category.html", context)


def search(request):
    if "q" in request.GET:
        q = request.GET["q"]
        search_posts = Post.objects.filter(Q(title__icontains=q) | Q(text__icontains=q))
        # search_post = Paginator(search_posts, 7)
        # page_num = request.GET.get("page")
        # page = search_post.page(page_num)
    else:
        search_posts = None
    return render(
        request, "search.html", {"search_post": search_posts, "q": q, "page": q}
    )
