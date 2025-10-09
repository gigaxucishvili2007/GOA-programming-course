'''4) შექმენი ფუნქცნია lion4() სადაც შევქმნით ცარიელ მასივს და for loop ის გამოყენეით + .appnd() შევიტანთ მხოლოდ კენტ რიცხვებს'''

def lion4(arr1):
    for x in range(1,10,2):
        arr1.append(arr1)
print(lion4([]))