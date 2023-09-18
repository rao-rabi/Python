def add(f_num, s_num):
    sum = f_num + s_num
    return sum


res = add(f_num=34, s_num=22)  # keyword arguments
print(res)

# write a program to convert symbols to emojis

def emoji_converter(message):
    words = message.split(" ")

    emojis = {
    ":)": "😄",
    ":(": "😥",
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
    
    
message = input("> ")   
print(emoji_converter(message))


# function to print data from ditionary

customers = {
   0: {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
   1: {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
   2: {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
}

def find_name(dict, dict_id, target):
    return dict[dict_id][target]


res = find_name(customers, 2, "last name")
print(res)


# function with optional unknown arguments

def football(name, score, **optional_param):
    print(f"{name} has won the match by {score}")
    for key,value in optional_param.items():
        print(f"{key}--->{value}")
        
        
football("Real madrid", "1-0", Injured = "none", overtime = "yes")

        