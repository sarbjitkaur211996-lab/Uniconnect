
import streamlit as st

st.set_page_config(
    page_title="UniConnect",
    page_icon="🌐"
)

if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "user": "Simmi",
            "message": "Welcome to UniConnect!",
            "likes": 0
        },
        {
            "user": "Gurpreet",
            "message": "Learning Python is fun!",
            "likes": 2
        }
    ]

if "liked" not in st.session_state:
    st.session_state.liked = set()

st.title("🌐 UniConnect")
st.caption("Connect • Share • Discover")

page = st.sidebar.radio(
    "Menu",
    ["Home Feed", "My Profile", "Create Post"]
)

if page == "Home Feed":
    st.header("🏠 Home Feed")

    for i, post in enumerate(st.session_state.posts):
        with st.container(border=True):
            st.subheader("👤 " + post["user"])
            st.write(post["message"])
            st.write("❤️ Likes:", post["likes"])

            if i not in st.session_state.liked:
                if st.button("Like", key=f"like_{i}"):
                    post["likes"] += 1
                    st.session_state.liked.add(i)
                    st.rerun()
            else:
                st.caption("You liked this post")

elif page == "My Profile":
    st.header("👤 My Profile")
    st.subheader("Simmi")
    st.write("Building my first social media app!")

    st.write(
        "My posts:",
        sum(p["user"] == "Simmi"
            for p in st.session_state.posts)
    )

else:
    st.header("✍️ Create Post")
    message = st.text_area("What do you want to share?")

    if st.button("Publish Post"):
        if message.strip():
            st.session_state.posts.insert(
                0,
                {
                    "user": "Simmi",
                    "message": message.strip(),
                    "likes": 0
                }
            )
            st.success("Post published!")
        else:
            st.warning("Please write a post first.")
# -------- UNICONNECT PHOTO POSTS --------

import streamlit as st

# Create a place to store posts for this session
if "photo_posts" not in st.session_state:
    st.session_state.photo_posts = []

st.divider()
st.header("📸 UniConnect Photo Feed")
st.write("Share your campus moments with other students!")

# User details
student_name = st.text_input(
    "Your name",
    key="photo_student_name"
)

# Choose a photo
uploaded_photo = st.file_uploader(
    "Choose a photo",
    type=["jpg", "jpeg", "png", "webp"],
    key="photo_upload"
)

# Write a caption
caption = st.text_input(
    "Write a caption",
    placeholder="What would you like to share?",
    key="photo_caption"
)

# Preview the selected photo
if uploaded_photo is not None:
    st.image(
        uploaded_photo,
        caption="Photo preview",
        use_container_width=True
    )

# Publish the post
if st.button("🚀 Publish Post", key="publish_photo"):
    if not student_name.strip():
        st.warning("Please enter your name.")
    elif uploaded_photo is None:
        st.warning("Please select a photo first.")
    else:
        st.session_state.photo_posts.insert(
            0,
            {
                "name": student_name.strip(),
                "caption": caption.strip(),
                "image": uploaded_photo.getvalue()
            }
        )
        st.success("Your photo post has been published!")

# Display the feed
st.subheader("Latest Posts")

if not st.session_state.photo_posts:
    st.info("No photo posts yet. Be the first to share!")

for post in st.session_state.photo_posts:
    with st.container(border=True):
        st.markdown(f"**👤 {post['name']}**")

        if post["caption"]:
            st.write(post["caption"])

        st.image(
            post["image"],
            use_container_width=True
        )
