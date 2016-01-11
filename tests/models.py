import database


class Post(database.Model):
    title = database.CharField(max_lenth=100)
    content = database.TextField()
    pub_date = database.DateTimeField()

    author_id = database.ForeignKeyField('author')

    class Meta:
        db_table = 'my_post'

    def __repr__(self):
        return '<Post {0}>'.format(self.title)


class Author(database.Model):
    id = database.PrimaryKeyField()
    name = database.CharField(max_lenth=20)

    posts = database.ForeignKeyReverseField('my_post')

    def __repr__(self):
        return '<Author {0}>'.format(self.name)


class Tag(database.Model):
    id = database.PrimaryKeyField()
    name = database.CharField(100)

    posts = database.ManyToManyField(Post)

    def __repr__(self):
        return '<Tag {0}>'.format(self.name)