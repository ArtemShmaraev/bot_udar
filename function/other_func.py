from data.user import User


def top(id, tochnost, db_sess):
    d = []
    if tochnost == 1:
        user = db_sess.query(User).filter(User.tg_id == id).first()
        if user.balance < 100:
            return "Для участия в этом топе необходимо набрать 100 🎯\nУ вас " + str(
                user.balance) + " 🎯"
    for user in db_sess.query(User).all():
        if tochnost == 1:
            if user.balance < 100:
                continue
            else:
                d.append([round((user.good * 100) / (user.good + user.bad), 2), user.name.split()[0], user.tg_id])
        elif tochnost == 2:
            d.append([user.nedel, user.name.split()[0], user.tg_id])
        else:
            d.append([user.balance, user.name.split()[0], user.tg_id])
    d.sort(reverse=True)
    kubok = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "11)", "12)", "13)", "14)", "15)", "16)",
             "17)", "18)", "19)", "20)", "21)", "22)", "23)", "24)", "25)", "26)", "27)", "28)", "29)", "30)", "31)",
             "32)", "33)", "34)", "35)", "36)", "37)", "38)", "39)", "40)", "41)", "42)", "43)", "44)", "45)"]
    fraz = ["Счёт", "Точность"]
    smail = [" 🎯", "% 🎲"]
    st = ""
    do = 15
    if id == 365209216:
        do = 45
    mesto = ""
    for i in range(len(d)):
        if i < min(do, len(d)):
            st += f"{kubok[i]} [https://vk.com/id{str(d[i][2])}|{d[i][1]}] {fraz[tochnost % 2]}: {str(d[i][0])}{smail[tochnost % 2]}\n"
        if id in d[i]:
            mesto = "\nВы на " + str(i + 1) + " месте 🏆"
            if i > min(do, len(d)):
                break
    return st + mesto


def oshibki(user):
    f = open("q.txt", "r", encoding="utf-8").read().split("\n")
    s = []
    st = ""
    sp = user.bad_slova.split()
    for i in range(len(f)):
        if sp[i] != "0":
            s.append([sp[i], i])
    s.sort(reverse=True)
    if len(s) == 0:
        return "Список ваших ошибок пуст, и я думаю что это очень хорошо 🥳"
    else:
        for i in range(min(30, len(s))):
            st += f"{i + 1}) {f[s[i][1]].lower()} Ошибок: {s[i][0]} ❌\n"
        return st


def summa(db_sess):
    balance = 0
    good = 0
    bad = 0
    k = 0
    nedel = 0
    for user in db_sess.query(User).all():
        if user.tg_id == 442844239:
            continue
        k += 1
        balance += user.balance
        nedel += user.nedel
        good += user.good
        bad += user.bad
    return f"Общий счёт: {str(balance)} 🎯\nСредний счет: {str(round(balance / k, 2))} 🎯\nВсего правильно: {str(good)}" \
           f" ✅\nВсего неправильно: {str(bad)} ❌\nСредняя точность {round((good * 100) / max(1, (good + bad)), 4)}" \
           f"% 🎲 \nЗа неделю: {str(nedel)} 🎯 "


def sbros_nedeli(db_sess):
    for user in db_sess.query(User).all():
        user.nedel = 0
    db_sess.commit()
