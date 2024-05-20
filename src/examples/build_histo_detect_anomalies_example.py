import sys
sys.path.append("..")
from histo_building.utils import *
import data_preprocessing.utils as data_utils
import anomaly_detection.detector as anomaly_detector
import anomaly_detection.utils as detect_utils
import concrete_aux.fhe_utils as fhe_utils

dft = data_utils.read_data_from_csv()
data_utils.rescale_data(dft)

day1 = input("Provide a day for building the reference histogram (mm/dd/yyyy or m/d/yyyy): ")
day2 = input("Provide a day for detecting anomalies (mm/dd/yyyy or m/d/yyyy): ")

d1 = data_utils.get_data_by_day(dft, day1)
d2 = data_utils.get_data_by_day(dft, day2)

detect_config = detect_utils.get_configuration()
(low_detect, high_detect) = build_buckets(detect_config['reference_histogram']['bin_size'], detect_config['reference_histogram']['min'], detect_config['reference_histogram']['max'])

nd = int(input("Number of training days for detecting anomalies: "))
training_days_anomaly_detection = []
for _ in range(nd):
    training_days_anomaly_detection.append(input("Provide a day for training the anomaly detection circuit (mm/dd/yyyy or m/d/yyyy): "))

training_data_anomaly_detection = []
for day in training_days_anomaly_detection:
    training_data_anomaly_detection.append(data_utils.get_data_by_day(dft, day))

nb = int(input("Number of training days for building the reference histogram: "))
training_days_histogram_building = []
for _ in range(nb):
    training_days_histogram_building.append(input("Provide a day for training the histogram building circuit (mm/dd/yyyy or m/d/yyyy): "))

training_data_histogram_building = []
for day in training_days_histogram_building:
    training_data_histogram_building.append(data_utils.get_data_by_day(dft, day))

build_and_detect_inputset = anomaly_detector.create_inputset_builder_and_detector(training_data_anomaly_detection, training_data_histogram_building)
builder_and_detector_circuit = fhe_utils.compile_circuit(anomaly_detector.crypto_build_histo_abnormal_labels, {"x": "encrypted", "y": "encrypted", "l": "encrypted", "h": "encrypted", "th": "encrypted"}, build_and_detect_inputset)

build_and_detect_sample = (d2, d1, low_detect, high_detect, detect_config['threshold'])

test = fhe_utils.check_results(builder_and_detector_circuit, anomaly_detector.build_histo_abnormal_labels, build_and_detect_sample)

if test:
    clear_labels = anomaly_detector.build_histo_abnormal_labels(d2, d1, low_detect, high_detect, detect_config['threshold'])
    data_utils.plot_data_and_anomalies(d2, d1, clear_labels)
    data_utils.plot_histograms(d2, d1, len(low_detect), detect_config['reference_histogram']['min'], detect_config['reference_histogram']['max'])