def isHappy(n):
    check = []
    while n != 1:
        sum = 0
        for i in str(n):
            sum += int(i)**2
        if sum in check:
            return False
        check.append(sum)
        n = sum
    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        
    print("Results saved to /app/bind_mount/output.txt")