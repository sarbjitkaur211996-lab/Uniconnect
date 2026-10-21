
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
