import time
print("vítej u gejm3")
time.sleep(3)
print("je to tu zase, špatná hra lol")
a = input("pain? (pain/nepain): ")
if a ==("pain"):
    print("pain")
    b =input("fakt pain? (mega pain/pain): ")
    if b ==("pain"):
        print("tak pain")
        time.sleep(3)
        c = input("od 1 do 10 jak moc pain? (1/2/3/4/5/6/7/8/9/10): ")
        if c ==("1"):
            print("tak to je OK")
            time.sleep(20)
        elif c ==("2"):
            print("lil hurt")
            time.sleep(20)
        elif c ==("3"):
            print("lil mor pain")
            time.sleep(20)
        elif c ==("4"):
            print("lechce podprůměrný pain")
            time.sleep(20)
        elif c ==("5"):
            print("medium pain")
            time.sleep(20)
        elif c ==("6"):
            print("lil mor then medium pain")
            time.sleep(20)
        elif c ==("7"):
            print("ouch!")
            time.sleep(20)
        elif c ==("8"):
            print("i wanna die more then this pain")
            time.sleep(20)
        elif c ==("9"):
            print("hmmmm yeah the pain is made out of pain")
            time.sleep(20)
        elif c ==("10"):
            print("you are ded not big surprice")
            time.sleep(20)
    elif b ==("mega pain"):
        print("tak to teda jo")
        time.sleep(10)
elif a ==("nepain"):
    print("špatně")
    time.sleep(10)