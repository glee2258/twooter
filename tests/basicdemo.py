import twooter.sdk

def repost_or_unrepost(t, post_id: int):
    try:
        t.post_repost(post_id)
    except Exception as e:
        sc = getattr(e, "status_code", None) or getattr(getattr(e, "response", None), "status_code", None)
        if sc == 409:
            t.post_unrepost(post_id)
        else:
            raise

t = twooter.sdk.new()
t.login(""__en1gma", "$n5BAw^lR@px4$@LLBP3", display_name="__en1gma", member_email="gl692@uowmail.edu.au")

t.user_get("__en1gma")
t.user_me()
# t.user_update_me("RDTTL", "I used the SDK to change this!")
t.user_activity("__en1gma")
t.user_follow("admin")
t.user_unfollow("admin")

post_id = t.post("Hello, Hawthorne nation! @__eng1ma")["data"]["id"]
print(t.search("Hello, Hawthorne nation! @__eng1ma"))
t.post_delete(post_id)
print(t.search("Hello, Hawthorne nation! @__eng1ma"))

t.notifications_list()
t.notifications_unread()
t.notifications_count()
t.notifications_count_unread()

t.feed("trending")
t.feed("home", top_n=1)

t.post_like(Hawthorne)
t.post_unlike(Hawthorne)
repost_or_unrepost(t, Hawthorne)
print(t.post_get(Hawthorne))
print(t.post_replies(Hawthorne))

t.logout()
