calls = 0

def count_calls():
 global calls
 calls += 1

 def string_info (string):
     count_calls()
     return (len(string), string.upper(), string.lower())


    def is_contains (string,list_to_search):
        count_calls()
        return string in list_to_search

 #Прошу подсказать как жолжна быть записана 3 функция

