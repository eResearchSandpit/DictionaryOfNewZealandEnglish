# -*- coding: utf-8 -*-
#from flask import Blueprint, render_template
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, g)
from flask.ext.login import login_required, current_user
from flask_wtf import Form
import DictionaryOfNewZealandEnglish.utils as utils
import logging
import sys
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from DictionaryOfNewZealandEnglish.database import db
from DictionaryOfNewZealandEnglish.user.forms import HeadwordForm, RegisterForm, TableEditForm
from DictionaryOfNewZealandEnglish.public.forms import LoginForm
from DictionaryOfNewZealandEnglish.user.models import Headword, Citation, Word_class, Data_set
from DictionaryOfNewZealandEnglish.database import engine
import datetime as dt
from operator import itemgetter

blueprint = Blueprint("user", __name__, url_prefix='/users',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("users/members.html")



@blueprint.route("/insert", methods=["GET"]) #, "POST"])
def insert():
    user_form = LoginForm(request.form)
    form = HeadwordForm(request.form)
    return render_template("users/insert.html", form=form, HeadwordForm=HeadwordForm)




@blueprint.route("/insert", methods=["POST"])
def insertdb():
    
    user_form = LoginForm(request.form)
    form = HeadwordForm(request.form)
    if form.validate():
      flash('Inserting data, in theory - still working on this. Validations are turned off.')
    else:
      flash('Inserting data, in theory - still working on this. Validate == FALSE ')



#    date_obj = datetime.datetime.strptime(form.date.data, '%d/%m/%Y').date()

    homonym_number_id = 1
    word_class_id = 1
    sense_number_id = 1
    origin_id= 1
    register_id =1
    domain_id = 1
    region_id = 1
    #headword_citation = [1]
    #headword_flag = [1]
    updated_by = 1
    headword = Headword.create(headword = form.headword.data,
                               definition = form.definition.data,
                               see = form.see.data,
                               pronunciation = form.pronunciation.data,
                               notes = form.notes.data,
                               archived = form.archived.data,
                               data_set_id = form.data_set.data,

                               homonym_number_id=homonym_number_id, 
                               word_class_id=word_class_id, 
                               sense_number_id=sense_number_id, 
                               origin_id=origin_id, 
                               register_id=register_id, 
                               domain_id=domain_id, 
                               region_id=region_id, 
                               #headword_citation=headword_citation, 
                               #headword_flag=headword_flag, 
                               updated_at=dt.datetime.utcnow(),
                               updated_by=updated_by )

    return render_template("users/insert.html", form=form)





@blueprint.route("/search/", methods=["GET"])
@login_required
def search():
    # logged in users arrive here
    form = HeadwordForm(request.form, "search_data")
    return render_template("users/search.html", form=form)


@blueprint.route("/search/db", methods=["POST"])
@login_required
def searchdb():
    form = HeadwordForm(request.form, "display_data")
    # Handle search
    if form.validate_on_submit():
        #author = form.author.data
        #source = form.source.data
        try:
            date = dt.datetime.strptime(form.updated_at.data, '%d/%m/%Y').date()
        except ValueError:
            date = ""

        #citations = Citation.query.filter_by(author="Wallace", source="maximum").all()
        #citations = engine.execute('select * from Citations where author = :1', [author]).first()

        flash('Search form is validated ')# + citations[0].source)

    else:
        flash_errors(form)

    #flash('Searching data - this page should display responses, but doesn\'t yet.')
    return render_template("users/search.html", form=form)


@blueprint.route("/table_list/", methods=["GET"])
@login_required
def table_list():
    table = request.args.get('table')
    data = get_data_for_table_rowname(table, 'all')
    form = TableEditForm(request.form, "edit_table") # for new entries
    return render_template("users/table_list.html", table=table, data=data, form = form)


@blueprint.route("/table_new_entry/", methods=["POST"])
@login_required
def table_new_entry():
    table = request.args.get('table')
    form = TableEditForm(request.form, "edit_table")
    name = form.name.data
    data = create_row_in_table_for_name(table, form)

    return render_template("users/table_update.html", table=table, name = name, data=data, form=form)


@blueprint.route("/table_delete_row/", methods=["GET", "POST"])
@login_required
def table_delete_row():
    table = request.args.get('table')
    name = request.args.get('name')
    data = get_data_for_table_rowname(table, name)

    # case when refreshing view after delete has taken effect
    if data == None:
        data = get_data_for_table_rowname(table, 'all')
        form = TableEditForm(request.form, "edit_table") # for new entries
        return render_template("users/table_list.html", table=table, data=data, form = form)


    # TODO finish this recipe once Headwords can cope
    data = None # TODO get all headwords using this table & name
    if data == None:
        flash("TODO not yet checking database for existing use before deleting")
        # TODO if set is empty, display 'are you sure?' message
        data = delete_row_in_table(table, name)
        form = TableEditForm(request.form, "edit_table") # for new entries
        return render_template("users/table_list.html", table=table, data=data, form = form)
    else:
        flash("Cannot delete %s as it is in use in these records" % name) 
        # TODO render a page with list of (max 30?) headwords that will be affected


@blueprint.route("/table_update/", methods=["GET", "POST"])
@login_required
def table_update():
    table = request.args.get('table')
    name = request.args.get('name')
    form = TableEditForm(request.form, "edit_table")
#    archived = True if 'archived' in form else False

    if request.method == "GET":
      data = get_data_for_table_rowname(table, name)
    if request.method == "POST":
      data = set_data_for_table_rowname(table, name, form)
      if isinstance(data, basestring):
        flash(data)
        data = get_data_for_table_rowname(table, name)
      else:
        name = data.name

    return render_template("users/table_update.html", table=table, name = name, data=data, form=form)


                       #headword, 
                       #definition, 
                       #see, 
                       #pronunciation, 
                       #notes, 
                       #archived, 

                       #data_set_id, 
                       #homonym_number_id, 
                       #word_class_id, 
                       #sense_number_id, 
                       #origin_id, 
                       #register_id, 
                       #domain_id, 
                       #region_id, 
                       #headword_citation, 
                       #headword_flag, 
                       #updated_by

module_name = "DictionaryOfNewZealandEnglish.user.models"

def create_row_in_table_for_name(table, form):

    name=form.name.data
    _class = str_to_class(module_name, table)

    try:
        _class.create(
                      name=form.name.data,
                      notes=form.notes.data, 
                      archived=form.archived.data, 
                      updated_by=current_user.username, 
                      updated_at=dt.datetime.utcnow()
                      )

    except (IntegrityError, InvalidRequestError):
        db.session.rollback()
        return "Database integrety constraint - %s already exists in the database" % name

    flash("%s inserted into database" % name)
    return get_data_for_table_rowname(table, name)

def delete_row_in_table(table, name):

    _class = str_to_class(module_name, table)
    db_row = _class.query.filter_by(name=name).first()

    try:
        _class.delete(db_row)

    except (IntegrityError, InvalidRequestError):
        db.session.rollback()
        return "Database integrety constraint - %s has a problem" % name

    flash("%s deleted from database" % name)
    return get_data_for_table_rowname(table, 'all')


# TODO find way to make this a private method... @private
def get_data_for_table_rowname(table, name):

    _class = str_to_class(module_name, table)

    if name == "all":
        return _class.query.order_by('archived').order_by('name').all()
    else: 
        return _class.query.filter_by(name=name).first()



# TODO find way to make this a private method... @private
def set_data_for_table_rowname(table, name, form):

    _class = str_to_class(module_name, table)
    db_row = _class.query.filter_by(name=name).first()
    new_name = form.name.data

    try:
        _class.update(db_row,
                  name=new_name,
                  notes=form.notes.data,
                  archived=form.archived.data,
                  updated_by=current_user.username, 
                  updated_at=dt.datetime.utcnow()
                  )
    except (IntegrityError, InvalidRequestError):
        db.session.rollback()
        return "Database integrety constraint - %s already exists in the database" % new_name

    return get_data_for_table_rowname(table, new_name)


# TODO move to utils.py
def str_to_class(module_name, class_name):
    class_name = class_name.replace(' ', '_')
    class_ = None
    try:
        module_ = utils.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)
        except AttributeError:
            print 'Class does not exist'
            logging.error('Class does not exist')
    except ImportError:
        print 'Module does not exist', module_name
        logging.error('Module does not exist')
    return class_

