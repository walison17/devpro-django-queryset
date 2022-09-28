from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'actor'

    def __str__(self):
        return self.first_name


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    district = models.TextField()
    city = models.ForeignKey('City', models.DO_NOTHING)
    postal_code = models.TextField(blank=True, null=True)
    phone = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.TextField()
    country = models.ForeignKey('Country', models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)
    outro_campo = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.TextField()
    last_update = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    active = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING, related_name='+')
    original_language = models.ForeignKey('Language', models.DO_NOTHING, blank=True, null=True, related_name='+')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=5)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=10, decimal_places=5)
    rating = models.TextField(blank=True, null=True)
    special_features = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    actors = models.ManyToManyField('Actor', through='FilmActor')
    categories = models.ManyToManyField('Category', through='FilmCategory', related_name='films')

    class Meta:
        managed = False
        db_table = 'film'

    def __str__(self):
        return self.title


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, models.DO_NOTHING, primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'film_actor'


class FilmCategory(models.Model):
    film = models.ForeignKey(Film, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'film_category'


class FilmText(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    rental = models.ForeignKey('Rental', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    payment_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.ForeignKey(Address, models.DO_NOTHING)
    picture = models.BinaryField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    active = models.SmallIntegerField()
    username = models.TextField()
    password = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(Staff, models.DO_NOTHING, related_name='managed_stores')
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'store'
