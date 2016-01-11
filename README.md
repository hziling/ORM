ORM
===
ORM for sqlite3 like Django ORM.

Usage:
-----
    from datetime import datetime
    import database

    db = database.Sqlite('blog.db')

    class Post(db.Model):
        title = database.CharField(20)
        content = database.TextField()
        created_time = database.DateTimeField()

    db.create_table(Post)

    post = Post(title='post title', content='post content', created_time=datetime.now())
    post.save()
    
    post.id, post.title, post.content
    Out: (5, 'post title', 'post content', datetime.datetime(2016, 1, 6, 17, 25, 37, 342000))
    
    print Post.select().where(id=5).all()
    Out: [<Post post title>]

The ManyToManyField just like Django ManyToManyField:

    class Tag(db.Model):
        name = database.CharField(50)
        posts = database.ManyToManyField(Post)

When create table from class `Tag`, ORM will auto-create a table `post_tag` which referenced `Post` and `Tag`.
We can add tag to the post like this:

    tag = Tag(name='tag')
    tag.save()
    
    post.tags.add(tag)
    post.tags.all()
    Out: [<Tag tag>]