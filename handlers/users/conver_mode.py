from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
import asyncio


from Ai_package.Contextual_AI.Contextual_DB import sql_remember

# Neural imports bellow
import random


import torch

from Ai_package.Contextual_AI.model import NeuralNet
from Ai_package.Contextual_AI.nltk_puk import bag_of_words, tokenize
from Ai_package.Contextual_AI.ctw import tag_list
from Ai_package.Contextual_AI.Contextual_DB import get_words


# Neural VARIABLES
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


FILE = "data.pth"
data = torch.load(FILE)



input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()





""" Это Хендлер для обычного беседного режима """

@dp.message_handler(state=None)
async def bot_conver(message: types.Message):
    
    sentence = message.text

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.90:
        for unit in tag_list:
            if tag == unit:
                collected_words = get_words('{}'.format(tag))
                unpacked_words = []
                for word in collected_words:
                    unpacked_words.append(word[0])
                await message.answer(f"{random.choice(unpacked_words)}")
    else:
        not_responded = ['Не_распознано',message.text,'ВПИШИ ОТВЕТ', message.from_user.id]
        if (message.text).startswith('/'):
            pass
        else:
            try:
                sql_remember(not_responded)
            except:
                print('Возникла ошибка при запоминании.')

        await message.answer("А? О чем ты?")


    
