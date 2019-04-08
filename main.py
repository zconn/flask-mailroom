import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add', methods=["GET", "POST"])
def add():

    if request.method == "POST":
        donor_name = request.form["donor"]
        donation_amount = int(request.form["donation"])
        donor_object = Donor.get(Donor.name == donor_name)
        donation_save = Donation(value=donation_amount, donor=donor_object)
        donation_save.save()
        return all()
    return render_template('create_donation.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
