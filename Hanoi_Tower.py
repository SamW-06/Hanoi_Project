#Tower of Hanoi certfication project fcc.


def hanoi_solver(disks):
    output = ''
    a = [disk + 1 for disk in range(disks)][::-1]
    b = []
    c = []

    output += f"{a} {b} {c}\n"
    def move(n, left,right, mid):
        nonlocal output
        if n == 1:
            right.append(left.pop())
            output += f"{a} {b} {c}\n"
        else:
            move(n - 1, left, mid, right)
            right.append(left.pop())
            output += f"{a} {b} {c}\n"
            move(n - 1, mid, right, left)

    move(disks, a, c,b)
    return output.strip('\n')

print(hanoi_solver(2))
