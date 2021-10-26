from .Contextual_DB import get_keys, get_tags, get_XY, get_words
from .nltk_puk import tokenize,stem



def collector(command):
    temp_list = []
    collected = command 
    for phras in collected:
        temp_list.append(phras[0])
    return temp_list


unpacked_bag = collector(get_words(None)) # responds

unpacked_keys = collector(get_keys(None)) # patterns одной категории

unpacked_tags = collector(get_tags()) # Категории


#unpacked_keys # ALL WORDS
#unpacked_bag # RESPONSES
#unpacked_tags # TAGS

# Вытащить Категории + Ключи из дб
collected_XY = get_XY() # СБОР (КАТЕГОРИЙ, КЛЮЧЕЙ)

def XY_list(): # РАСПАКОВКА [(КАТЕГОРИЯ, КЛЮЧЕЙ),]
    pred_xy = []
    for cross in collected_XY:
        pred_xy.append((tokenize(cross[1]),cross[0]))
    return pred_xy

def tokenize_list(list_object):
    bag_of_words = []
    for x in list_object:
        bag_of_words.extend(tokenize(x))
    return bag_of_words


ignore_words = ['?','!','.',',']



class Data_Preparation():
    def prepare_AW(self,keys_list):
        self.all_words = tokenize_list(keys_list)
        self.all_words = [stem(w) for w in self.all_words if w not in ignore_words]
        self.all_words = sorted(set(self.all_words))
        return self.all_words
    
    def prepare_TL(self,tags_list):
        self.tag_list = sorted(set(tags_list))
        return self.tag_list
    
    def prepare_XY(self):
        self.xy = XY_list() # НО КСТА, мб и не нужно делать эту дичь
        return self.xy

dt = Data_Preparation()

all_words = dt.prepare_AW(unpacked_keys)
tag_list = dt.prepare_TL(unpacked_tags)
xy = dt.prepare_XY()
print(tag_list)

def refresh():
    global unpacked_bag, unpacked_keys, unpacked_tags
    unpacked_bag = collector(get_words(None)) # responds
    unpacked_keys = collector(get_keys(None)) # patterns одной категории
    unpacked_tags = collector(get_tags()) # Категории

    global all_words, tag_list, xy
    all_words = dt.prepare_AW(unpacked_keys)
    tag_list = dt.prepare_TL(unpacked_tags)
    print(tag_list)
    xy = dt.prepare_XY()



if __name__ == '__main__':
    refresh()
