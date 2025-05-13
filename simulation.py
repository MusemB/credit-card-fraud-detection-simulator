
import data_stream as ds
import cleaning_zone as cz
import classifier_zone as clz
import time


while True:
    ds.fetch()
    cz.clean()
    clz.classify()


    time.sleep(0.2)

