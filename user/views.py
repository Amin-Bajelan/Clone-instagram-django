from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, Post, Comment, Follow, FollowRequest
from django.contrib.auth import logout, login
from .forms import UserForm, ProfileEditForm, AddPostForm

# Create your views here.
account_owner = ''
user = ''


def index(request):
    my_user = request.user

    global user
    if request.method == 'POST':
        value_input_search = request.POST.get('search_input')
        all_users = UserProfile.objects.filter(username__icontains=value_input_search)
        for i in all_users:
            print(i.username)
        return render(request, 'user/show_profiles.html', {'users': all_users})

    return render(request, 'user/index.html', {'user': user})


def first_page(request):
    return render(request, "user/first_page.html")


def signup(request):
    global account_owner

    if request.method == "POST":
        try:
            form = UserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                if '@' in username:
                    form = UserForm()
                    messages.error(request, 'the username cant contain @')
                    return render(request, 'user/signup.html', {'form': form})
                else:
                    form.save()
                    account_owner = UserProfile.objects.get(username=username)
                    print(account_owner)
                    messages.success(request, 'Your account has been created!')
                    return redirect('first_page')
        except:
            form = UserForm()
            messages.error(request, 'Something went wrong')
            return render(request, 'user/signup.html', {'form': form})
    form = UserForm()
    return render(request, 'user/signup.html', {'form': form})


def login(request):
    global account_owner
    global user
    flag = int(1)
    if request.method == 'POST':
        try:
            username_or_email = request.POST.get('username')
            password = request.POST.get('password')
            if '@' in username_or_email:
                form = UserProfile.objects.get(email=username_or_email)
                flag = 1
            else:
                form = UserProfile.objects.get(username=username_or_email)
                flag = 0
            if form.password == password:
                if flag == 1:
                    account_owner = UserProfile.objects.get(email=username_or_email)
                else:
                    account_owner = UserProfile.objects.get(username=username_or_email)
                messages.success(request, 'You Logged In successfully')
                user = account_owner.username
                return redirect('index')
            else:
                messages.error(request, 'Your password is incorrect')
                return render(request, 'user/login.html')

        except:
            messages.error(request, 'Something went wrong your username or password is incorrect.')
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html', )


def logout(request):
    global account_owner
    global user
    account_owner = ''
    user = 'katsuhero'
    request.session.flush()
    messages.success(request, 'You Logged out successfully')
    return redirect('first_page')


def profile(request):
    global user
    global account_owner
    user_info = UserProfile.objects.get(username=user)
    posts = Post.objects.filter(user=account_owner)
    show_posts = True
    my_account = True
    return render(request, 'user/profile.html', locals())


def edit_profile(request):
    global user
    if request.method == 'POST':
        try:
            form = ProfileEditForm(request.POST, request.FILES)
            if form.is_valid():
                object_user = UserProfile.objects.get(username=user)

                password = form.cleaned_data['password']
                bio = form.cleaned_data['bio']
                profile_pic = form.cleaned_data['profile_picture']
                object_user.password = password
                object_user.bio = bio
                object_user.profile_picture = profile_pic
                object_user.save()
                messages.success(request, 'Your Profile has been updated')
                return redirect('profile')
        except:
            form = ProfileEditForm()
            messages.error(request, 'Something went wrong')
            return render(request, "user/edit_profile.html", {'form': form})

    form = ProfileEditForm()
    return render(request, "user/edit_profile.html", {'form': form})


def add_post(request):
    global user
    global account_owner
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            caption = form.cleaned_data['caption']
            print(caption)
            object_post = Post.objects.create(user=account_owner, image=image, caption=caption)
            print(object_post)
            object_post.save()
            obj_user = UserProfile.objects.get(username=user)
            obj_user.post_count += 1
            return redirect('index')

    form = AddPostForm()
    return render(request, "user/add_post.html", {'form': form})


# for when you search for user and click on username
def show_user_profiles(request, user_id):
    global account_owner
    global user
    user_info = UserProfile.objects.get(id=user_id)
    posts = Post.objects.filter(user=user_id)

    object_follow = Follow.objects.filter(follower=account_owner)
    show_posts = False
    my_account = False
    if account_owner == user_info:
        show_posts = True
        my_account = True
    elif user_info.is_private == False:
        show_posts = True
    else:
        for i in object_follow:
            if i.following == user_info:
                show_posts = True
                my_account = True

    return render(request, 'user/profile.html', locals())


def like_post(request, post_id):
    global user
    global account_owner
    post = Post.objects.get(id=post_id)
    if account_owner in post.liked_by.all():
        post.liked_by.remove(account_owner)
        post.likes -= 1
    else:
        post.liked_by.add(account_owner)
        post.likes += 1

    post.save()
    print(post.likes)
    return redirect('profile')


def comment_post(request, post_id):
    global user
    global account_owner
    user_comment = request.POST.get('comment')
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(user=account_owner, post=post, text=user_comment)
    print(comment)
    comment.save()
    return redirect('profile')


def show_comments(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    for comment in comments:
        print(comment.text)
    return render(request, 'user/show_comment.html', {'comments': comments})


# accept user follow request
def create_follow_user(request, message_id):
    request_follow = FollowRequest.objects.get(id=message_id)
    sender_follow = request_follow.sender
    receiver_follow = request_follow.receiver
    sender_follow.following += 1
    print(sender_follow.following)
    receiver_follow.followers += 1
    print(receiver_follow.following)
    obj_follow = Follow.objects.create(follower=sender_follow, following=receiver_follow)
    obj_follow.save()
    sender_follow.save()
    receiver_follow.save()
    request_follow.delete()
    return redirect('show_follow_request')


# reject follow request
def delete_follow_user(request, message_id):
    request_follow = FollowRequest.objects.get(id=message_id)
    request_follow.delete()
    return redirect('show_follow_request')


# for show message on messages on index page
def show_follow_request(request):
    global account_owner
    messages = FollowRequest.objects.filter(receiver=account_owner)
    return render(request, 'user/show_messages.html', locals())


def follow_user_request(request, user_id):
    global account_owner
    user_sender = UserProfile.objects.get(id=user_id)
    object_request = FollowRequest.objects.create(sender=account_owner, receiver=user_sender)
    object_request.save()
    return redirect('index')

def show_follow(request,user_id):
    user_info = UserProfile.objects.get(id=user_id)
    followers = Follow.objects.filter(follower=user_info)
    followings = Follow.objects.filter(following=user_info)
    for i in followers:
        print(i.following.username)
    return render(request,'user/show_follows.html',locals())

