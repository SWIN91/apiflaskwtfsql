from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from app.forms import SignUpForm


@app.route('/index-particles.html')
@app.route('/')
def home():
    return render_template('index-particles.html')

@app.route('/index-static.html')
@app.route('/about')
def about():
    return render_template('index-static.html')

@app.route('/index-slides.html')
def sigin():
    return render_template('index-slides.html')

@app.route('/index.html')
@app.route('/view')
def view():
    return render_template('index.html')

@app.route('/portfolio.html')
def me():
    return render_template('portfolio.html')

@app.route('/signup.html', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Success!', category='alert alert-success d-flex align-items-center')
        else:
            flash('Your form did not validate. Please try again.', category='alert alert-danger d-flex align-items-center')
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)
