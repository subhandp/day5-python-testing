def convert(num):
    units = ("", "satu ", "dua ", "tiga ", "empat ","lima ", "enam ", "tujuh ","delapan ", "sembilan ", "sepuluh ", "sebelas ", "duabelas ", "tigabelas ", "empatbelas ", "limabelas ","enambelas ", "tujuhbelas ", "delapanbelas ", "sembilanbelas ")
    tens =("", "", "duapuluh ", "tigapuluh ", "empatpuluh ", "limapuluh ","enampuluh ","tujuhpuluh ","delapanpuluh ","sembilanpuluh ")

    if num < 0:
        return "minus "+convert(-num)

    if num<20:
        return  units[num] 

    if num<100:

        return  tens[num // 10]  + units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"ratus " +convert(int(num % 100))

    if num<1000000: 
        return  convert(num // 1000) + "ribu " + convert(int(num % 1000))

    if num < 1000000000:    
        return convert(num // 1000000) + "juta " + convert(int(num % 1000000))

    return convert(num // 1000000000)+ "milliar "+ convert(int(num % 1000000000))
