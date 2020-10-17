Poultry Farm Management System: TelelBirds
==========================================

**The Chicken came before the Egg**

A web-based application and platform for keeping track of the entire production system of a Poultry farm,from breeding, egg production, hatchery to chicks management. Written in Python using the Django framework.

<b>Main Site:</b> https://www.telelbirds.com

<b>Features:</b>

* <b>Simple, easy to use.</b>  Entering glucose data should be faster than finding a pen and paper and writing down the number.  Fields have pre-set values where it makes sense (such as the date, time, and category based on time of day).
* <b>Send notifications via email/sms.</b>  Email it to your doctor before your visit, no more carrying log books (and you're saving trees)!  Can be sent as a CSV or PDF attachment.
* <b>Reporting.</b>  Simple reports to see how you're doing.  Highlight how many times you have lows and highs. Show averages by day and category using nice-looking charts and graphs.
* <b>Data filtering.</b>  Advanced filtering: filter by glucose range, date range, category, tag, and notes.
* <b>Tagging.</b>  An optional tag field to help further organize and make sense of your data. For example, it might be useful to add tags to a record such as: exercise, sick, insulin, fasting, etc.
* <b>Expenditure estimation.</b>  Estimate expenditures based on data from the last 3 months.
* <b>Import data from CSV.</b> Import existing data from other software/systems.
* <b>Mobile friendly.</b>  Layout adapts to screen size.


<b>Systems:</b>

* <b>Hatchery.</b> Track incubators capacity and availability for Setting and Incubation Services.
* <b>Chicks.</b> Track a clutch of chicks or multiple batches on the farm.
* <b>Breeders.</b> Track and monitor several breeders of poultry and other birds. 
* <b>Medication Schedules.</b>
* <b>Tagging.</b>
* <b>Finance.</b>
* <b>Deliveries.</b>
* <b>Mobile friendly.</b>

<b>Some point in the future: 2021:</b>

* A simple TelelBird Android app that works offline and auto-syncs with the remote database via REST calls.


Installation/Running the App
----------------------------

1. Install the required libraries listed in the requirements file with pip: pip install -r requirements.txt
2. If you just want to run a demo of the app, use the <b>local_demo.py</b> file which uses an SQLite database and will be created automatically. Otherwise, for development, please use PostgreSQL and the local_settings.py file.  Set the database settings and environment variables accordingly.
3. Run the syncdb command: e.g. python manage.py syncdb --noinput --settings=settings.local_demo
4. Run the South migration: e.g. python manage.py migrate --settings=settings.local_demo
5. (Optional) Populate your database with dummy data: e.g. python manage.py load_random_glucose_data jsmith --settings=settings.local_demo (note that 'telelbirds' can be changed to any username you like, the password will always be 'demo').
6. Run the local web server: e.g. python manage.py runserver --settings=settings.local_demo

3rd-Party Apps/Libraries/Plugins
--------------------------------

TelelBirds uses the following:

* Twitter Bootstrap 3 (http://getbootstrap.com)
* South (http://south.aeracode.org)
* Django Crispy Forms (http://django-crispy-forms.readthedocs.org/en/latest)
* Django Braces (http://django-braces.readthedocs.org/en/v1.2.2/)
* Django Compressor (http://django-compressor.readthedocs.org/en/latest/)
* Bootstrap DateTimePicker (http://eonasdan.github.io/bootstrap-datetimepicker/)
* Datatables (http://datatables.net)
* Highcharts (http://www.highcharts.com/)
