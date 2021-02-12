import csv
def save(url, mobile_num, price_set):
    with open('track.csv', mode='w') as tracker:
        tracker_writer = csv.writer(tracker, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tracker_writer.writerow(['Product', 'Number', 'TargetPrice'])
        tracker_writer.writerow([url, mobile_num, price_set])
