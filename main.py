
import art
import random
import game_data

print(art.logo)


def uniqueRandomNumber(a):
  
  flag=0
  while flag==0:
    x =random.randint(0,len(game_data.data)-1)
    flag=1
    for i in a:
      if(i==x):
        flag=0
        break
  return x

# print(f"Compare A: {name1}, {name2} from {Country}.")

repeatedNumbers=[]
def compareMain():
  randomNumber = uniqueRandomNumber(repeatedNumbers)
  repeatedNumbers.append(randomNumber)
  
  dictionary_1 = game_data.data[randomNumber]
  # print(dictionary_1)
  
  
 
  for a in game_data.data:
    myflag = 1
    flag=0
    if dictionary_1["country"].lower() == a["country"].lower() :
      
      
      for b in repeatedNumbers:
       if game_data.data.index(a) == b  :
         flag=1
      if flag==0:
        myflag=0
        dictionary_2 = a
        repeatedNumbers.append(game_data.data.index(a))
        # print(game_data.data.index(a))
        break
  
  if myflag ==0 :    
    combinedDisctionary =[
      dictionary_1,
      dictionary_2,
      ]
    return combinedDisctionary
  else:
    combinedDisctionary =[
      dictionary_1,
      ]
    return combinedDisctionary
    # print(dictionary_2)
    
    # print(f"Compare A: {dictionary_1['name']}, {dictionary_2['name']} from {dictionary_2['country']}.")
  # else:
  #   # print(f"Compare A: {dictionary_1['name']} from {dictionary_1['country']}.")
  #   return dictionary_1


def count_Score(Combined_dictionary_1,Combined_dictionary_2):
  score_of_Team_A = 0
  score_of_Team_B = 0
  if len(Combined_dictionary_1) ==2:
    score_of_Team_A = int(Combined_dictionary_1[0]['follower_count']) + int(Combined_dictionary_1[1]['follower_count'])
  else:
    score_of_Team_A = int(Combined_dictionary_1[0]['follower_count'] )
  
  if len(Combined_dictionary_2) ==2:
    score_of_Team_B = int(Combined_dictionary_2[0]['follower_count']) + int(Combined_dictionary_2[1]['follower_count'])
  else:
    score_of_Team_B = int(Combined_dictionary_2[0]['follower_count'] )
    
  print(f"{score_of_Team_A}  + {score_of_Team_B}")
  
  if score_of_Team_A > score_of_Team_B :
    return 1
  else:
    return 0
  





def print_dictionary(Combined_dictionary_1,Combined_dictionary_2):
  if len(Combined_dictionary_1) ==2:
    print(f" \n \n Compare A: {Combined_dictionary_1[0]['name']}, {Combined_dictionary_1[1]['name']} from {Combined_dictionary_1[1]['country']}.")
  else:
    print(f" \n \n Compare A: {Combined_dictionary_1[0]['name']} from {Combined_dictionary_1[0]['country']}.")
  
  print(art.vs)
  
  
  if len(Combined_dictionary_2) ==2:
    print(f" \n \n Compare B: {Combined_dictionary_2[0]['name']}, {Combined_dictionary_2[1]['name']} from {Combined_dictionary_2[1]['country']}.")
  else:
    print(f" \n \n Compare A: {Combined_dictionary_2[0]['name']} from {Combined_dictionary_2[0]['country']}.")


def main():
  
  Combined_dictionary_1 =compareMain()
  Combined_dictionary_2 =compareMain()
  print_dictionary(Combined_dictionary_1,Combined_dictionary_2)
  
  flag = count_Score(Combined_dictionary_1,Combined_dictionary_2)
  
  userInput = int(input("Which team has more followers: \n 1. Team A \n 2. Team B  \n Your Choice:"))

  

  if flag==1 and userInput ==1:
    
    print("team A wins, You win")
    return 1
  elif flag==0 and userInput ==2:
    print("team B wins, You win")
    return 1
  else:
    print("You loose")
    return 0

flag_for_next_round =1
end =1

while end ==1:
  if(flag_for_next_round ==1):
    flag_for_next_round = main()
  elif flag_for_next_round ==0:
    print("you loose")
    break
  else:
    end =0
    print("you have completed all levels , You Win")
    break
  

print(art.credit)
print("\n \n \n")
print(art.reez)
