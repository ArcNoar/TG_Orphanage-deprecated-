# Импорт данных
from .ctw import xy, all_words, tag_list
from .nltk_puk import bag_of_words
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from .model import NeuralNet


X_train = []
y_train = []


# Анпакинг XY
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tag_list.index(tag)
    y_train.append(label)  # CrossEntropyLoss

X_train = np.array(X_train)
y_train = np.array(y_train)


class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


# HyperParam
batch_size = 8
hidden_size = 8
output_size = len(tag_list)
input_size = len(X_train[0])  # Длина ALL_WORDS
learning_rate = 0.001
num_epoches = 1000


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True,num_workers = 0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and Optim

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


for epoche in range(num_epoches):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        # Forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        #backward / optimiser
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoche + 1) % 100 == 0:
        print(f'epoch {epoche + 1}/{num_epoches}, loss = {loss.item():.4f}')

print(f'Final Loss, loss = {loss.item():.4f}')


data = {
    "model_state":model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size":hidden_size,
    "all_words": all_words,
    "tags": tag_list
    }

FILE = "data.pth"
torch.save(data,FILE)

print(f'Тренировка усе, все сохранено в {FILE}')
