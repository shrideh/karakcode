# Model Meta options | Django documentation | Django

-   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

-   Language: **en**
-   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/models/options/)
-   [sv](https://docs.djangoproject.com/sv/6.0/ref/models/options/)
-   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/models/options/)
-   [pl](https://docs.djangoproject.com/pl/6.0/ref/models/options/)
-   [ko](https://docs.djangoproject.com/ko/6.0/ref/models/options/)
-   [ja](https://docs.djangoproject.com/ja/6.0/ref/models/options/)
-   [it](https://docs.djangoproject.com/it/6.0/ref/models/options/)
-   [id](https://docs.djangoproject.com/id/6.0/ref/models/options/)
-   [fr](https://docs.djangoproject.com/fr/6.0/ref/models/options/)
-   [es](https://docs.djangoproject.com/es/6.0/ref/models/options/)
-   [el](https://docs.djangoproject.com/el/6.0/ref/models/options/)

-   Documentation version: **6.0**
-   [dev](https://docs.djangoproject.com/en/dev/ref/models/options/)
-   [6.1](https://docs.djangoproject.com/en/6.1/ref/models/options/)
-   [5.2](https://docs.djangoproject.com/en/5.2/ref/models/options/)
-   [5.1](https://docs.djangoproject.com/en/5.1/ref/models/options/)
-   [5.0](https://docs.djangoproject.com/en/5.0/ref/models/options/)
-   [4.2](https://docs.djangoproject.com/en/4.2/ref/models/options/)
-   [4.1](https://docs.djangoproject.com/en/4.1/ref/models/options/)
-   [4.0](https://docs.djangoproject.com/en/4.0/ref/models/options/)
-   [3.2](https://docs.djangoproject.com/en/3.2/ref/models/options/)
-   [3.1](https://docs.djangoproject.com/en/3.1/ref/models/options/)
-   [3.0](https://docs.djangoproject.com/en/3.0/ref/models/options/)
-   [2.2](https://docs.djangoproject.com/en/2.2/ref/models/options/)
-   [2.1](https://docs.djangoproject.com/en/2.1/ref/models/options/)
-   [2.0](https://docs.djangoproject.com/en/2.0/ref/models/options/)
-   [1.11](https://docs.djangoproject.com/en/1.11/ref/models/options/)
-   [1.10](https://docs.djangoproject.com/en/1.10/ref/models/options/)
-   [1.9](https://docs.djangoproject.com/en/1.9/ref/models/options/)
-   [1.8](https://docs.djangoproject.com/en/1.8/ref/models/options/)

-   [](#top)

# Model `Meta` options[¶](#model-meta-options "Link to this heading")

This document explains all the possible [metadata options](../../../topics/db/models/#meta-options) that you can give your model in its internal `class Meta`.

## Available `Meta` options[¶](#available-meta-options "Link to this heading")

### `abstract`[¶](#abstract "Link to this heading")

Options.abstract[¶](#django.db.models.Options.abstract "Link to this definition")

If `abstract = True`, this model will be an [abstract base class](../../../topics/db/models/#abstract-base-classes).

### `app_label`[¶](#app-label "Link to this heading")

Options.app\_label[¶](#django.db.models.Options.app_label "Link to this definition")

If a model is defined outside of an application in [`INSTALLED_APPS`](../../settings/#std-setting-INSTALLED_APPS), it must declare which app it belongs to:

app\_label \= "myapp"

If you want to represent a model with the format `app_label.object_name` or `app_label.model_name` you can use `model._meta.label` or `model._meta.label_lower` respectively.

### `base_manager_name`[¶](#base-manager-name "Link to this heading")

Options.base\_manager\_name[¶](#django.db.models.Options.base_manager_name "Link to this definition")

The attribute name of the manager, for example, `'objects'`, to use for the model’s [`_base_manager`](../../../topics/db/managers/#django.db.models.Model._base_manager "django.db.models.Model._base_manager").

### `db_table`[¶](#db-table "Link to this heading")

Options.db\_table[¶](#django.db.models.Options.db_table "Link to this definition")

The name of the database table to use for the model:

db\_table \= "music\_album"

#### Table names[¶](#table-names "Link to this heading")

To save you time, Django automatically derives the name of the database table from the name of your model class and the app that contains it. A model’s database table name is constructed by joining the model’s “app label” – the name you used in [`manage.py startapp`](../../django-admin/#django-admin-startapp) – to the model’s class name, with an underscore between them.

For example, if you have an app `bookstore` (as created by `manage.py startapp bookstore`), a model defined as `class Book` will have a database table named `bookstore_book`.

To override the database table name, use the `db_table` parameter in `class Meta`.

If your database table name is an SQL reserved word, or contains characters that aren’t allowed in Python variable names – notably, the hyphen – that’s OK. Django quotes column and table names behind the scenes.

Use lowercase table names for MariaDB and MySQL

It is strongly advised that you use lowercase table names when you override the table name via `db_table`, particularly if you are using the MySQL backend. See the [MySQL notes](../../databases/#mysql-notes) for more details.

Table name quoting for Oracle

In order to meet the 30-char limitation Oracle has on table names, and match the usual conventions for Oracle databases, Django may shorten table names and turn them all-uppercase. To prevent such transformations, use a quoted name as the value for `db_table`:

db\_table \= '"name\_left\_in\_lowercase"'

Such quoted names can also be used with Django’s other supported database backends; except for Oracle, however, the quotes have no effect. See the [Oracle notes](../../databases/#oracle-notes) for more details.

### `db_table_comment`[¶](#db-table-comment "Link to this heading")

Options.db\_table\_comment[¶](#django.db.models.Options.db_table_comment "Link to this definition")

The comment on the database table to use for this model. It is useful for documenting database tables for individuals with direct database access who may not be looking at your Django code. For example:

class Answer(models.Model):
    question \= models.ForeignKey(Question, on\_delete\=models.CASCADE)
    answer \= models.TextField()

    class Meta:
        db\_table\_comment \= "Question answers"

### `db_tablespace`[¶](#db-tablespace "Link to this heading")

Options.db\_tablespace[¶](#django.db.models.Options.db_tablespace "Link to this definition")

The name of the [database tablespace](../../../topics/db/tablespaces/) to use for this model. The default is the project’s [`DEFAULT_TABLESPACE`](../../settings/#std-setting-DEFAULT_TABLESPACE) setting, if set. If the backend doesn’t support tablespaces, this option is ignored.

### `default_manager_name`[¶](#default-manager-name "Link to this heading")

Options.default\_manager\_name[¶](#django.db.models.Options.default_manager_name "Link to this definition")

The name of the manager to use for the model’s [`_default_manager`](../../../topics/db/managers/#django.db.models.Model._default_manager "django.db.models.Model._default_manager").

### `default_related_name`[¶](#default-related-name "Link to this heading")

Options.default\_related\_name[¶](#django.db.models.Options.default_related_name "Link to this definition")

The name that will be used by default for the relation from a related object back to this one. The default is `<model_name>_set`.

This option also sets [`related_query_name`](../fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name").

As the reverse name for a field should be unique, be careful if you intend to subclass your model. To work around name collisions, part of the name should contain `'%(app_label)s'` and `'%(model_name)s'`, which are replaced respectively by the name of the application the model is in, and the name of the model, both lowercased. See the paragraph on [related names for abstract models](../../../topics/db/models/#abstract-related-name).

### `get_latest_by`[¶](#get-latest-by "Link to this heading")

Options.get\_latest\_by[¶](#django.db.models.Options.get_latest_by "Link to this definition")

The name of a field or a list of field names in the model, typically [`DateField`](../fields/#django.db.models.DateField "django.db.models.DateField"), [`DateTimeField`](../fields/#django.db.models.DateTimeField "django.db.models.DateTimeField"), or [`IntegerField`](../fields/#django.db.models.IntegerField "django.db.models.IntegerField"). This specifies the default field(s) to use in your model [`Manager`](../../../topics/db/managers/#django.db.models.Manager "django.db.models.Manager")’s [`latest()`](../querysets/#django.db.models.query.QuerySet.latest "django.db.models.query.QuerySet.latest") and [`earliest()`](../querysets/#django.db.models.query.QuerySet.earliest "django.db.models.query.QuerySet.earliest") methods.

Example:

\# Latest by ascending order\_date.
get\_latest\_by \= "order\_date"

\# Latest by priority descending, order\_date ascending.
get\_latest\_by \= \["-priority", "order\_date"\]

See the [`latest()`](../querysets/#django.db.models.query.QuerySet.latest "django.db.models.query.QuerySet.latest") docs for more.

### `managed`[¶](#managed "Link to this heading")

Options.managed[¶](#django.db.models.Options.managed "Link to this definition")

Defaults to `True`, meaning Django will create the appropriate database tables in [`migrate`](../../django-admin/#django-admin-migrate) or as part of migrations and remove them as part of a [`flush`](../../django-admin/#django-admin-flush) management command. That is, Django _manages_ the database tables’ lifecycles.

If `False`, no database table creation, modification, or deletion operations will be performed for this model. This is useful if the model represents an existing table or a database view that has been created by some other means. This is the _only_ difference when `managed=False`. All other aspects of model handling are exactly the same as normal. This includes

1.  Adding an automatic primary key field to the model if you don’t declare it. To avoid confusion for later code readers, it’s recommended to specify all the columns from the database table you are modeling when using unmanaged models.
    
2.  If a model with `managed=False` contains a [`ManyToManyField`](../fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") that points to another unmanaged model, then the intermediate table for the many-to-many join will also not be created. However, the intermediary table between one managed and one unmanaged model _will_ be created.
    
    If you need to change this default behavior, create the intermediary table as an explicit model (with `managed` set as needed) and use the [`ManyToManyField.through`](../fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") attribute to make the relation use your custom model.
    

For tests involving models with `managed=False`, it’s up to you to ensure the correct tables are created as part of the test setup.

If you’re interested in changing the Python-level behavior of a model class, you _could_ use `managed=False` and create a copy of an existing model. However, there’s a better approach for that situation: [Proxy models](../../../topics/db/models/#proxy-models).

### `order_with_respect_to`[¶](#order-with-respect-to "Link to this heading")

Options.order\_with\_respect\_to[¶](#django.db.models.Options.order_with_respect_to "Link to this definition")

Makes this object orderable with respect to the given field, usually a `ForeignKey`. This can be used to make related objects orderable with respect to a parent object. For example, if an `Answer` relates to a `Question` object, and a question has more than one answer, and the order of answers matters, you’d do this:

from django.db import models

class Question(models.Model):
    text \= models.TextField()
    \# ...

class Answer(models.Model):
    question \= models.ForeignKey(Question, on\_delete\=models.CASCADE)
    \# ...

    class Meta:
        order\_with\_respect\_to \= "question"

When `order_with_respect_to` is set, two additional methods are provided to retrieve and to set the order of the related objects: `get_RELATED_order()` and `set_RELATED_order()`, where `RELATED` is the lowercased model name. For example, assuming that a `Question` object has multiple related `Answer` objects, the list returned contains the primary keys of the related `Answer` objects:

\>>> question \= Question.objects.get(id\=1)
\>>> question.get\_answer\_order()
\[1, 2, 3\]

The order of a `Question` object’s related `Answer` objects can be set by passing in a list of `Answer` primary keys:

\>>> question.set\_answer\_order(\[3, 1, 2\])

The related objects also get two methods, `get_next_in_order()` and `get_previous_in_order()`, which can be used to access those objects in their proper order. Assuming the `Answer` objects are ordered by `id`:

\>>> answer \= Answer.objects.get(id\=2)
\>>> answer.get\_next\_in\_order()
<Answer: 3>
\>>> answer.get\_previous\_in\_order()
<Answer: 1>

`order_with_respect_to` implicitly sets the `ordering` option

Internally, `order_with_respect_to` adds an additional field/database column named `_order` and sets the model’s [`ordering`](#django.db.models.Options.ordering "django.db.models.Options.ordering") option to this field. Consequently, `order_with_respect_to` and `ordering` cannot be used together, and the ordering added by `order_with_respect_to` will apply whenever you obtain a list of objects of this model.

Changing `order_with_respect_to`

Because `order_with_respect_to` adds a new database column, be sure to make and apply the appropriate migrations if you add or change `order_with_respect_to` after your initial [`migrate`](../../django-admin/#django-admin-migrate).

### `ordering`[¶](#ordering "Link to this heading")

Options.ordering[¶](#django.db.models.Options.ordering "Link to this definition")

The default ordering for the object, for use when obtaining lists of objects:

ordering \= \["-order\_date"\]

This is a tuple or list of strings and/or query expressions. Each string is a field name with an optional “-” prefix, which indicates descending order. Fields without a leading “-” will be ordered ascending. Use the string “?” to order randomly.

For example, to order by a `pub_date` field ascending, use this:

ordering \= \["pub\_date"\]

To order by `pub_date` descending, use this:

ordering \= \["-pub\_date"\]

To order by `pub_date` descending, then by `author` ascending, use this:

ordering \= \["-pub\_date", "author"\]

You can also use [query expressions](../expressions/). To order by `author` ascending and make null values sort last, use this:

from django.db.models import F

ordering \= \[F("author").asc(nulls\_last\=True)\]

Default ordering and GROUP BY

In [GROUP BY queries](../../../topics/db/aggregation/#aggregation-ordering-interaction) (for example, those using [`values()`](../querysets/#django.db.models.query.QuerySet.values "django.db.models.query.QuerySet.values") and [`annotate()`](../querysets/#django.db.models.query.QuerySet.annotate "django.db.models.query.QuerySet.annotate")), the default ordering is not applied.

Warning

Ordering is not a free operation. Each field you add to the ordering incurs a cost to your database. Each foreign key you add will implicitly include all of its default orderings as well.

If a query doesn’t have an ordering specified, results are returned from the database in an unspecified order. A particular ordering is guaranteed only when ordering by a set of fields that uniquely identify each object in the results. For example, if a `name` field isn’t unique, ordering by it won’t guarantee objects with the same name always appear in the same order.

### `permissions`[¶](#permissions "Link to this heading")

Options.permissions[¶](#django.db.models.Options.permissions "Link to this definition")

Extra permissions to enter into the permissions table when creating this object. Add, change, delete, and view permissions are automatically created for each model. This example specifies an extra permission, `can_deliver_pizzas`:

permissions \= \[("can\_deliver\_pizzas", "Can deliver pizzas")\]

This is a list or tuple of 2-tuples in the format `(permission_code, human_readable_permission_name)`.

### `default_permissions`[¶](#default-permissions "Link to this heading")

Options.default\_permissions[¶](#django.db.models.Options.default_permissions "Link to this definition")

Defaults to `('add', 'change', 'delete', 'view')`. You may customize this list, for example, by setting this to an empty list if your app doesn’t require any of the default permissions. It must be specified on the model before the model is created by [`migrate`](../../django-admin/#django-admin-migrate) in order to prevent any omitted permissions from being created.

### `proxy`[¶](#proxy "Link to this heading")

Options.proxy[¶](#django.db.models.Options.proxy "Link to this definition")

If `proxy = True`, a model which subclasses another model will be treated as a [proxy model](../../../topics/db/models/#proxy-models).

### `required_db_features`[¶](#required-db-features "Link to this heading")

Options.required\_db\_features[¶](#django.db.models.Options.required_db_features "Link to this definition")

List of database features that the current connection should have so that the model is considered during the migration phase. For example, if you set this list to `['gis_enabled']`, the model will only be synchronized on GIS-enabled databases. It’s also useful to skip some models when testing with several database backends. Avoid relations between models that may or may not be created as the ORM doesn’t handle this.

### `required_db_vendor`[¶](#required-db-vendor "Link to this heading")

Options.required\_db\_vendor[¶](#django.db.models.Options.required_db_vendor "Link to this definition")

Name of a supported database vendor that this model is specific to. Current built-in vendor names are: `sqlite`, `postgresql`, `mysql`, `oracle`. If this attribute is not empty and the current connection vendor doesn’t match it, the model will not be synchronized.

### `select_on_save`[¶](#select-on-save "Link to this heading")

Options.select\_on\_save[¶](#django.db.models.Options.select_on_save "Link to this definition")

Determines if Django will use the pre-1.6 [`django.db.models.Model.save()`](../instances/#django.db.models.Model.save "django.db.models.Model.save") algorithm. The old algorithm uses `SELECT` to determine if there is an existing row to be updated. The new algorithm tries an `UPDATE` directly. In some rare cases the `UPDATE` of an existing row isn’t visible to Django. An example is the PostgreSQL `ON UPDATE` trigger which returns `NULL`. In such cases the new algorithm will end up doing an `INSERT` even when a row exists in the database.

Usually there is no need to set this attribute. The default is `False`.

See [`django.db.models.Model.save()`](../instances/#django.db.models.Model.save "django.db.models.Model.save") for more about the old and new saving algorithm.

### `indexes`[¶](#indexes "Link to this heading")

Options.indexes[¶](#django.db.models.Options.indexes "Link to this definition")

A list of [indexes](../indexes/) that you want to define on the model:

from django.db import models

class Customer(models.Model):
    first\_name \= models.CharField(max\_length\=100)
    last\_name \= models.CharField(max\_length\=100)

    class Meta:
        indexes \= \[
            models.Index(fields\=\["last\_name", "first\_name"\]),
            models.Index(fields\=\["first\_name"\], name\="first\_name\_idx"),
        \]

### `unique_together`[¶](#unique-together "Link to this heading")

Options.unique\_together[¶](#django.db.models.Options.unique_together "Link to this definition")

Use [`UniqueConstraint`](../constraints/#django.db.models.UniqueConstraint "django.db.models.UniqueConstraint") with the [`constraints`](#django.db.models.Options.constraints "django.db.models.Options.constraints") option instead.

[`UniqueConstraint`](../constraints/#django.db.models.UniqueConstraint "django.db.models.UniqueConstraint") provides more functionality than `unique_together`. `unique_together` may be deprecated in the future.

Sets of field names that, taken together, must be unique:

unique\_together \= \[\["driver", "restaurant"\]\]

This is a list of lists that must be unique when considered together. It’s used in the Django admin and is enforced at the database level (i.e., the appropriate `UNIQUE` statements are included in the `CREATE TABLE` statement).

For convenience, `unique_together` can be a single list when dealing with a single set of fields:

unique\_together \= \["driver", "restaurant"\]

A [`ManyToManyField`](../fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") cannot be included in `unique_together`. (It’s not clear what that would even mean!) If you need to validate uniqueness related to a [`ManyToManyField`](../fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), try using a signal or an explicit [`through`](../fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") model.

The `ValidationError` raised during model validation when the constraint is violated has the `unique_together` error code.

### `constraints`[¶](#constraints "Link to this heading")

Options.constraints[¶](#django.db.models.Options.constraints "Link to this definition")

A list of [constraints](../constraints/) that you want to define on the model:

from django.db import models

class Customer(models.Model):
    age \= models.IntegerField()

    class Meta:
        constraints \= \[
            models.CheckConstraint(condition\=models.Q(age\_\_gte\=18), name\="age\_gte\_18"),
        \]

### `verbose_name`[¶](#verbose-name "Link to this heading")

Options.verbose\_name[¶](#django.db.models.Options.verbose_name "Link to this definition")

A human-readable name for the object, singular:

verbose\_name \= "pizza"

If this isn’t given, Django will use a munged version of the class name: `CamelCase` becomes `camel case`.

### `verbose_name_plural`[¶](#verbose-name-plural "Link to this heading")

Options.verbose\_name\_plural[¶](#django.db.models.Options.verbose_name_plural "Link to this definition")

The plural name for the object:

verbose\_name\_plural \= "stories"

If this isn’t given, Django will use [`verbose_name`](#django.db.models.Options.verbose_name "django.db.models.Options.verbose_name") + `"s"`.

## Read-only `Meta` attributes[¶](#read-only-meta-attributes "Link to this heading")

### `label`[¶](#label "Link to this heading")

Options.label[¶](#django.db.models.Options.label "Link to this definition")

Representation of the object, returns `app_label.object_name`, e.g. `'polls.Question'`.

### `label_lower`[¶](#label-lower "Link to this heading")

Options.label\_lower[¶](#django.db.models.Options.label_lower "Link to this definition")

Representation of the model, returns `app_label.model_name`, e.g. `'polls.question'`.

[Back to Top](#top)