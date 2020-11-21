import numpy as np
from sklearn import preprocessing
#Предоставление меток входных данных
input_labels = ['red','black','red','green','black','yellow','white']
#Создание кодировщика и установление соответствия между метками и числами
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
#Вывод отображения
print("\nLabel mapping:")
for i  , item in enumerate(encoder.classes_):
    print(item,'-->',i)
#Преобразование меток с помощью кодировщика
test_labels = ['green','red','black']
encoded_values = [3,4,0,1,3,2,2,1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nLabels = ",test_labels)
print("Encoded values = ",list(encoded_values))
print("\nDecoded labels = ",list(decoded_list))