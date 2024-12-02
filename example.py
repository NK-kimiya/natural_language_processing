from tensorflow.keras.preprocessing.sequence import pad_sequences
requences = [[1,2],[3,4,5],[6,7,8,9]]
print(pad_sequences(requences))
