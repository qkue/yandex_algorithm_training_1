# Python 3.12.1

n, m = map(int, input().split())
anna_cubs = {int(input()) for _ in range(n)}
borya_cubs = {int(input()) for _ in range(m)}

intersection_cubs = sorted(anna_cubs & borya_cubs)
print(len(intersection_cubs))
if intersection_cubs:
    print(*intersection_cubs)

annas_dif = sorted(anna_cubs - borya_cubs)
print(len(annas_dif))
if annas_dif:
    print(*annas_dif)

borya_dif = sorted(borya_cubs - anna_cubs)
print(len(borya_dif))
if borya_dif:
    print(*borya_dif)
