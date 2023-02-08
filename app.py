from flask import Flask, render_template, request
from dataclasses import dataclass
from typing import List

@dataclass
class script_data:
    date_of_service: str
    service_title: str
    speaker_name: str
    liturgist_name: str
    coordinator_name: str
    zoom_host_name: str
    metta_singer: str
    slide_manager_name: str
    readers_names: List[str]
    singers_names: List[str]
    circle_round_singer: str
    prelude_hymn_number: str
    prelude_hymn_name: str
    first_hymn_number: str
    first_hymn_name: str
    second_hymn_number: str
    second_hymn_name: str
    final_hymn_number: str
    final_hymn_name: str
    principle_or_source_number: str
    principle_or_source: str
    principle_or_source_text: str
    opening_words: str
    meditation_reading: str
    shared_plate_partner: str
    shared_plate_partner_text: str

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        script_variables = script_data(
            date_of_service = request.form['date_of_service'],
            service_title = request.form['service_title'],
            speaker_name = request.form['speaker_name'],
            liturgist_name = request.form['liturgist_name'],
            coordinator_name = request.form['coordinator_name'],
            zoom_host_name = request.form['zoom_host_name'],
            metta_singer = request.form['metta_singer'],
            slide_manager_name = request.form['slide_manager_name'],
            readers_names = request.form['readers_names'],
            singers_names = request.form['singers_names'],
            circle_round_singer = request.form['circle_round_singer'],
            prelude_hymn_number = request.form['prelude_hymn_number'],
            prelude_hymn_name = request.form['prelude_hymn_name'],
            first_hymn_number = request.form['first_hymn_number'],
            first_hymn_name = request.form['first_hymn_name'],
            second_hymn_number = request.form['second_hymn_number'],
            second_hymn_name = request.form['second_hymn_name'],
            final_hymn_number = request.form['final_hymn_number'],
            final_hymn_name = request.form['final_hymn_name'],
            principle_or_source_number = request.form['principle_or_source_number'],
            principle_or_source = request.form['principle_or_source'],
            principle_or_source_text = request.form['principle_or_source_text'],
            opening_words = request.form['opening_words'],
            meditation_reading = request.form['meditation_reading'],
            shared_plate_partner = request.form['shared_plate_partner'],
            shared_plate_partner_text = request.form['shared_plate_partner_text']
        )
        return render_template('script.html', script_variables=script_variables)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
