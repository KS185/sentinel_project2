import numpy as np


with open('../data/ndvi_km_res19.npy', 'rb') as pic2019:
    pic2019 = np.load(pic2019)
    unique_elements19, count_elements19 = np.unique(pic2019,
                                          return_counts=True)

print(unique_elements19, count_elements19)

with open('../data/ndvi_km_res20.npy', 'rb') as pic2020:
    pic2020 = np.load(pic2020)
    unique_elements20, count_elements20 = np.unique(pic2020,
                                          return_counts=True)

print(unique_elements20, count_elements20)

area_percents2019 = np.round(count_elements19/count_elements19.sum()*100, 1)
area_percents2020 = np.round(count_elements20/count_elements20.sum()*100, 1)

with open('../data/results_200825a.npy', 'wb') as ap:
    np.save(ap, np.array(area_percents2019))
    np.save(ap, np.array(area_percents2020))

with open('../data/results_200825a.npy', 'rb') as result:
    result1 = np.load(result)
    result2 = np.load(result)
    print(result1)
    print(result2)