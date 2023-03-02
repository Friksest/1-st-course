
posts = [
  {
    "title": "About the importance of functional programming",
    "body": "Functional programming is ....." 
  },
  {
    "title": "OOP programming brings classes and objects into the code",
    "body": "OOP is  ....." 
  },
]

def addPost(postList, postTitle, postBody):
    newPost = {"title": postTitle, "body": postBody}
    postList.insert(0, newPost)
    

addPost(posts, "New post title", "New post body")


# This will add a new post to the beginning of the posts list. 
# Note that the function does not return anything, 
# but it modifies the postList parameter in place.


