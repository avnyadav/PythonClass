if __name__=="__main__":
    N = 9
    M = N*3
    N_MIDDLE = (N+1)//2
    M_MIDDLE = (M+1)//2
    print(f"N_MIDDLE: {N_MIDDLE} and M_MIDDLE:{M_MIDDLE}")
    WELCOME_RANGE = (M_MIDDLE-3,M_MIDDLE+3)
    print(f"{WELCOME_RANGE}")
    WELCOME_MESSAGE = "WELCOME"
    pattern = ".|."
    increment_number = 2
    pattern_repeat_number = 1
    for row in range(1,N+1):
        #print(pattern_repeat_number)
        pattern_messgae = pattern*pattern_repeat_number
        pattern_messgae_length = len(pattern_messgae)
        pattern_middle  = (pattern_messgae_length+1)//2
        number = pattern_middle-1
        pattern_range = (M_MIDDLE-number,M_MIDDLE+number)
        for col in range(1,M+1):
            
            if row==N_MIDDLE and col>=WELCOME_RANGE[0] and col<=WELCOME_RANGE[1]:
                print(WELCOME_MESSAGE[col-WELCOME_RANGE[0]],end="")
            elif row!=N_MIDDLE and col>=pattern_range[0] and col<=pattern_range[1]:
                print(pattern_messgae[col-pattern_range[0]],end="")
            else:
                print("-",end="")
        if row==N_MIDDLE:
            increment_number= increment_number*-1
        pattern_repeat_number = pattern_repeat_number+increment_number  
        print("")
        
