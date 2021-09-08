import fasttext

PRETRAINED_MODEL_PATH = '/tmp/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

sentences = ['I am developer']
predictions = model.predict(sentences)
print(predictions[0][0][0][-2:].upper())