# Making queries | Django documentation | Django

-   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

-   Language: **en**
-   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/topics/db/queries/)
-   [sv](https://docs.djangoproject.com/sv/6.0/topics/db/queries/)
-   [pt-br](https://docs.djangoproject.com/pt-br/6.0/topics/db/queries/)
-   [pl](https://docs.djangoproject.com/pl/6.0/topics/db/queries/)
-   [ko](https://docs.djangoproject.com/ko/6.0/topics/db/queries/)
-   [ja](https://docs.djangoproject.com/ja/6.0/topics/db/queries/)
-   [it](https://docs.djangoproject.com/it/6.0/topics/db/queries/)
-   [id](https://docs.djangoproject.com/id/6.0/topics/db/queries/)
-   [fr](https://docs.djangoproject.com/fr/6.0/topics/db/queries/)
-   [es](https://docs.djangoproject.com/es/6.0/topics/db/queries/)
-   [el](https://docs.djangoproject.com/el/6.0/topics/db/queries/)

-   Documentation version: **6.0**
-   [dev](https://docs.djangoproject.com/en/dev/topics/db/queries/)
-   [6.1](https://docs.djangoproject.com/en/6.1/topics/db/queries/)
-   [5.2](https://docs.djangoproject.com/en/5.2/topics/db/queries/)
-   [5.1](https://docs.djangoproject.com/en/5.1/topics/db/queries/)
-   [5.0](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
-   [4.2](https://docs.djangoproject.com/en/4.2/topics/db/queries/)
-   [4.1](https://docs.djangoproject.com/en/4.1/topics/db/queries/)
-   [4.0](https://docs.djangoproject.com/en/4.0/topics/db/queries/)
-   [3.2](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
-   [3.1](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
-   [3.0](https://docs.djangoproject.com/en/3.0/topics/db/queries/)
-   [2.2](https://docs.djangoproject.com/en/2.2/topics/db/queries/)
-   [2.1](https://docs.djangoproject.com/en/2.1/topics/db/queries/)
-   [2.0](https://docs.djangoproject.com/en/2.0/topics/db/queries/)
-   [1.11](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
-   [1.10](https://docs.djangoproject.com/en/1.10/topics/db/queries/)
-   [1.9](https://docs.djangoproject.com/en/1.9/topics/db/queries/)
-   [1.8](https://docs.djangoproject.com/en/1.8/topics/db/queries/)

-   [](#top)

# Making queries[¶](#making-queries "Link to this heading")

Once you’ve created your [data models](../models/), Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. This document explains how to use this API. Refer to the [data model reference](../../../ref/models/) for full details of all the various model lookup options.

Throughout this guide (and in the reference), we’ll refer to the following models, which comprise a blog application:

from datetime import date

from django.db import models

class Blog(models.Model):
    name \= models.CharField(max\_length\=100)
    tagline \= models.TextField()

    def \_\_str\_\_(self):
        return self.name

class Author(models.Model):
    name \= models.CharField(max\_length\=200)
    email \= models.EmailField()

    def \_\_str\_\_(self):
        return self.name

class Entry(models.Model):
    blog \= models.ForeignKey(Blog, on\_delete\=models.CASCADE)
    headline \= models.CharField(max\_length\=255)
    body\_text \= models.TextField()
    pub\_date \= models.DateField()
    mod\_date \= models.DateField(default\=date.today)
    authors \= models.ManyToManyField(Author)
    number\_of\_comments \= models.IntegerField(default\=0)
    number\_of\_pingbacks \= models.IntegerField(default\=0)
    rating \= models.IntegerField(default\=5)

    def \_\_str\_\_(self):
        return self.headline

## Creating objects[¶](#creating-objects "Link to this heading")

To represent database-table data in Python objects, Django uses an intuitive system: A model class represents a database table, and an instance of that class represents a particular record in the database table.

To create an object, instantiate it using keyword arguments to the model class, then call [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") to save it to the database.

Assuming models live in a `models.py` file inside a `blog` Django app, here is an example:

\>>> from blog.models import Blog
\>>> b \= Blog(name\="Beatles Blog", tagline\="All the latest Beatles news.")
\>>> b.save()

This performs an `INSERT` SQL statement behind the scenes. Django doesn’t hit the database until you explicitly call [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save").

The [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method has no return value.

See also

[`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") takes a number of advanced options not described here. See the documentation for [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") for complete details.

To create and save an object in a single step, use the [`create()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.create "django.db.models.query.QuerySet.create") method.

## Saving changes to objects[¶](#saving-changes-to-objects "Link to this heading")

To save changes to an object that’s already in the database, use [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save").

Given a `Blog` instance `b5` that has already been saved to the database, this example changes its name and updates its record in the database:

\>>> b5.name \= "New name"
\>>> b5.save()

This performs an `UPDATE` SQL statement behind the scenes. Django doesn’t hit the database until you explicitly call [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save").

### Saving `ForeignKey` and `ManyToManyField` fields[¶](#saving-foreignkey-and-manytomanyfield-fields "Link to this heading")

Updating a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") field works exactly the same way as saving a normal field – assign an object of the right type to the field in question. This example updates the `blog` attribute of an `Entry` instance `entry`, assuming appropriate instances of `Entry` and `Blog` are already saved to the database (so we can retrieve them below):

\>>> from blog.models import Blog, Entry
\>>> entry \= Entry.objects.get(pk\=1)
\>>> cheese\_blog \= Blog.objects.get(name\="Cheddar Talk")
\>>> entry.blog \= cheese\_blog
\>>> entry.save()

Updating a [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") works a little differently – use the [`add()`](../../../ref/models/relations/#django.db.models.fields.related.RelatedManager.add "django.db.models.fields.related.RelatedManager.add") method on the field to add a record to the relation. This example adds the `Author` instance `joe` to the `entry` object:

\>>> from blog.models import Author
\>>> joe \= Author.objects.create(name\="Joe")
\>>> entry.authors.add(joe)

To add multiple records to a [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") in one go, include multiple arguments in the call to [`add()`](../../../ref/models/relations/#django.db.models.fields.related.RelatedManager.add "django.db.models.fields.related.RelatedManager.add"), like this:

\>>> john \= Author.objects.create(name\="John")
\>>> paul \= Author.objects.create(name\="Paul")
\>>> george \= Author.objects.create(name\="George")
\>>> ringo \= Author.objects.create(name\="Ringo")
\>>> entry.authors.add(john, paul, george, ringo)

Django will complain if you try to assign or add an object of the wrong type.

## Retrieving objects[¶](#retrieving-objects "Link to this heading")

To retrieve objects from your database, construct a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") via a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") on your model class.

A [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") represents a collection of objects from your database. It can have zero, one or many _filters_. Filters narrow down the query results based on the given parameters. In SQL terms, a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") equates to a `SELECT` statement, and a filter is a limiting clause such as `WHERE` or `LIMIT`.

You get a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") by using your model’s [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager"). Each model has at least one [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager"), and it’s called [`objects`](../../../ref/models/class/#django.db.models.Model.objects "django.db.models.Model.objects") by default. Access it directly via the model class, like so:

\>>> Blog.objects
<django.db.models.manager.Manager object at ...>
\>>> b \= Blog(name\="Foo", tagline\="Bar")
\>>> b.objects
Traceback:
    ...
AttributeError: "Manager isn't accessible via Blog instances."

Note

A `Manager` is accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations.

The [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") is the main source of querysets for a model. For example, `Blog.objects.all()` returns a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that contains all `Blog` objects in the database.

### Retrieving all objects[¶](#retrieving-all-objects "Link to this heading")

The simplest way to retrieve objects from a table is to get all of them. To do this, use the [`all()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") method on a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager"):

\>>> all\_entries \= Entry.objects.all()

The [`all()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") method returns a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of all the objects in the database.

### Retrieving specific objects with filters[¶](#retrieving-specific-objects-with-filters "Link to this heading")

The [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") returned by [`all()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") describes all objects in the database table. Usually, though, you’ll need to select only a subset of the complete set of objects.

To create such a subset, you refine the initial [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), adding filter conditions. The two most common ways to refine a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") are:

`filter(**kwargs)`

Returns a new [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing objects that match the given lookup parameters.

`exclude(**kwargs)`

Returns a new [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing objects that do _not_ match the given lookup parameters.

The lookup parameters (`**kwargs` in the above function definitions) should be in the format described in [Field lookups](#field-lookups) below.

For example, to get a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of blog entries from the year 2006, use [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") like so:

Entry.objects.filter(pub\_date\_\_year\=2006)

With the default manager class, it is the same as:

Entry.objects.all().filter(pub\_date\_\_year\=2006)

#### Chaining filters[¶](#chaining-filters "Link to this heading")

The result of refining a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is itself a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), so it’s possible to chain refinements together. For example:

\>>> Entry.objects.filter(headline\_\_startswith\="What").exclude(
...     pub\_date\_\_gte\=datetime.date.today()
... ).filter(pub\_date\_\_gte\=datetime.date(2005, 1, 30))

This takes the initial [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of all entries in the database, adds a filter, then an exclusion, then another filter. The final result is a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing all entries with a headline that starts with “What”, that were published between January 30, 2005, and the current day.

#### Filtered `QuerySet`s are unique[¶](#filtered-querysets-are-unique "Link to this heading")

Each time you refine a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), you get a brand-new [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that is in no way bound to the previous [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"). Each refinement creates a separate and distinct [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that can be stored, used and reused.

Example:

\>>> q1 \= Entry.objects.filter(headline\_\_startswith\="What")
\>>> q2 \= q1.exclude(pub\_date\_\_gte\=datetime.date.today())
\>>> q3 \= q1.filter(pub\_date\_\_gte\=datetime.date.today())

These three querysets are separate. The first is a base [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing all entries that contain a headline starting with “What”. The second is a subset of the first, with an additional criteria that excludes records whose `pub_date` is today or in the future. The third is a subset of the first, with an additional criteria that selects only the records whose `pub_date` is today or in the future. The initial [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") (`q1`) is unaffected by the refinement process.

#### `QuerySet`s are lazy[¶](#querysets-are-lazy "Link to this heading")

`QuerySet` objects are lazy – the act of creating a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is _evaluated_. Take a look at this example:

\>>> q \= Entry.objects.filter(headline\_\_startswith\="What")
\>>> q \= q.filter(pub\_date\_\_lte\=datetime.date.today())
\>>> q \= q.exclude(body\_text\_\_icontains\="food")
\>>> print(q)

Though this looks like three database hits, in fact it hits the database only once, at the last line (`print(q)`). In general, the results of a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") aren’t fetched from the database until you “ask” for them. When you do, the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is _evaluated_ by accessing the database. For more details on exactly when evaluation takes place, see [When QuerySets are evaluated](../../../ref/models/querysets/#when-querysets-are-evaluated).

### Retrieving a single object with `get()`[¶](#retrieving-a-single-object-with-get "Link to this heading")

[`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") will always give you a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), even if only a single object matches the query - in this case, it will be a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing a single element.

If you know there is only one object that matches your query, you can use the [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") method on a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") which returns the object directly:

\>>> one\_entry \= Entry.objects.get(pk\=1)

You can use any query expression with [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), just like with [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") - again, see [Field lookups](#field-lookups) below.

Note that there is a difference between using [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), and using [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") with a slice of `[0]`. If there are no results that match the query, [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") will raise a `DoesNotExist` exception. This exception is an attribute of the model class that the query is being performed on - so in the code above, if there is no `Entry` object with a primary key of 1, Django will raise `Entry.DoesNotExist`.

Similarly, Django will complain if more than one item matches the [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") query. In this case, it will raise [`MultipleObjectsReturned`](../../../ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "django.core.exceptions.MultipleObjectsReturned"), which again is an attribute of the model class itself.

### Other `QuerySet` methods[¶](#other-queryset-methods "Link to this heading")

Most of the time you’ll use [`all()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all"), [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") and [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") when you need to look up objects from the database. However, that’s far from all there is; see the [QuerySet API Reference](../../../ref/models/querysets/#queryset-api) for a complete list of all the various [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods.

### Limiting `QuerySet`s[¶](#limiting-querysets "Link to this heading")

Use a subset of Python’s array-slicing syntax to limit your [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") to a certain number of results. This is the equivalent of SQL’s `LIMIT` and `OFFSET` clauses.

For example, this returns the first 5 objects (`LIMIT 5`):

\>>> Entry.objects.all()\[:5\]

This returns the sixth through tenth objects (`OFFSET 5 LIMIT 5`):

\>>> Entry.objects.all()\[5:10\]

Negative indexing (i.e. `Entry.objects.all()[-1]`) is not supported.

Generally, slicing a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") returns a new [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") – it doesn’t evaluate the query. An exception is if you use the “step” parameter of Python slice syntax. For example, this would actually execute the query in order to return a list of every _second_ object of the first 10:

\>>> Entry.objects.all()\[:10:2\]

Further filtering or ordering of a sliced queryset is prohibited due to the ambiguous nature of how that might work.

To retrieve a _single_ object rather than a list (e.g. `SELECT foo FROM bar LIMIT 1`), use an index instead of a slice. For example, this returns the first `Entry` in the database, after ordering entries alphabetically by headline:

\>>> Entry.objects.order\_by("headline")\[0\]

This is roughly equivalent to:

\>>> Entry.objects.order\_by("headline")\[0:1\].get()

Note, however, that the first of these will raise `IndexError` while the second will raise `DoesNotExist` if no objects match the given criteria. See [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") for more details.

### Field lookups[¶](#field-lookups "Link to this heading")

Field lookups are how you specify the meat of an SQL `WHERE` clause. They’re specified as keyword arguments to the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") and [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").

Basic lookups keyword arguments take the form `field__lookuptype=value`. (That’s a double-underscore). For example:

\>>> Entry.objects.filter(pub\_date\_\_lte\="2006-01-01")

translates (roughly) into the following SQL:

SELECT \* FROM blog\_entry WHERE pub\_date <= '2006-01-01';

How this is possible

Python has the ability to define functions that accept arbitrary name-value arguments whose names and values are evaluated at runtime. For more information, see [Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#tut-keywordargs "(in Python v3.14)") in the official Python tutorial.

The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") you can specify the field name suffixed with `_id`. In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key. For example:

\>>> Entry.objects.filter(blog\_id\=4)

If you pass an invalid keyword argument, a lookup function will raise `TypeError`.

The database API supports about two dozen lookup types; a complete reference can be found in the [field lookup reference](../../../ref/models/querysets/#field-lookups). To give you a taste of what’s available, here’s some of the more common lookups you’ll probably use:

[`exact`](../../../ref/models/querysets/#std-fieldlookup-exact)

An “exact” match. For example:

\>>> Entry.objects.get(headline\_\_exact\="Cat bites dog")

Would generate SQL along these lines:

SELECT ... WHERE headline \= 'Cat bites dog';

If you don’t provide a lookup type – that is, if your keyword argument doesn’t contain a double underscore – the lookup type is assumed to be `exact`.

For example, the following two statements are equivalent:

\>>> Blog.objects.get(id\_\_exact\=14)  \# Explicit form
\>>> Blog.objects.get(id\=14)  \# \_\_exact is implied

This is for convenience, because `exact` lookups are the common case.

[`iexact`](../../../ref/models/querysets/#std-fieldlookup-iexact)

A case-insensitive match. So, the query:

\>>> Blog.objects.get(name\_\_iexact\="beatles blog")

Would match a `Blog` titled `"Beatles Blog"`, `"beatles blog"`, or even `"BeAtlES blOG"`.

[`contains`](../../../ref/models/querysets/#std-fieldlookup-contains)

Case-sensitive containment test. For example:

Entry.objects.get(headline\_\_contains\="Lennon")

Roughly translates to this SQL:

SELECT ... WHERE headline LIKE '%Lennon%';

Note this will match the headline `'Today Lennon honored'` but not `'today lennon honored'`.

There’s also a case-insensitive version, [`icontains`](../../../ref/models/querysets/#std-fieldlookup-icontains).

[`startswith`](../../../ref/models/querysets/#std-fieldlookup-startswith), [`endswith`](../../../ref/models/querysets/#std-fieldlookup-endswith)

Starts-with and ends-with search, respectively. There are also case-insensitive versions called [`istartswith`](../../../ref/models/querysets/#std-fieldlookup-istartswith) and [`iendswith`](../../../ref/models/querysets/#std-fieldlookup-iendswith).

Again, this only scratches the surface. A complete reference can be found in the [field lookup reference](../../../ref/models/querysets/#field-lookups).

### Lookups that span relationships[¶](#lookups-that-span-relationships "Link to this heading")

Django offers a powerful and intuitive way to “follow” relationships in lookups, taking care of the SQL `JOIN`s for you automatically, behind the scenes. To span a relationship, use the field name of related fields across models, separated by double underscores, until you get to the field you want.

This example retrieves all `Entry` objects with a `Blog` whose `name` is `'Beatles Blog'`:

\>>> Entry.objects.filter(blog\_\_name\="Beatles Blog")

This spanning can be as deep as you’d like.

It works backwards, too. While it [`can be customized`](../../../ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name"), by default you refer to a “reverse” relationship in a lookup using the lowercase name of the model.

This example retrieves all `Blog` objects which have at least one `Entry` whose `headline` contains `'Lennon'`:

\>>> Blog.objects.filter(entry\_\_headline\_\_contains\="Lennon")

If you are filtering across multiple relationships and one of the intermediate models doesn’t have a value that meets the filter condition, Django will treat it as if there is an empty (all values are `NULL`), but valid, object there. All this means is that no error will be raised. For example, in this filter:

Blog.objects.filter(entry\_\_authors\_\_name\="Lennon")

(if there was a related `Author` model), if there was no `author` associated with an entry, it would be treated as if there was also no `name` attached, rather than raising an error because of the missing `author`. Usually this is exactly what you want to have happen. The only case where it might be confusing is if you are using [`isnull`](../../../ref/models/querysets/#std-fieldlookup-isnull). Thus:

Blog.objects.filter(entry\_\_authors\_\_name\_\_isnull\=True)

will return `Blog` objects that have an empty `name` on the `author` and also those which have an empty `author` on the `entry`. If you don’t want those latter objects, you could write:

Blog.objects.filter(entry\_\_authors\_\_isnull\=False, entry\_\_authors\_\_name\_\_isnull\=True)

#### Spanning multi-valued relationships[¶](#spanning-multi-valued-relationships "Link to this heading")

When spanning a [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") or a reverse [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") (such as from `Blog` to `Entry`), filtering on multiple attributes raises the question of whether to require each attribute to coincide in the same related object. We might seek blogs that have an entry from 2008 with _“Lennon”_ in its headline, or we might seek blogs that merely have any entry from 2008 as well as some newer or older entry with _“Lennon”_ in its headline.

To select all blogs containing at least one entry from 2008 having _“Lennon”_ in its headline (the same entry satisfying both conditions), we would write:

Blog.objects.filter(entry\_\_headline\_\_contains\="Lennon", entry\_\_pub\_date\_\_year\=2008)

Otherwise, to perform a more permissive query selecting any blogs with merely _some_ entry with _“Lennon”_ in its headline and _some_ entry from 2008, we would write:

Blog.objects.filter(entry\_\_headline\_\_contains\="Lennon").filter(
    entry\_\_pub\_date\_\_year\=2008
)

Suppose there is only one blog that has both entries containing _“Lennon”_ and entries from 2008, but that none of the entries from 2008 contained _“Lennon”_. The first query would not return any blogs, but the second query would return that one blog. (This is because the entries selected by the second filter may or may not be the same as the entries in the first filter. We are filtering the `Blog` items with each filter statement, not the `Entry` items.) In short, if each condition needs to match the same related object, then each should be contained in a single [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") call.

Note

As the second (more permissive) query chains multiple filters, it performs multiple joins to the primary model, potentially yielding duplicates.

\>>> from datetime import date
\>>> beatles \= Blog.objects.create(name\="Beatles Blog")
\>>> pop \= Blog.objects.create(name\="Pop Music Blog")
\>>> Entry.objects.create(
...     blog\=beatles,
...     headline\="New Lennon Biography",
...     pub\_date\=date(2008, 6, 1),
... )
<Entry: New Lennon Biography>
\>>> Entry.objects.create(
...     blog\=beatles,
...     headline\="New Lennon Biography in Paperback",
...     pub\_date\=date(2009, 6, 1),
... )
<Entry: New Lennon Biography in Paperback>
\>>> Entry.objects.create(
...     blog\=pop,
...     headline\="Best Albums of 2008",
...     pub\_date\=date(2008, 12, 15),
... )
<Entry: Best Albums of 2008>
\>>> Entry.objects.create(
...     blog\=pop,
...     headline\="Lennon Would Have Loved Hip Hop",
...     pub\_date\=date(2020, 4, 1),
... )
<Entry: Lennon Would Have Loved Hip Hop>
\>>> Blog.objects.filter(
...     entry\_\_headline\_\_contains\="Lennon",
...     entry\_\_pub\_date\_\_year\=2008,
... )
<QuerySet \[<Blog: Beatles Blog>\]>
\>>> Blog.objects.filter(
...     entry\_\_headline\_\_contains\="Lennon",
... ).filter(
...     entry\_\_pub\_date\_\_year\=2008,
... )
<QuerySet \[<Blog: Beatles Blog>, <Blog: Beatles Blog>, <Blog: Pop Music Blog\]>

Note

The behavior of [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") for queries that span multi-value relationships, as described above, is not implemented equivalently for [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude"). Instead, the conditions in a single [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") call will not necessarily refer to the same item.

For example, the following query would exclude blogs that contain _both_ entries with _“Lennon”_ in the headline _and_ entries published in 2008:

Blog.objects.exclude(
    entry\_\_headline\_\_contains\="Lennon",
    entry\_\_pub\_date\_\_year\=2008,
)

However, unlike the behavior when using [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), this will not limit blogs based on entries that satisfy both conditions. In order to do that, i.e. to select all blogs that do not contain entries published with _“Lennon”_ that were published in 2008, you need to make two queries:

Blog.objects.exclude(
    entry\_\_in\=Entry.objects.filter(
        headline\_\_contains\="Lennon",
        pub\_date\_\_year\=2008,
    ),
)

### Filters can reference fields on the model[¶](#filters-can-reference-fields-on-the-model "Link to this heading")

In the examples given so far, we have constructed filters that compare the value of a model field with a constant. But what if you want to compare the value of a model field with another field on the same model?

Django provides [`F expressions`](../../../ref/models/expressions/#django.db.models.F "django.db.models.F") to allow such comparisons. Instances of `F()` act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.

For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an `F()` object to reference the pingback count, and use that `F()` object in the query:

\>>> from django.db.models import F
\>>> Entry.objects.filter(number\_of\_comments\_\_gt\=F("number\_of\_pingbacks"))

Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with `F()` objects, both with constants and with other `F()` objects. To find all the blog entries with more than _twice_ as many comments as pingbacks, we modify the query:

\>>> Entry.objects.filter(number\_of\_comments\_\_gt\=F("number\_of\_pingbacks") \* 2)

To find all the entries where the rating of the entry is less than the sum of the pingback count and comment count, we would issue the query:

\>>> Entry.objects.filter(rating\_\_lt\=F("number\_of\_comments") + F("number\_of\_pingbacks"))

You can also use the double underscore notation to span relationships in an `F()` object. An `F()` object with a double underscore will introduce any joins needed to access the related object. For example, to retrieve all the entries where the author’s name is the same as the blog name, we could issue the query:

\>>> Entry.objects.filter(authors\_\_name\=F("blog\_\_name"))

For date and date/time fields, you can add or subtract a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") object. The following would return all entries that were modified more than 3 days after they were published:

\>>> from datetime import timedelta
\>>> Entry.objects.filter(mod\_date\_\_gt\=F("pub\_date") + timedelta(days\=3))

The `F()` objects support bitwise operations by `.bitand()`, `.bitor()`, `.bitxor()`, `.bitrightshift()`, and `.bitleftshift()`. For example:

\>>> F("somefield").bitand(16)

Oracle

Oracle doesn’t support bitwise XOR operation.

### Expressions can reference transforms[¶](#expressions-can-reference-transforms "Link to this heading")

Django supports using transforms in expressions.

For example, to find all `Entry` objects published in the same year as they were last modified:

\>>> from django.db.models import F
\>>> Entry.objects.filter(pub\_date\_\_year\=F("mod\_date\_\_year"))

To find the earliest year an entry was published, we can issue the query:

\>>> from django.db.models import Min
\>>> Entry.objects.aggregate(first\_published\_year\=Min("pub\_date\_\_year"))

This example finds the value of the highest rated entry and the total number of comments on all entries for each year:

\>>> from django.db.models import OuterRef, Subquery, Sum
\>>> Entry.objects.values("pub\_date\_\_year").annotate(
...     top\_rating\=Subquery(
...         Entry.objects.filter(
...             pub\_date\_\_year\=OuterRef("pub\_date\_\_year"),
...         )
...         .order\_by("-rating")
...         .values("rating")\[:1\]
...     ),
...     total\_comments\=Sum("number\_of\_comments"),
... )

### The `pk` lookup shortcut[¶](#the-pk-lookup-shortcut "Link to this heading")

For convenience, Django provides a `pk` lookup shortcut, which stands for “primary key”.

In the example `Blog` model, the primary key is the `id` field, so these three statements are equivalent:

\>>> Blog.objects.get(id\_\_exact\=14)  \# Explicit form
\>>> Blog.objects.get(id\=14)  \# \_\_exact is implied
\>>> Blog.objects.get(pk\=14)  \# pk implies id\_\_exact

The use of `pk` isn’t limited to `__exact` queries – any query term can be combined with `pk` to perform a query on the primary key of a model:

\# Get blogs entries with id 1, 4 and 7
\>>> Blog.objects.filter(pk\_\_in\=\[1, 4, 7\])

\# Get all blog entries with id > 14
\>>> Blog.objects.filter(pk\_\_gt\=14)

`pk` lookups also work across joins. For example, these three statements are equivalent:

\>>> Entry.objects.filter(blog\_\_id\_\_exact\=3)  \# Explicit form
\>>> Entry.objects.filter(blog\_\_id\=3)  \# \_\_exact is implied
\>>> Entry.objects.filter(blog\_\_pk\=3)  \# \_\_pk implies \_\_id\_\_exact

### Escaping percent signs and underscores in `LIKE` statements[¶](#escaping-percent-signs-and-underscores-in-like-statements "Link to this heading")

The field lookups that equate to `LIKE` SQL statements (`iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith` and `iendswith`) will automatically escape the two special characters used in `LIKE` statements – the percent sign and the underscore. (In a `LIKE` statement, the percent sign signifies a multiple-character wildcard and the underscore signifies a single-character wildcard.)

This means things should work intuitively, so the abstraction doesn’t leak. For example, to retrieve all the entries that contain a percent sign, use the percent sign as any other character:

\>>> Entry.objects.filter(headline\_\_contains\="%")

Django takes care of the quoting for you; the resulting SQL will look something like this:

SELECT ... WHERE headline LIKE '%\\%%';

Same goes for underscores. Both percentage signs and underscores are handled for you transparently.

### Caching and `QuerySet`s[¶](#caching-and-querysets "Link to this heading")

Each [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") contains a cache to minimize database access. Understanding how it works will allow you to write the most efficient code.

In a newly created [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), the cache is empty. The first time a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is evaluated – and, hence, a database query happens – Django saves the query results in the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")’s cache and returns the results that have been explicitly requested (e.g., the next element, if the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is being iterated over). Subsequent evaluations of the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") reuse the cached results.

Keep this caching behavior in mind, because it may bite you if you don’t use your [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")s correctly. For example, the following will create two [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")s, evaluate them, and throw them away:

\>>> print(\[e.headline for e in Entry.objects.all()\])
\>>> print(\[e.pub\_date for e in Entry.objects.all()\])

That means the same database query will be executed twice, effectively doubling your database load. Also, there’s a possibility the two lists may not include the same database records, because an `Entry` may have been added or deleted in the split second between the two requests.

To avoid this problem, save the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and reuse it:

\>>> queryset \= Entry.objects.all()
\>>> print(\[p.headline for p in queryset\])  \# Evaluate the query set.
\>>> print(\[p.pub\_date for p in queryset\])  \# Reuse the cache from the evaluation.

#### When `QuerySet`s are not cached[¶](#when-querysets-are-not-cached "Link to this heading")

Querysets do not always cache their results. When evaluating only _part_ of the queryset, the cache is checked, but if it is not populated then the items returned by the subsequent query are not cached. Specifically, this means that [limiting the queryset](#limiting-querysets) using an array slice or an index will not populate the cache.

For example, repeatedly getting a certain index in a queryset object will query the database each time:

\>>> queryset \= Entry.objects.all()
\>>> print(queryset\[5\])  \# Queries the database
\>>> print(queryset\[5\])  \# Queries the database again

However, if the entire queryset has already been evaluated, the cache will be checked instead:

\>>> queryset \= Entry.objects.all()
\>>> \[entry for entry in queryset\]  \# Queries the database
\>>> print(queryset\[5\])  \# Uses cache
\>>> print(queryset\[5\])  \# Uses cache

Here are some examples of other actions that will result in the entire queryset being evaluated and therefore populate the cache:

\>>> \[entry for entry in queryset\]
\>>> bool(queryset)
\>>> entry in queryset
\>>> list(queryset)

Note

Simply printing the queryset will not populate the cache. This is because the call to `__repr__()` only returns a slice of the entire queryset.

## Asynchronous queries[¶](#asynchronous-queries "Link to this heading")

If you are writing asynchronous views or code, you cannot use the ORM for queries in quite the way we have described above, as you cannot call _blocking_ synchronous code from asynchronous code - it will block up the event loop (or, more likely, Django will notice and raise a `SynchronousOnlyOperation` to stop that from happening).

Fortunately, you can do many queries using Django’s asynchronous query APIs. Every method that might block - such as `get()` or `delete()` - has an asynchronous variant (`aget()` or `adelete()`), and when you iterate over results, you can use asynchronous iteration (`async for`) instead.

### Query iteration[¶](#query-iteration "Link to this heading")

The default way of iterating over a query - with `for` - will result in a blocking database query behind the scenes as Django loads the results at iteration time. To fix this, you can swap to `async for`:

async for entry in Authors.objects.filter(name\_\_startswith\="A"):
    ...

Be aware that you also can’t do other things that might iterate over the queryset, such as wrapping `list()` around it to force its evaluation (you can use `async for` in a comprehension, if you want it).

Because `QuerySet` methods like `filter()` and `exclude()` do not actually run the query - they set up the queryset to run when it’s iterated over - you can use those freely in asynchronous code. For a guide to which methods can keep being used like this, and which have asynchronous versions, read the next section.

### `QuerySet` and manager methods[¶](#queryset-and-manager-methods "Link to this heading")

Some methods on managers and querysets - like `get()` and `first()` - force execution of the queryset and are blocking. Some, like `filter()` and `exclude()`, don’t force execution and so are safe to run from asynchronous code. But how are you supposed to tell the difference?

While you could poke around and see if there is an `a`\-prefixed version of the method (for example, we have `aget()` but not `afilter()`), there is a more logical way - look up what kind of method it is in the [QuerySet reference](../../../ref/models/querysets/).

In there, you’ll find the methods on QuerySets grouped into two sections:

-   _Methods that return new querysets_: These are the non-blocking ones, and don’t have asynchronous versions. You’re free to use these in any situation, though read the notes on `defer()` and `only()` before you use them.
    
-   _Methods that do not return querysets_: These are the blocking ones, and have asynchronous versions - the asynchronous name for each is noted in its documentation, though our standard pattern is to add an `a` prefix.
    

Using this distinction, you can work out when you need to use asynchronous versions, and when you don’t. For example, here’s a valid asynchronous query:

user \= await User.objects.filter(username\=my\_input).afirst()

`filter()` returns a queryset, and so it’s fine to keep chaining it inside an asynchronous environment, whereas `first()` evaluates and returns a model instance - thus, we change to `afirst()`, and use `await` at the front of the whole expression in order to call it in an asynchronous-friendly way.

Note

If you forget to put the `await` part in, you may see errors like _“coroutine object has no attribute x”_ or _“<coroutine …>”_ strings in place of your model instances. If you ever see these, you are missing an `await` somewhere to turn that coroutine into a real value.

### Transactions[¶](#transactions "Link to this heading")

Transactions are **not** currently supported with asynchronous queries and updates. You will find that trying to use one raises `SynchronousOnlyOperation`.

If you wish to use a transaction, we suggest you write your ORM code inside a separate, synchronous function and then call that using `sync_to_async` - see [Asynchronous support](../../async/) for more.

## Querying `JSONField`[¶](#querying-jsonfield "Link to this heading")

Lookups implementation is different in [`JSONField`](../../../ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField"), mainly due to the existence of key transformations. To demonstrate, we will use the following example model:

from django.db import models

class Dog(models.Model):
    name \= models.CharField(max\_length\=200)
    data \= models.JSONField(null\=True)

    def \_\_str\_\_(self):
        return self.name

### Storing and querying for `None`[¶](#storing-and-querying-for-none "Link to this heading")

As with other fields, storing `None` as the field’s value will store it as SQL `NULL`. While not recommended, it is possible to store JSON scalar `null` instead of SQL `NULL` by using [`Value(None, JSONField())`](../../../ref/models/expressions/#django.db.models.Value "django.db.models.Value").

Whichever of the values is stored, when retrieved from the database, the Python representation of the JSON scalar `null` is the same as SQL `NULL`, i.e. `None`. Therefore, it can be hard to distinguish between them.

This only applies to `None` as the top-level value of the field. If `None` is inside a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") or [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), it will always be interpreted as JSON `null`.

When querying, `None` value will always be interpreted as JSON `null`. To query for SQL `NULL`, use [`isnull`](../../../ref/models/querysets/#std-fieldlookup-isnull):

\>>> Dog.objects.create(name\="Max", data\=None)  \# SQL NULL.
<Dog: Max>
\>>> Dog.objects.create(name\="Archie", data\=Value(None, JSONField()))  \# JSON null.
<Dog: Archie>
\>>> Dog.objects.filter(data\=None)
<QuerySet \[<Dog: Archie>\]>
\>>> Dog.objects.filter(data\=Value(None, JSONField()))
<QuerySet \[<Dog: Archie>\]>
\>>> Dog.objects.filter(data\_\_isnull\=True)
<QuerySet \[<Dog: Max>\]>
\>>> Dog.objects.filter(data\_\_isnull\=False)
<QuerySet \[<Dog: Archie>\]>

Unless you are sure you wish to work with SQL `NULL` values, consider setting `null=False` and providing a suitable default for empty values, such as `default=dict`.

Note

Storing JSON scalar `null` does not violate [`null=False`](../../../ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null").

### Key, index, and path transforms[¶](#key-index-and-path-transforms "Link to this heading")

To query based on a given dictionary key, use that key as the lookup name:

\>>> Dog.objects.create(
...     name\="Rufus",
...     data\={
...         "breed": "labrador",
...         "owner": {
...             "name": "Bob",
...             "other\_pets": \[
...                 {
...                     "name": "Fishy",
...                 }
...             \],
...         },
...     },
... )
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"breed": "collie", "owner": None})
<Dog: Meg>
\>>> Dog.objects.filter(data\_\_breed\="collie")
<QuerySet \[<Dog: Meg>\]>

Multiple keys can be chained together to form a path lookup:

\>>> Dog.objects.filter(data\_\_owner\_\_name\="Bob")
<QuerySet \[<Dog: Rufus>\]>

If the key is an integer, it will be interpreted as an index transform in an array:

\>>> Dog.objects.filter(data\_\_owner\_\_other\_pets\_\_0\_\_name\="Fishy")
<QuerySet \[<Dog: Rufus>\]>

If the key is a negative integer, it cannot be used in a filter keyword directly, but you can still use dictionary unpacking to use it in a query:

\>>> Dog.objects.filter(\*\*{"data\_\_owner\_\_other\_pets\_\_-1\_\_name": "Fishy"})
<QuerySet \[<Dog: Rufus>\]>

MySQL, MariaDB, and Oracle

Negative JSON array indices are not supported.

Changed in Django 6.0:

SQLite support for negative JSON array indices was added.

If the key you wish to query by clashes with the name of another lookup, use the [`contains`](#std-fieldlookup-jsonfield.contains) lookup instead.

To query for missing keys, use the `isnull` lookup:

\>>> Dog.objects.create(name\="Shep", data\={"breed": "collie"})
<Dog: Shep>
\>>> Dog.objects.filter(data\_\_owner\_\_isnull\=True)
<QuerySet \[<Dog: Shep>\]>

Note

The lookup examples given above implicitly use the [`exact`](../../../ref/models/querysets/#std-fieldlookup-exact) lookup. Key, index, and path transforms can also be chained with: [`icontains`](../../../ref/models/querysets/#std-fieldlookup-icontains), [`endswith`](../../../ref/models/querysets/#std-fieldlookup-endswith), [`iendswith`](../../../ref/models/querysets/#std-fieldlookup-iendswith), [`iexact`](../../../ref/models/querysets/#std-fieldlookup-iexact), [`regex`](../../../ref/models/querysets/#std-fieldlookup-regex), [`iregex`](../../../ref/models/querysets/#std-fieldlookup-iregex), [`startswith`](../../../ref/models/querysets/#std-fieldlookup-startswith), [`istartswith`](../../../ref/models/querysets/#std-fieldlookup-istartswith), [`lt`](../../../ref/models/querysets/#std-fieldlookup-lt), [`lte`](../../../ref/models/querysets/#std-fieldlookup-lte), [`gt`](../../../ref/models/querysets/#std-fieldlookup-gt), and [`gte`](../../../ref/models/querysets/#std-fieldlookup-gte), as well as with [Containment and key lookups](#containment-and-key-lookups).

#### `KT()` expressions[¶](#module-django.db.models.fields.json "Link to this heading")

_class_ KT(_lookup_)[¶](#django.db.models.fields.json.KT "Link to this definition")

Represents the text value of a key, index, or path transform of [`JSONField`](../../../ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField"). You can use the double underscore notation in `lookup` to chain dictionary key and index transforms.

For example:

\>>> from django.db.models.fields.json import KT
\>>> Dog.objects.create(
...     name\="Shep",
...     data\={
...         "owner": {"name": "Bob"},
...         "breed": \["collie", "lhasa apso"\],
...     },
... )
<Dog: Shep>
\>>> Dog.objects.annotate(
...     first\_breed\=KT("data\_\_breed\_\_1"), owner\_name\=KT("data\_\_owner\_\_name")
... ).filter(first\_breed\_\_startswith\="lhasa", owner\_name\="Bob")
<QuerySet \[<Dog: Shep>\]>

Note

Due to the way in which key-path queries work, [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") and [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") are not guaranteed to produce exhaustive sets. If you want to include objects that do not have the path, add the `isnull` lookup.

Warning

Since any string could be a key in a JSON object, any lookup other than those listed below will be interpreted as a key lookup. No errors are raised. Be extra careful for typing mistakes, and always check your queries work as you intend.

MariaDB and Oracle users

Using [`order_by()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by") on key, index, or path transforms will sort the objects using the string representation of the values. This is because MariaDB and Oracle Database do not provide a function that converts JSON values into their equivalent SQL values.

Oracle users

On Oracle Database, using `None` as the lookup value in an [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") query will return objects that do not have `null` as the value at the given path, including objects that do not have the path. On other database backends, the query will return objects that have the path and the value is not `null`.

PostgreSQL users

On PostgreSQL, if only one key or index is used, the SQL operator `->` is used. If multiple operators are used then the `#>` operator is used.

SQLite users

On SQLite, `"true"`, `"false"`, and `"null"` string values will always be interpreted as `True`, `False`, and JSON `null` respectively.

### Containment and key lookups[¶](#containment-and-key-lookups "Link to this heading")

#### `contains`[¶](#contains "Link to this heading")

The [`contains`](../../../ref/models/querysets/#std-fieldlookup-contains) lookup is overridden on `JSONField`. The returned objects are those where the given `dict` of key-value pairs are all contained in the top-level of the field. For example:

\>>> Dog.objects.create(name\="Rufus", data\={"breed": "labrador", "owner": "Bob"})
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
\>>> Dog.objects.create(name\="Fred", data\={})
<Dog: Fred>
\>>> Dog.objects.create(
...     name\="Merry", data\={"breed": "pekingese", "tricks": \["fetch", "dance"\]}
... )
\>>> Dog.objects.filter(data\_\_contains\={"owner": "Bob"})
<QuerySet \[<Dog: Rufus>, <Dog: Meg>\]>
\>>> Dog.objects.filter(data\_\_contains\={"breed": "collie"})
<QuerySet \[<Dog: Meg>\]>
\>>> Dog.objects.filter(data\_\_contains\={"tricks": \["dance"\]})
<QuerySet \[<Dog: Merry>\]>

Oracle and SQLite

`contains` is not supported on Oracle and SQLite.

#### `contained_by`[¶](#contained-by "Link to this heading")

This is the inverse of the [`contains`](#std-fieldlookup-jsonfield.contains) lookup - the objects returned will be those where the key-value pairs on the object are a subset of those in the value passed. For example:

\>>> Dog.objects.create(name\="Rufus", data\={"breed": "labrador", "owner": "Bob"})
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
\>>> Dog.objects.create(name\="Fred", data\={})
<Dog: Fred>
\>>> Dog.objects.create(
...     name\="Merry", data\={"breed": "pekingese", "tricks": \["fetch", "dance"\]}
... )
\>>> Dog.objects.filter(data\_\_contained\_by\={"breed": "collie", "owner": "Bob"})
<QuerySet \[<Dog: Meg>, <Dog: Fred>\]>
\>>> Dog.objects.filter(data\_\_contained\_by\={"breed": "collie"})
<QuerySet \[<Dog: Fred>\]>
\>>> Dog.objects.filter(
...     data\_\_contained\_by\={"breed": "pekingese", "tricks": \["dance", "fetch", "hug"\]}
... )
<QuerySet \[<Dog: Merry>, <Dog: Fred>\]>

Oracle and SQLite

`contained_by` is not supported on Oracle and SQLite.

#### `has_key`[¶](#has-key "Link to this heading")

Returns objects where the given key is in the top-level of the data. For example:

\>>> Dog.objects.create(name\="Rufus", data\={"breed": "labrador"})
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
\>>> Dog.objects.filter(data\_\_has\_key\="owner")
<QuerySet \[<Dog: Meg>\]>

#### `has_keys`[¶](#has-keys "Link to this heading")

Returns objects where all of the given keys are in the top-level of the data. For example:

\>>> Dog.objects.create(name\="Rufus", data\={"breed": "labrador"})
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
\>>> Dog.objects.filter(data\_\_has\_keys\=\["breed", "owner"\])
<QuerySet \[<Dog: Meg>\]>

#### `has_any_keys`[¶](#has-any-keys "Link to this heading")

Returns objects where any of the given keys are in the top-level of the data. For example:

\>>> Dog.objects.create(name\="Rufus", data\={"breed": "labrador"})
<Dog: Rufus>
\>>> Dog.objects.create(name\="Meg", data\={"owner": "Bob"})
<Dog: Meg>
\>>> Dog.objects.filter(data\_\_has\_any\_keys\=\["owner", "breed"\])
<QuerySet \[<Dog: Rufus>, <Dog: Meg>\]>

## Complex lookups with `Q` objects[¶](#complex-lookups-with-q-objects "Link to this heading")

Keyword argument queries – in [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with `OR` statements), you can use [`Q objects`](../../../ref/models/querysets/#django.db.models.Q "django.db.models.Q").

A [`Q object`](../../../ref/models/querysets/#django.db.models.Q "django.db.models.Q") (`django.db.models.Q`) is an object used to encapsulate a collection of keyword arguments. These keyword arguments are specified as in “Field lookups” above.

For example, this `Q` object encapsulates a single `LIKE` query:

from django.db.models import Q

Q(question\_\_startswith\="What")

`Q` objects can be combined using the `&`, `|`, and `^` operators. When an operator is used on two `Q` objects, it yields a new `Q` object.

For example, this statement yields a single `Q` object that represents the “OR” of two `"question__startswith"` queries:

Q(question\_\_startswith\="Who") | Q(question\_\_startswith\="What")

This is equivalent to the following SQL `WHERE` clause:

WHERE question LIKE 'Who%' OR question LIKE 'What%'

You can compose statements of arbitrary complexity by combining `Q` objects with the `&`, `|`, and `^` operators and use parenthetical grouping. Also, `Q` objects can be negated using the `~` operator, allowing for combined lookups that combine both a normal query and a negated (`NOT`) query:

Q(question\_\_startswith\="Who") | ~Q(pub\_date\_\_year\=2005)

Each lookup function that takes keyword-arguments (e.g. [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude"), [`get()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get")) can also be passed one or more `Q` objects as positional (not-named) arguments. If you provide multiple `Q` object arguments to a lookup function, the arguments will be “AND”ed together. For example:

Poll.objects.get(
    Q(question\_\_startswith\="Who"),
    Q(pub\_date\=date(2005, 5, 2)) | Q(pub\_date\=date(2005, 5, 6)),
)

… roughly translates into the SQL:

SELECT \* from polls WHERE question LIKE 'Who%'
    AND (pub\_date \= '2005-05-02' OR pub\_date \= '2005-05-06')

Lookup functions can mix the use of `Q` objects and keyword arguments. All arguments provided to a lookup function (be they keyword arguments or `Q` objects) are “AND”ed together. However, if a `Q` object is provided, it must precede the definition of any keyword arguments. For example:

Poll.objects.get(
    Q(pub\_date\=date(2005, 5, 2)) | Q(pub\_date\=date(2005, 5, 6)),
    question\_\_startswith\="Who",
)

… would be a valid query, equivalent to the previous example; but:

\# INVALID QUERY
Poll.objects.get(
    question\_\_startswith\="Who",
    Q(pub\_date\=date(2005, 5, 2)) | Q(pub\_date\=date(2005, 5, 6)),
)

… would not be valid.

See also

The [OR lookups examples](https://github.com/django/django/blob/main/tests/or_lookups/tests.py) in Django’s unit tests show some possible uses of `Q`.

## Comparing objects[¶](#comparing-objects "Link to this heading")

To compare two model instances, use the standard Python comparison operator, the double equals sign: `==`. Behind the scenes, that compares the primary key values of two models.

Using the `Entry` example above, the following two statements are equivalent:

\>>> some\_entry \== other\_entry
\>>> some\_entry.id \== other\_entry.id

If a model’s primary key isn’t called `id`, no problem. Comparisons will always use the primary key, whatever it’s called. For example, if a model’s primary key field is called `name`, these two statements are equivalent:

\>>> some\_obj \== other\_obj
\>>> some\_obj.name \== other\_obj.name

## Deleting objects[¶](#deleting-objects "Link to this heading")

The delete method, conveniently, is named [`delete()`](../../../ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete"). This method immediately deletes the object and returns the number of objects deleted and a dictionary with the number of deletions per object type. Example:

\>>> e.delete()
(1, {'blog.Entry': 1})

You can also delete objects in bulk. Every [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") has a [`delete()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method, which deletes all members of that [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet").

For example, this deletes all `Entry` objects with a `pub_date` year of 2005:

\>>> Entry.objects.filter(pub\_date\_\_year\=2005).delete()
(5, {'webapp.Entry': 5})

Keep in mind that this will, whenever possible, be executed purely in SQL, and so the `delete()` methods of individual object instances will not necessarily be called during the process. If you’ve provided a custom `delete()` method on a model class and want to ensure that it is called, you will need to “manually” delete instances of that model (e.g., by iterating over a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and calling `delete()` on each object individually) rather than using the bulk [`delete()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method of a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet").

When Django deletes an object, by default it emulates the behavior of the SQL constraint `ON DELETE CASCADE` – in other words, any objects which had foreign keys pointing at the object to be deleted will be deleted along with it. For example:

b \= Blog.objects.get(pk\=1)
\# This will delete the Blog and all of its Entry objects.
b.delete()

This cascade behavior is customizable via the [`on_delete`](../../../ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") argument to the [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey").

Note that [`delete()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") is the only [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") method that is not exposed on a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") itself. This is a safety mechanism to prevent you from accidentally requesting `Entry.objects.delete()`, and deleting _all_ the entries. If you _do_ want to delete all the objects, then you have to explicitly request a complete query set:

Entry.objects.all().delete()

## Copying model instances[¶](#copying-model-instances "Link to this heading")

Although there is no built-in method for copying model instances, it is possible to easily create new instance with all fields’ values copied. In the simplest case, you can set `pk` to `None` and [`_state.adding`](../../../ref/models/instances/#django.db.models.Model._state "django.db.models.Model._state") to `True`. Using our blog example:

blog \= Blog(name\="My blog", tagline\="Blogging is easy")
blog.save()  \# blog.pk == 1

blog.pk \= None
blog.\_state.adding \= True
blog.save()  \# blog.pk == 2

Things get more complicated if you use inheritance. Consider a subclass of `Blog`:

class ThemeBlog(Blog):
    theme \= models.CharField(max\_length\=200)

django\_blog \= ThemeBlog(name\="Django", tagline\="Django is easy", theme\="python")
django\_blog.save()  \# django\_blog.pk == 3

Due to how inheritance works, you have to set both `pk` and `id` to `None`, and `_state.adding` to `True`:

django\_blog.pk \= None
django\_blog.id \= None
django\_blog.\_state.adding \= True
django\_blog.save()  \# django\_blog.pk == 4

This process doesn’t copy relations that aren’t part of the model’s database table. For example, `Entry` has a `ManyToManyField` to `Author`. After duplicating an entry, you must set the many-to-many relations for the new entry:

entry \= Entry.objects.all()\[0\]  \# some previous entry
old\_authors \= entry.authors.all()
entry.pk \= None
entry.\_state.adding \= True
entry.save()
entry.authors.set(old\_authors)

For a `OneToOneField`, you must duplicate the related object and assign it to the new object’s field to avoid violating the one-to-one unique constraint. For example, assuming `entry` is already duplicated as above:

detail \= EntryDetail.objects.all()\[0\]
detail.pk \= None
detail.\_state.adding \= True
detail.entry \= entry
detail.save()

Note that it is not possible to copy instances of models with deferred fields using this pattern unless values are assigned to them:

\>>> blog \= Blog.objects.defer("name")\[0\]
\>>> blog.pk \= None
\>>> blog.\_state.adding \= True
\>>> blog.save()
Traceback (most recent call last):
    ...
AttributeError: Cannot retrieve deferred field 'name' from an unsaved model.
\>>> blog.name \= "Another Blog"
\>>> blog.save()

## Updating multiple objects at once[¶](#updating-multiple-objects-at-once "Link to this heading")

Sometimes you want to set a field to a particular value for all the objects in a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"). You can do this with the [`update()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update") method. For example:

\# Update all the headlines with pub\_date in 2007.
Entry.objects.filter(pub\_date\_\_year\=2007).update(headline\="Everything is the same")

You can only set non-relation fields and [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") fields using this method. To update a non-relation field, provide the new value as a constant. To update [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") fields, set the new value to be the new model instance you want to point to. For example:

\>>> b \= Blog.objects.get(pk\=1)

\# Change every Entry so that it belongs to this Blog.
\>>> Entry.objects.update(blog\=b)

The `update()` method is applied instantly and returns the number of rows matched by the query (which may not be equal to the number of rows updated if some rows already have the new value). The only restriction on the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") being updated is that it can only access one database table: the model’s main table. You can filter based on related fields, but you can only update columns in the model’s main table. Example:

\>>> b \= Blog.objects.get(pk\=1)

\# Update all the headlines belonging to this Blog.
\>>> Entry.objects.filter(blog\=b).update(headline\="Everything is the same")

Be aware that the `update()` method is converted directly to an SQL statement. It is a bulk operation for direct updates. It doesn’t run any [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") methods on your models, or emit the `pre_save` or `post_save` signals (which are a consequence of calling [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save")), or honor the [`auto_now`](../../../ref/models/fields/#django.db.models.DateField.auto_now "django.db.models.DateField.auto_now") field option. If you want to save every item in a [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and make sure that the [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method is called on each instance, you don’t need any special function to handle that. Loop over them and call [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"):

for item in my\_queryset:
    item.save()

Calls to update can also use [`F expressions`](../../../ref/models/expressions/#django.db.models.F "django.db.models.F") to update one field based on the value of another field in the model. This is especially useful for incrementing counters based upon their current value. For example, to increment the pingback count for every entry in the blog:

\>>> Entry.objects.update(number\_of\_pingbacks\=F("number\_of\_pingbacks") + 1)

However, unlike `F()` objects in filter and exclude clauses, you can’t introduce joins when you use `F()` objects in an update – you can only reference fields local to the model being updated. If you attempt to introduce a join with an `F()` object, a `FieldError` will be raised:

\# This will raise a FieldError
\>>> Entry.objects.update(headline\=F("blog\_\_name"))

## Related objects[¶](#related-objects "Link to this heading")

When you define a relationship in a model (i.e., a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), [`OneToOneField`](../../../ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField"), or [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField")), instances of that model will have a convenient API to access the related object(s).

Using the models at the top of this page, for example, an `Entry` object `e` can get its associated `Blog` object by accessing the `blog` attribute: `e.blog`.

(Behind the scenes, this functionality is implemented by Python [descriptors](https://docs.python.org/3/howto/descriptor.html "(in Python v3.14)"). This shouldn’t really matter to you, but we point it out here for the curious.)

Django also creates API accessors for the “other” side of the relationship – the link from the related model to the model that defines the relationship. For example, a `Blog` object `b` has access to a list of all related `Entry` objects via the `entry_set` attribute: `b.entry_set.all()`.

All examples in this section use the sample `Blog`, `Author` and `Entry` models defined at the top of this page.

### One-to-many relationships[¶](#one-to-many-relationships "Link to this heading")

#### Forward[¶](#forward "Link to this heading")

If a model has a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), instances of that model will have access to the related (foreign) object via an attribute of the model.

Example:

\>>> e \= Entry.objects.get(id\=2)
\>>> e.blog  \# Returns the related Blog object.

You can get and set via a foreign-key attribute. As you may expect, changes to the foreign key aren’t saved to the database until you call [`save()`](../../../ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"). Example:

\>>> e \= Entry.objects.get(id\=2)
\>>> e.blog \= some\_blog
\>>> e.save()

If a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") field has `null=True` set (i.e., it allows `NULL` values), you can assign `None` to remove the relation. Example:

\>>> e \= Entry.objects.get(id\=2)
\>>> e.blog \= None
\>>> e.save()  \# "UPDATE blog\_entry SET blog\_id = NULL ...;"

Forward access to one-to-many relationships is cached the first time the related object is accessed. Subsequent accesses to the foreign key on the same object instance are cached. Example:

\>>> e \= Entry.objects.get(id\=2)
\>>> print(e.blog)  \# Hits the database to retrieve the associated Blog.
\>>> print(e.blog)  \# Doesn't hit the database; uses cached version.

Note that the [`select_related()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.select_related "django.db.models.query.QuerySet.select_related") [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") method recursively prepopulates the cache of all one-to-many relationships ahead of time. Example:

\>>> e \= Entry.objects.select\_related().get(id\=2)
\>>> print(e.blog)  \# Doesn't hit the database; uses cached version.
\>>> print(e.blog)  \# Doesn't hit the database; uses cached version.

#### Following relationships “backward”[¶](#following-relationships-backward "Link to this heading")

If a model has a [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), instances of the foreign-key model will have access to a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") that returns all instances of the first model. By default, this [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") is named `FOO_set`, where `FOO` is the source model name, lowercased. This [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") returns `QuerySet` instances, which can be filtered and manipulated as described in the “Retrieving objects” section above.

Example:

\>>> b \= Blog.objects.get(id\=1)
\>>> b.entry\_set.all()  \# Returns all Entry objects related to Blog.

\# b.entry\_set is a Manager that returns QuerySets.
\>>> b.entry\_set.filter(headline\_\_contains\="Lennon")
\>>> b.entry\_set.count()

You can override the `FOO_set` name by setting the [`related_name`](../../../ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") parameter in the [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") definition. For example, if the `Entry` model was altered to `blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')`, the above example code would look like this:

\>>> b \= Blog.objects.get(id\=1)
\>>> b.entries.all()  \# Returns all Entry objects related to Blog.

\# b.entries is a Manager that returns \`\`QuerySet\`\` instances.
\>>> b.entries.filter(headline\_\_contains\="Lennon")
\>>> b.entries.count()

#### Using a custom reverse manager[¶](#using-a-custom-reverse-manager "Link to this heading")

By default the [`RelatedManager`](../../../ref/models/relations/#django.db.models.fields.related.RelatedManager "django.db.models.fields.related.RelatedManager") used for reverse relations is a subclass of the [default manager](../managers/#manager-names) for that model. If you would like to specify a different manager for a given query you can use the following syntax:

from django.db import models

class Entry(models.Model):
    \# ...
    objects \= models.Manager()  \# Default Manager
    entries \= EntryManager()  \# Custom Manager

b \= Blog.objects.get(id\=1)
b.entry\_set(manager\="entries").all()

If `EntryManager` performed default filtering in its `get_queryset()` method, that filtering would apply to the `all()` call.

Specifying a custom reverse manager also enables you to call its custom methods:

b.entry\_set(manager\="entries").is\_published()

Interaction with prefetching

When calling [`prefetch_related()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related "django.db.models.query.QuerySet.prefetch_related") with a reverse relation, the default manager will be used. If you want to prefetch related objects using a custom reverse manager, use [`Prefetch()`](../../../ref/models/querysets/#django.db.models.Prefetch "django.db.models.Prefetch"). For example:

from django.db.models import Prefetch

prefetch\_manager \= Prefetch("entry\_set", queryset\=Entry.entries.all())
Blog.objects.prefetch\_related(prefetch\_manager)

#### Additional methods to handle related objects[¶](#additional-methods-to-handle-related-objects "Link to this heading")

In addition to the [`QuerySet`](../../../ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods defined in “Retrieving objects” above, the [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") has additional methods used to handle the set of related objects. A synopsis of each is below, and complete details can be found in the [related objects reference](../../../ref/models/relations/).

`add(obj1, obj2, ...)`

Adds the specified model objects to the related object set.

`create(**kwargs)`

Creates a new object, saves it and puts it in the related object set. Returns the newly created object.

`remove(obj1, obj2, ...)`

Removes the specified model objects from the related object set.

`clear()`

Removes all objects from the related object set.

`set(objs)`

Replace the set of related objects.

To assign the members of a related set, use the `set()` method with an iterable of object instances. For example, if `e1` and `e2` are `Entry` instances:

b \= Blog.objects.get(id\=1)
b.entry\_set.set(\[e1, e2\])

If the `clear()` method is available, any preexisting objects will be removed from the `entry_set` before all objects in the iterable (in this case, a list) are added to the set. If the `clear()` method is _not_ available, all objects in the iterable will be added without removing any existing elements.

Each “reverse” operation described in this section has an immediate effect on the database. Every addition, creation and deletion is immediately and automatically saved to the database.

### Many-to-many relationships[¶](#many-to-many-relationships "Link to this heading")

Both ends of a many-to-many relationship get automatic API access to the other end. The API works similar to a “backward” one-to-many relationship, above.

One difference is in the attribute naming: The model that defines the [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") uses the attribute name of that field itself, whereas the “reverse” model uses the lowercased model name of the original model, plus `'_set'` (just like reverse one-to-many relationships).

An example makes this easier to understand:

e \= Entry.objects.get(id\=3)
e.authors.all()  \# Returns all Author objects for this Entry.
e.authors.count()
e.authors.filter(name\_\_contains\="John")

a \= Author.objects.get(id\=5)
a.entry\_set.all()  \# Returns all Entry objects for this Author.

Like [`ForeignKey`](../../../ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") can specify [`related_name`](../../../ref/models/fields/#django.db.models.ManyToManyField.related_name "django.db.models.ManyToManyField.related_name"). In the above example, if the [`ManyToManyField`](../../../ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") in `Entry` had specified `related_name='entries'`, then each `Author` instance would have an `entries` attribute instead of `entry_set`.

Another difference from one-to-many relationships is that in addition to model instances, the `add()`, `set()`, and `remove()` methods on many-to-many relationships accept primary key values. For example, if `e1` and `e2` are `Entry` instances, then these `set()` calls work identically:

a \= Author.objects.get(id\=5)
a.entry\_set.set(\[e1, e2\])
a.entry\_set.set(\[e1.pk, e2.pk\])

#### Filtering on many-to-many relationships[¶](#filtering-on-many-to-many-relationships "Link to this heading")

When calling `filter()` on a many-to-many relationship, be aware that the join between `Entry` and the intermediary model to `Author` is performed only once, resulting in a restrictive, or “sticky”, filter. Consider the following example:

\>>> from datetime import date
\>>> batucada \= Blog.objects.create(name\="Batucada Blog")
\>>> e \= Entry.objects.create(
...     blog\=batucada,
...     headline\="Supporting social movements with drums",
...     pub\_date\=date(2019, 6, 14),
... )

\>>> gloria \= Author.objects.create(name\="Gloria")
\>>> anna \= Author.objects.create(name\="Anna")
\>>> e.authors.add(gloria, anna)

\>>> anna.entry\_set.filter(authors\_\_name\="Gloria")
<QuerySet \[\]>

This filtered query is looking for blog entries that are co-authored by `anna` and `gloria`. You would expect it to return the entry `e`. However, the filter condition, which traverses the many-to-many relationship between `Entry` and `Author`, yields an empty `QuerySet`.

Since the join between `Entry` and the intermediary model to `Author` happens only once, no single object of the joined models - i.e., a relation between one author and one entry - can fulfill the query condition (entries that are co-authored by `anna` and `gloria`). You can circumvent this behavior by chaining two consecutive `filter()` calls, resulting in two separate joins and thus a more permissive filter:

\>>> anna.entry\_set.filter().filter(authors\_\_name\="Gloria")
<QuerySet \[<Entry: Supporting social movements with drums>\]>

exclude() is also sticky

Please note that for this example, [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") behaves similarly to [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") despite being implemented differently. When traversing the many-to-many relationship, it does not exclude the entry `e` despite being co-authored by Gloria:

\>>> anna.entry\_set.exclude(authors\_\_name\="Gloria")
<QuerySet \[<Entry: Supporting social movements with drums>\]>

When chaining a second `exclude()` call, an empty `QuerySet` is returned, as expected:

\>>> anna.entry\_set.exclude().exclude(authors\_\_name\="Gloria")
<QuerySet \[\]>

However, in other cases, [`exclude()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") behaves differently from [`filter()`](../../../ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"). See the [note](#exclude-implementation) in the “Spanning multi-valued relationships” section above.

### One-to-one relationships[¶](#one-to-one-relationships "Link to this heading")

One-to-one relationships are very similar to many-to-one relationships. If you define a [`OneToOneField`](../../../ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") on your model, instances of that model will have access to the related object via an attribute of the model.

For example:

class EntryDetail(models.Model):
    entry \= models.OneToOneField(Entry, on\_delete\=models.CASCADE)
    details \= models.TextField()

ed \= EntryDetail.objects.get(id\=2)
ed.entry  \# Returns the related Entry object.

The difference comes in “reverse” queries. The related model in a one-to-one relationship also has access to a [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") object, but that [`Manager`](../managers/#django.db.models.Manager "django.db.models.Manager") represents a single object, rather than a collection of objects:

e \= Entry.objects.get(id\=2)
e.entrydetail  \# returns the related EntryDetail object

If no object has been assigned to this relationship, Django will raise a `DoesNotExist` exception.

Instances can be assigned to the reverse relationship in the same way as you would assign the forward relationship:

e.entrydetail \= ed

### How are the backward relationships possible?[¶](#how-are-the-backward-relationships-possible "Link to this heading")

Other object-relational mappers require you to define relationships on both sides. The Django developers believe this is a violation of the DRY (Don’t Repeat Yourself) principle, so Django only requires you to define the relationship on one end.

But how is this possible, given that a model class doesn’t know which other model classes are related to it until those other model classes are loaded?

The answer lies in the [`app registry`](../../../ref/applications/#django.apps.apps "django.apps.apps"). When Django starts, it imports each application listed in [`INSTALLED_APPS`](../../../ref/settings/#std-setting-INSTALLED_APPS), and then the `models` module inside each application. Whenever a new model class is created, Django adds backward-relationships to any related models. If the related models haven’t been imported yet, Django keeps tracks of the relationships and adds them when the related models eventually are imported.

For this reason, it’s particularly important that all the models you’re using be defined in applications listed in [`INSTALLED_APPS`](../../../ref/settings/#std-setting-INSTALLED_APPS). Otherwise, backwards relations may not work properly.

### Queries over related objects[¶](#queries-over-related-objects "Link to this heading")

Queries involving related objects follow the same rules as queries involving normal value fields. When specifying the value for a query to match, you may use either an object instance itself, or the primary key value for the object.

For example, if you have a Blog object `b` with `id=5`, the following three queries would be identical:

Entry.objects.filter(blog\=b)  \# Query using object instance
Entry.objects.filter(blog\=b.id)  \# Query using id from instance
Entry.objects.filter(blog\=5)  \# Query using id directly

## Falling back to raw SQL[¶](#falling-back-to-raw-sql "Link to this heading")

If you find yourself needing to write an SQL query that is too complex for Django’s database-mapper to handle, you can fall back on writing SQL by hand. Django has a couple of options for writing raw SQL queries; see [Performing raw SQL queries](../sql/).

Finally, it’s important to note that the Django database layer is merely an interface to your database. You can access your database via other tools, programming languages or database frameworks; there’s nothing Django-specific about your database.

[Back to Top](#top)